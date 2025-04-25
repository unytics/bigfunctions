import functools
import glob
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
PEOPLE_FILENAME = 'docs/people.yaml'
NAV_FILENAME = 'docs/.nav.yml'
PEOPLE = None
REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'
BIGFUNCTION_DOC_TEMPLATE_FILENAME = f'{TEMPLATE_FOLDER}/bigfunction.md'
DOC_FOLDER_TEMPLATE_FILENAME = f'{TEMPLATE_FOLDER}/folder.md'
MKDOCS_DEFAULT_FILE =  f'{TEMPLATE_FOLDER}/mkdocs.yml'
DEFAULT_CONFIG = yaml.safe_load(open(DEFAULT_CONFIG_FILENAME, encoding='utf-8').read()) if os.path.isfile(DEFAULT_CONFIG_FILENAME) else {}
TESTS_FOLDER = 'tests'
USE_CASES_FOLDER = 'use_cases'

BIGFUNCTION_DOC_TEMPLATE = jinja2.Template(open(BIGFUNCTION_DOC_TEMPLATE_FILENAME, encoding='utf-8').read())
DOC_FOLDER_TEMPLATE = jinja2.Template(open(DOC_FOLDER_TEMPLATE_FILENAME, encoding='utf-8').read())





def list_bigfunctions():
    filenames = sorted([f.replace("\\", "/") for f in glob.glob(f'{BIGFUNCTIONS_FOLDER}/**/*.yaml', recursive=True)])
    return {
        f.split('/')[-1].replace('.yaml', ''): f
        for f in filenames
    }


def list_people():
    if not os.path.isfile(PEOPLE_FILENAME):
        return {}
    with open(PEOPLE_FILENAME, encoding='utf-8') as f:
        people_list = yaml.safe_load(f.read())
        return {
            person['name']: person
            for person in people_list
        }


BIGFUNCTIONS = list_bigfunctions()
PEOPLE = list_people()


class BigFunction:

    def __init__(self, name, **config_override):
        self.name = name
        self.config_override = config_override
        self._config_from_file = None
        self._config = None
        self._bigquery = None
        self._dataset = None

    @property
    def filename(self):
        if self.name not in BIGFUNCTIONS:
            handle_error(f'Could not find a yaml file in `{BIGFUNCTIONS_FOLDER}` folder for bigfunction `{self.name}`')
        return BIGFUNCTIONS[self.name]

    @property
    def folder(self):
        return '/'.join(self.filename.split('/')[:-1])

    @property
    def config_from_file(self):
        if self._config_from_file is None:
            if not os.path.isfile(self.filename):
                handle_error(f'Could not find configuration file {self.filename}')
            content = open(self.filename, encoding='utf-8').read()
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
            self._config['filename'] = self.filename
            self._config['short_description'] = self._config['description'].split('\n')[0]
            self._config['signature'] = (
                self.name +
                '(' +
                ', '.join(argument['name'] for argument in self._config.get('arguments', [])) +
                ')'
            )
            if 'author' in self._config and isinstance(self._config['author'], str):
                self._config['author'] = PEOPLE.get(self._config['author']) or {'name': self._config['author']}
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
        argument_values = [value for value in self.config['examples'][0]['arguments']]
        argument_types = [arg['type'] for arg in self.config['arguments']]
        arguments = zip(argument_names, argument_values, argument_types)
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
        os.makedirs(os.path.dirname(code_filename), exist_ok=True)
        with open(code_filename, 'w', encoding='utf-8') as out:
            out.write(code)
        print_info(f'Executing python code file {code_filename}')
        requirements = ' '.join([f'--with "{r.strip()}"' for r in self.config.get('requirements', '').split('\n')])
        command = f'uv run --no-project  {requirements}  {code_filename}'
        os.system(command)

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

    def generate_description_improvement(self):
        prompt = '\n\n'.join([
            'Improve the description of this bigquery function. Return only the description.',
            'FUNCTION YAML DEFINITION:',
            open(self.filename, encoding='utf-8').read(),
        ])
        description = generate_content(prompt)
        print(description)

    def generate_use_case(self, overwrite_if_exists=False):
        if os.path.isfile(self.use_case_filename):
            if not overwrite_if_exists:
                return
            os.remove(self.use_case_filename)

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


