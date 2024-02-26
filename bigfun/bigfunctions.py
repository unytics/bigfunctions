import tempfile
import re
import os
import shutil
import json
import functools

import yaml
import jinja2

from .utils import BigQuery, CloudRun, handle_error, print_success, print_info, print_command, build_and_upload_npm_package, merge_dict

BIGFUNCTIONS_FOLDER = 'bigfunctions'
DEFAULT_CONFIG_FILENAME = './config.yaml'
REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'
DEFAULT_CONFIG = yaml.safe_load(open(DEFAULT_CONFIG_FILENAME, encoding='utf-8').read()) if os.path.isfile(DEFAULT_CONFIG_FILENAME) else {}
TESTS_FOLDER = 'tests'


class BigFunction:

    def __init__(self, name, project=None, dataset=None):
        self.name = name
        self.config_override = {}
        if project:
            self.config_override['project'] = project
        if dataset:
            self.config_override['dataset'] = dataset
        self._config_from_file = None
        self._config = None
        self._bigquery = None
        self._dataset = None

    @property
    def config_filename(self):
        return f'bigfunctions/{self.name}.yaml'

    @property
    def config_from_file(self):
        if self._config_from_file is None:
            if not os.path.isfile(self.config_filename):
                handle_error(f'Could not find configuration file {self.config_filename}')
            content = open(self.config_filename, encoding='utf-8').read()
            self._config_from_file = yaml.safe_load(content)
        return self._config_from_file

    @property
    def config(self):
        if self._config is None:
            self._config = functools.reduce(
                merge_dict,
                [dict(DEFAULT_CONFIG), self.config_from_file, self.config_override]
            )
            self._config['name'] = self.name
            self._config['filename'] = self.config_filename
        return self._config

    @property
    def project(self):
        if 'project' not in self.config:
            handle_error('Missing `project` field in config')
        return self.config['project']

    @property
    def dataset_name(self):
        if 'dataset' not in self.config:
            handle_error('Missing `dataset` field in config')
        return self.config['dataset']

    @property
    def bigquery(self):
        if self._bigquery is None:
            self._bigquery = BigQuery(self.project)
        return self._bigquery

    @property
    def dataset(self):
        if self._dataset is None:
            self._dataset = self.bigquery.get_dataset(f'{self.project}.{self.dataset_name}')
        return self._dataset

    def test(self):
        # WARNING: TO CHANGE THIS AND DEPLOY A PYTHON FUNCTION HERE WE NEED TO HAVE A REMOTE CONNECTION PER DATASET AS users between dataset and remote connection are identical
        if self.config['type'] == 'function_py':
            return self._test_python_function_locally()
        self.deploy()
        print_info('Executing function with examples')
        template_file = f'{TEMPLATE_FOLDER}/{self.config["type"]}_test.sql'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        for example in self.config['examples']:
            query = template.render(example=example, **self.config).strip()
            print('')
            print_command(query)
            rows = self.bigquery.query(query)
            print('EXPECTING RESULT:', example['output'])
            print('RESULT:')
            for row in rows:
                print(dict(row))

    def _test_python_function_locally(self):
        argument_names = [arg['name'] for arg in self.config['arguments']]
        argument_values = [value.strip() for value in self.config['examples'][0]['arguments']]
        arguments = zip(argument_names, argument_values)
        template_file = f'{TEMPLATE_FOLDER}/function_py_test.py'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        code = template.render(arguments=arguments, code=self.config['code'].strip())

        print(code)
        os.makedirs(TESTS_FOLDER, exist_ok=True)
        code_filename = f'{TESTS_FOLDER}/{self.name}.py'
        print_info(f'Generating python code file {code_filename}')
        with open(code_filename, 'w', encoding='utf-8') as out:
            out.write(code)
        print_info(f'Executing python code file {code_filename}')
        os.system(f'python {code_filename}')

    def deploy(self):
        if 'npm_packages' in self.config:
            self._deploy_npm_packages()
        if self.config['type'] == 'function_py':
            self._deploy_cloud_run()
        template_file = f'{TEMPLATE_FOLDER}/{self.config["type"]}.sql'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        query = template.render(**self.config)
        print_info('Creating function in dataset')
        self.bigquery.query(query)
        print_success(f'successfully created {self.project}.{self.dataset_name}.{self.name}')

    def _deploy_npm_packages(self):
        if 'bucket_js_dependencies' not in self.config:
            handle_error('Please provide the name of the cloud storage bucket to host js dependencies. The bucket name must be set in config as a variable named: `bucket_js_dependencies`. You must have objectAdmin permissions on it to create or replace files. The users of your function must have read access')
        self.config['js_libraries_urls'] = [
            build_and_upload_npm_package(npm_package, self.config['bucket_js_dependencies'], self.project)
            for npm_package in self.config['npm_packages']
        ]

    def _deploy_cloud_run(self):
        with tempfile.TemporaryDirectory() as folder:
            remote_connection = self.bigquery.get_or_create_remote_connection(self.project, self.dataset.location, REMOTE_CONNECTION_NAME)
            self.bigquery.set_remote_connection_users(remote_connection.name, self.dataset.users)

            self._create_folder_with_cloudrun_code(folder)
            cloud_run_service = 'bf-' + self.name.replace("_", "-")
            cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(self.dataset.location, self.dataset.location)
            cloud_run = CloudRun(cloud_run_service, self.project, cloud_run_location)
            cloud_run.deploy(folder, self.config.get('cloud_run', {}))
            cloud_run.add_invoker_permission(f'serviceAccount:{remote_connection.cloud_resource.service_account_id}')

            self.config['remote_endpoint'] = cloud_run.url
            self.config['cloud_run_location'] = cloud_run_location
            self.config['remote_connection'] = re.sub(
                r"projects/(\d+)/locations/([\w-]+)/connections/([\w-]+)",
                r"\g<1>.\g<2>.\g<3>",
                remote_connection.name,
            )

    def _create_folder_with_cloudrun_code(self, folder):
        print_info(f'Creating folder with Cloud Run code `{folder}`')
        template_file = f'{TEMPLATE_FOLDER}/{self.config["type"]}.py'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        python_code = template.render(**self.config)
        with open(f'{folder}/main.py', 'w', encoding='utf-8') as out:
            out.write(python_code)

        with open(f'{folder}/requirements.txt', 'w', encoding='utf-8') as out:
            out.write(
                '\n'.join([
                    'gunicorn',
                    'flask',
                    'google-cloud-error-reporting',
                    'google-cloud-datastore',
                    'google-cloud-secret-manager',
                    self.config.get('requirements', '')
                ])
            )

        template = jinja2.Template(open(f'{TEMPLATE_FOLDER}/Dockerfile', encoding='utf-8').read())
        dockerfile = template.render(**self.config)
        with open(f'{folder}/Dockerfile', 'w', encoding='utf-8') as out:
            out.write(dockerfile)
