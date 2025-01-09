import functools
import glob
import json
import os
import re
import shutil
import tempfile

import jinja2
import yaml

from .utils import (BigQuery, CloudRun, build_and_upload_npm_package,
                    generate_content, handle_error, merge_dict, print_command,
                    print_info, print_success)

BIGFUNCTIONS_FOLDER = 'bigfunctions'
DEFAULT_CONFIG_FILENAME = './config.yaml'
REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'
BIGFUNCTION_DOC_TEMPLATE_FILENAME = f'{TEMPLATE_FOLDER}/bigfunction.md'
DEFAULT_CONFIG = yaml.safe_load(open(DEFAULT_CONFIG_FILENAME, encoding='utf-8').read()) if os.path.isfile(DEFAULT_CONFIG_FILENAME) else {}
TESTS_FOLDER = 'tests'
USE_CASES_FOLDER = 'use_cases'

BIGFUNCTION_DOC_TEMPLATE = jinja2.Template(open(BIGFUNCTION_DOC_TEMPLATE_FILENAME, encoding='utf-8').read())





def list_bigfunctions():
    filenames = sorted([f.replace("\\", "/") for f in glob.glob(f'{BIGFUNCTIONS_FOLDER}/**/*.yaml', recursive=True)])
    return {
        f.split('/')[-1].replace('.yaml', ''): f
        for f in filenames
    }


BIGFUNCTIONS = list_bigfunctions()


class BigFunction:

    def __init__(self, name, project=None, dataset=None, **config_override):
        self.name = name
        self.config_override = config_override
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
        if self.name not in BIGFUNCTIONS:
            handle_error(f'Could not find a yaml file in `{BIGFUNCTIONS_FOLDER}` folder for bigfunction `{self.name}`')
        return BIGFUNCTIONS[self.name]

    @property
    def config_folder(self):
        return '/'.join(self.config_filename.replace('bigfunctions/', '').split('/')[:-1])

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
            self._config['short_description'] = self._config['description'].split('\n')[0]
            self._config['signature'] = (
                self.name +
                '(' +
                ', '.join(argument['name'] for argument in self._config.get('arguments', [])) +
                ')'
            )
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

    @property
    def location(self):
        return self.dataset.location

    @property
    def use_case_filename(self):
        return f'{USE_CASES_FOLDER}/{self.name}.md'

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
        argument_values = [str(value).strip() for value in self.config['examples'][0]['arguments']]
        arguments = zip(argument_names, argument_values)
        template_file = f'{TEMPLATE_FOLDER}/function_py_test.py'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        code = template.render(
            project=self.project,
            arguments=arguments,
            init_code=self.config.get('init_code', '').strip(),
            code=self.config['code'].strip()
        )

        print(code)
        os.makedirs(TESTS_FOLDER, exist_ok=True)
        code_filename = f'{TESTS_FOLDER}/bf__{self.name}.py'
        print_info(f'Generating python code file {code_filename}')
        with open(code_filename, 'w', encoding='utf-8') as out:
            out.write(code)
        print_info(f'Executing python code file {code_filename}')
        os.system(f'python {code_filename}')

    def deploy(self):
        self.config['dataset_location'] = self.dataset.location
        if 'npm_packages' in self.config:
            self._deploy_npm_packages()
        if self.config['type'] == 'function_py':
            self._deploy_cloud_run()
        template_file = f'{TEMPLATE_FOLDER}/{self.config["type"]}.sql'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        query = template.render(**self.config)
        print_info('Creating function in dataset')
        self.bigquery.query(query, location=self.location)
        print_success(f'successfully created {self.project}.{self.dataset_name}.{self.name}')

    @property
    def doc(self):
        if os.path.isfile(self.use_case_filename):
            self.config['use_case'] = open(self.use_case_filename, encoding='utf-8').read()
        return BIGFUNCTION_DOC_TEMPLATE.render(**self.config)

    def generate_use_case(self, overwrite_if_exists=False):
        if os.path.isfile(self.use_case_filename):
            if not overwrite_if_exists:
                return
            os.remove(self.use_case_filename)

        doc = self.doc
        prompt = '\n\n'.join([
            'Give a use case of this function',
            'FUNCTION MARKDOWN DOCUMENTATION:',
            self.doc,
        ])
        use_case = generate_content(prompt)
        os.makedirs(USE_CASES_FOLDER, exist_ok=True)
        with open(self.use_case_filename, 'w', encoding='utf-8') as file:
            file.write(use_case)

    def _deploy_npm_packages(self):
        if 'bucket_js_dependencies' not in self.config:
            handle_error('Please provide the name of the cloud storage bucket to host js dependencies. The bucket name must be set in config as a variable named: `bucket_js_dependencies`. You must have objectAdmin permissions on it to create or replace files. The users of your function must have read access')
        self.config['js_libraries_urls'] = [
            build_and_upload_npm_package(npm_package, self.config['bucket_js_dependencies'], self.project)
            for npm_package in self.config['npm_packages']
        ]

    def _deploy_cloud_run(self):
        cloud_run_service = 'bf-' + self.name.replace("_", "-")
        cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(self.dataset.location, self.dataset.location)
        self.config['cloud_run_location'] = cloud_run_location
        with tempfile.TemporaryDirectory() as folder:
            remote_connection = self.bigquery.get_or_create_remote_connection(self.project, self.dataset.location, REMOTE_CONNECTION_NAME)
            self.bigquery.set_remote_connection_users(remote_connection.name, self.dataset.users)

            self._create_folder_with_cloudrun_code(folder)
            cloud_run = CloudRun(cloud_run_service, self.project, cloud_run_location)
            cloud_run.deploy(folder, self.config.get('cloud_run', {}))
            cloud_run.add_invoker_permission(f'serviceAccount:{remote_connection.cloud_resource.service_account_id}')

            self.config['remote_endpoint'] = cloud_run.url
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
                    'cryptography',
                    self.config.get('requirements', '')
                ])
            )

        template = jinja2.Template(open(f'{TEMPLATE_FOLDER}/Dockerfile', encoding='utf-8').read())
        dockerfile = template.render(**self.config)
        with open(f'{folder}/Dockerfile', 'w', encoding='utf-8') as out:
            out.write(dockerfile)