class Folder:

    def __init__(self, path):
        self._readme = None
        self.path = path
        self.name = path.split('/')[-1]
        self.title, self.content, self.frontmatter = self.parse_readme()
        self.clean_title = re.sub('[^a-zA-Z ]', '', self.title).strip()
        self.inner_link = f'#{self.clean_title.lower().replace(" ", "-")}'
        self.frontmatter['title'] = self.frontmatter.get('title') or self.title
        self.depth = len(path.split('/')) - 1
        self.nb_bigfunctions = len([1 for b in BIGFUNCTIONS.values() if b.startswith(f'{path}/')])
        self.subfolder_names = self.frontmatter.get('folders') or [d.name for d in os.scandir(path) if d.is_dir()]
        self.subfolder_paths = [f'{path}/{subfolder}' for subfolder in self.subfolder_names]
        self.subfolders = [Folder(subfolder_path) for subfolder_path in self.subfolder_paths]
        self.bigfunctions = [BigFunction(name) for name, _path in BIGFUNCTIONS.items() if re.match(f'{path}/([^/]+.yaml)', _path)]
        self.dict = {
            'name': self.name,
            'title': self.title,
            'depth': self.depth,
            'path': self.path,
            'inner_link': self.inner_link,
            'frontmatter': self.frontmatter,
            'content': self.content,
            'content_contains_title': True if re.findall(r'^\s*# .+', self.content, re.MULTILINE) else False,
            'nb_bigfunctions': self.nb_bigfunctions,
            'subfolders': [subf.dict for subf in self.subfolders],
            'bigfunctions': [b.config for b in self.bigfunctions],
        }

    def parse_readme(self):
        readme = ''
        if os.path.isfile(f'{self.path}/README.md'):
            readme = open(f'{self.path}/README.md', encoding='utf-8').read()
        readme = readme.strip()

        frontmatter = {}
        frontmatter_matches = re.findall(r'^---([\s\S]*?)---\n', readme)
        if readme.startswith('---') and frontmatter_matches:
            frontmatter_string = frontmatter_matches[0]
            frontmatter = yaml.safe_load(frontmatter_string)
            readme = readme.replace(f'---{frontmatter_string}---', '').strip()

        title = self.name.replace('_', ' ').title()
        if readme.startswith('#'):
            title, readme = (readme + '\n').split('\n', 1)
            title = title.lstrip('# ')

        return title, readme, frontmatter

    def generate_readme(self):
        prompt = '''
        BigFunctions is a catalog of BigQuery functions. Functions are categorized in folders. Generate the description of the folder containing the following functions:


        '''.replace('\n        ', '')
        prompt += '\n\n--------------------\n\n '.join(['FUNCTION `' + b.name + '``: ' + b.config['description'] for b in self.bigfunctions])
        print(prompt)
        readme = generate_content(prompt)
        with open(f'{self.path}/README.md', 'w', encoding='utf-8') as file:
            file.write(readme)

    @property
    def doc(self):
        return DOC_FOLDER_TEMPLATE.render(**self.dict)

    def generate_docs(self):
        docs = []
        docs.append((f'{self.path}/README.md', self.doc))
        for subfolder in self.subfolders:
            docs.extend(subfolder.generate_docs())
        for bigfunction in self.bigfunctions:
            docs.append((f'bigfunctions/{bigfunction.name}.md', bigfunction.doc))
        return docs

    @property
    def nav(self):
        return {
            self.clean_title: [
                *[f'{self.path}/README.md'],
                *[subfolder.nav for subfolder in self.subfolders],
                *[f'bigfunctions/{bigfunction.name}.md' for bigfunction in self.bigfunctions]
            ]
        }


def generate_doc():

    def init_docs_folder():
        os.makedirs('docs', exist_ok=True)
        shutil.rmtree('docs/bigfunctions', ignore_errors=True)
        os.makedirs('docs/bigfunctions')

    def generate_markdown_files(folder):
        docs = folder.generate_docs()
        for path, content in docs:
            path = f'docs/{path}'
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

    def generate_nav(folder):
        mkdocs_config = open('mkdocs.yml', encoding='utf-8').read()
        if '{BIGFUNCTIONS_DOC}' not in mkdocs_config:
            return
        mkdocs_config = re.sub(' !.*', ' ""', mkdocs_config)
        mkdocs_config = yaml.safe_load(mkdocs_config)
        nav = mkdocs_config['nav']
        bigfunctions_index = next((
            k for k, tab in enumerate(nav)
            if tab == '{BIGFUNCTIONS_DOC}'
        ), None)
        if bigfunctions_index is None:
            return
        nav[bigfunctions_index] = folder.nav
        with open(NAV_FILENAME, 'w', encoding='utf-8') as file:
            file.write(yaml.dump({'nav': nav}))

    def create_homepage_if_not_exists():
        if os.path.isfile('docs/index.md'):
            return
        print('INFO: CREATING docs/index.md FILE WHICH WILL BE THE ROOT CONTENT OF THE WEBSITE')
        content = '\n\n'.join([
            '# BigFunctions!',
            'Update this page content by editing `docs/index.md`',
            '[Explore Functions](bigfunctions/){ .md-button }',
        ])
        open('docs/index.md', 'w', encoding='utf-8').write(content)

    def copy_default_site_config():
        if not os.path.isfile('mkdocs.yml'):
            print('INFO: CREATING mkdocs.yml FILE in CURRENT DIRECTORY. It is the configuration file of the website...')
            shutil.copyfile(MKDOCS_DEFAULT_FILE, 'mkdocs.yml')

    def copy_screenshots_to_docs_folder():
        images = glob.glob('bigfunctions/**/*.png', recursive=True)
        for image in images:
            destination_filename = 'docs/bigfunctions/' + image.split('/')[-1]
            destination_dir = os.path.dirname(destination_filename)
            os.makedirs(destination_dir, exist_ok=True)
            shutil.copy(image, destination_filename)

    init_docs_folder()
    create_homepage_if_not_exists()
    copy_default_site_config()
    folder = Folder(BIGFUNCTIONS_FOLDER)
    generate_markdown_files(folder)
    generate_nav(folder)
    copy_screenshots_to_docs_folder()
