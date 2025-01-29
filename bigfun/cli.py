import glob
import multiprocessing
import os
import shutil

import click
import jinja2
import requests
import yaml
from click_help_colors import HelpColorsGroup
from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer

from . import bigfunctions as bf
from . import utils

TABLES_FOLDER = 'data'
PEOPLE_FILENAME = 'people.yaml'
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
MKDOCS_DEFAULT_FILE =  f'{THIS_FOLDER}/templates/mkdocs.yml'
DOC_FOLDER_TEMPLATE_FILENAME = f'{THIS_FOLDER}/templates/folder.md'
CONFIGS = {}

def get_config_value(name, config_filename):
    if config_filename not in CONFIGS:
        if os.path.exists(config_filename):
            with open(config_filename, encoding='utf-8') as file:
                CONFIGS[config_filename] = yaml.safe_load(file) or {}
        else:
            CONFIGS[config_filename] = {}

    config = CONFIGS[config_filename]
    if name in config:
        return config[name]

    text, default = {
        'project':                   ("Default GCP project where to deploy bigfunctions", None),
        'dataset':                   ("Default dataset where to deploy bigfunctions", None),  # eu,us,asia_east1,asia_east2,asia_northeast1,asia_northeast2,asia_northeast3,asia_south1,asia_southeast1,australia_southeast1,europe_north1,europe_west1,europe_west2,europe_west3,europe_west4,europe_west6,northamerica_northeast1,southamerica_east1,us_central1,us_east1,us_east4,us_west1,us_west2
        'project_for_tests':         ("Default GCP project where to deploy bigfunctions for TESTING purposes", None),
        'dataset_for_tests':         ("Default dataset where to deploy bigfunctions for TESTING purposes", None),  # eu,us,asia_east1,asia_east2,asia_northeast1,asia_northeast2,asia_northeast3,asia_south1,asia_southeast1,australia_southeast1,europe_north1,europe_west1,europe_west2,europe_west3,europe_west4,europe_west6,northamerica_northeast1,southamerica_east1,us_central1,us_east1,us_east4,us_west1,us_west2
    }[name]
    config[name] = click.prompt(text, default=default)
    with open(config_filename, 'w', encoding='utf-8') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)
    return config[name]


def generate_doc(project, dataset):

    def get_people():
        if not os.path.isfile(PEOPLE_FILENAME):
            return {}
        with open(PEOPLE_FILENAME, encoding='utf-8') as f:
            people = yaml.safe_load(f.read())
        return {
            person['name']: person
            for person in people
        }

    def enrich_bigfunctions_author(bigfunctions):
        people = get_people()
        for bigfunction in bigfunctions:
            if 'author' not in bigfunction.config:
                continue
            author = bigfunction.config['author']
            if isinstance(author, dict):
                # backward compatibility
                continue
            if author in people:
                bigfunction._config['author'] = people[author]
            else:
                bigfunction._config['author'] = {'name': author}

    def init_docs_folder():
        os.makedirs('docs', exist_ok=True)
        shutil.rmtree('docs/bigfunctions', ignore_errors=True)
        os.makedirs('docs/bigfunctions')

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

    def generate_bigfunctions_markdown(bigfunctions):
        for bigfunction in bigfunctions:
            open(f'docs/bigfunctions/{bigfunction.name}.md', 'w', encoding='utf-8').write(bigfunction.doc)

    def copy_screenshots_to_docs_folder():
        images = glob.glob('bigfunctions/**/*.png', recursive=True)
        for image in images:
            destination_filename = 'docs/bigfunctions/' + image.split('/')[-1]
            print(image, destination_filename)
            shutil.copy(image, destination_filename)

    def generate_bigfunctions_list_markdown(bigfunctions):
        content = '# BigFunctions\n\n'
        folders_to_add = None
        if os.path.isfile('bigfunctions/README.md'):
            content = open('bigfunctions/README.md', encoding='utf-8').read()
            if content.startswith('---'):
                content_without_first_line = content[content.find('\n'):]
                front_matter = content[:content.find('\n---')]
                front_matter = yaml.safe_load(front_matter)
                if 'folders' in front_matter:
                    folders_to_add = front_matter['folders']
        folder_template = jinja2.Template(open(DOC_FOLDER_TEMPLATE_FILENAME, encoding='utf-8').read())
        folders = {}
        for bigfunction in bigfunctions:
            folder = bigfunction.config_folder
            if folders_to_add and folder not in folders_to_add:
                continue
            if folder not in folders:
                folder_readme = f"## {folder.replace('_', ' ').title()}"
                if os.path.isfile(f'bigfunctions/{folder}/README.md'):
                    folder_readme = open(f'bigfunctions/{folder}/README.md', encoding='utf-8').read()
                folders[folder] = {'path': folder, 'readme': folder_readme, 'bigfunctions': []}
            folders[folder]['bigfunctions'].append(bigfunction.config)
        if folders_to_add:
            folders = [folders[folder] for folder in folders_to_add]
        else:
            folders = folders.values()
        folders_content = '\n\n\n'.join([folder_template.render(**folder) for folder in folders])

        open('docs/bigfunctions/README.md', 'w', encoding='utf-8').write(content + '\n' * 3 + folders_content)

    bigfunctions = [
        bf.BigFunction(bigfunction_name, project=project, dataset=dataset)
        for bigfunction_name in bf.BIGFUNCTIONS
    ]
    enrich_bigfunctions_author(bigfunctions)
    init_docs_folder()
    create_homepage_if_not_exists()
    copy_default_site_config()
    generate_bigfunctions_markdown(bigfunctions)
    copy_screenshots_to_docs_folder()
    generate_bigfunctions_list_markdown(bigfunctions)


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='cyan'
)
def cli():
    pass


@cli.command()
@click.argument('bigfunction')
def get(bigfunction):
    """
    Download BIGFUNCTION yaml file from unytics/bigfunctions github repo
    """
    if bigfunction.startswith('https://'):
        url = bigfunction
        bigfunction = bigfunction.split('/')[-1].split('.')[0]
        filepath = f'bigfunctions/{bigfunction}.yaml'
    else:
        url = 'https://api.github.com/repos/unytics/bigfunctions/git/trees/main?recursive=true'
        resp = requests.get(url)
        res = resp.json()
        filepaths = [f['path'] for f in res['tree'] if f['path'].startswith('bigfunctions/') and f['path'].endswith(f'{bigfunction}.yaml')]
        if not filepaths:
            utils.handle_error(f'Function `{bigfunction}` does NOT exist in repo https://github.com/unytics/bigfunctions')
        filepath = filepaths[0]
        url = f'https://raw.githubusercontent.com/unytics/bigfunctions/main/{filepath}'
    folder = '/'.join(filepath.split('/')[:-1])
    os.makedirs(folder, exist_ok=True)
    utils.download(url, filepath)


@cli.command()
@click.argument('bigfunction')
@click.option('--config', default='config.yaml', help='Path to the config file')
def test(bigfunction, config):
    """
    Test BIGFUNCTION
    """
    project = get_config_value('project_for_tests', config)
    dataset = get_config_value('dataset_for_tests', config)
    bigfunction = bf.BigFunction(bigfunction, project=project, dataset=dataset)
    bigfunction.test()


@cli.command()
@click.argument('bigfunction')
@click.option('--project', help='Google Cloud project where the function will be deployed')
@click.option('--dataset', help='BigQuery dataset name where the function will be deployed')
@click.option('--config', default='config.yaml', help='Path to the config file')
def deploy(bigfunction, project, dataset, config):
    """
    Deploy BIGFUNCTION

    Deploy the function defined in `bigfunctions/{BIGFUNCTION}.yaml` file. If BIGFUNCTION = 'ALL' then all bigfunctions contained in bigfunctions folder are deployed.
    """
    project = project or get_config_value('project', config)
    dataset = dataset or get_config_value('dataset', config)
    datasets = [dataset.strip() for dataset in dataset.split(',')]
    bigfunctions = [bigfunction.strip() for bigfunction in bigfunction.split(',')]
    if bigfunction == 'ALL':
        bigfunctions = bf.BIGFUNCTIONS

    for name in bigfunctions:
        bigfunction = bf.BigFunction(name, project=project, dataset=datasets[0])
        bigfunction.deploy()
        if len(datasets) > 1:
            with multiprocessing.Pool(processes=8) as pool:
                pool.map(
                    bf.BigFunction.deploy,
                    [
                        bf.BigFunction(name, project=project, dataset=dataset)
                        for dataset in datasets[1:]
                    ]
                )


@cli.command()
@click.argument('table')
@click.option('--project', help='Google Cloud project where the table is created')
@click.option('--dataset', help='BigQuery dataset name where the table is created')
@click.option('--config', default='config.yaml', help='Path to the config file')
def load_table(table, project, dataset, config):
    """
    Create or replace bigquery table TABLE with data contained in `data/{TABLE}.csv`.
    If TABLE=ALL, then all tables defined in `data` folder are created.
    """
    from .load_table import load_table as upload_table
    project = project or get_config_value('project', config)
    dataset = dataset or get_config_value('dataset', config)
    datasets = [dataset.strip() for dataset in dataset.split(',')]
    if table == 'ALL':
        tables = [f.replace('.yaml', '') for f in os.listdir(TABLES_FOLDER) if f.endswith('.yaml')]
    else:
        tables = [table]

    with multiprocessing.Pool(processes=8) as pool:
        pool.map(
            upload_table,
            [f'{project}.{dataset}.{table}' for dataset in datasets for table in tables]
        )


@cli.group()
def docs():
    """
    Generate, serve and publish documentation
    """
    pass


@docs.command()
@click.option('--project', help='Google Cloud project where the table is created')
@click.option('--dataset', help='BigQuery dataset name where the table is created')
@click.option('--config', default='config.yaml', help='Path to the config file')
def generate(project, dataset, config):
    """
    Generate markdown files for documentation from yaml bigfunctions files
    """
    project = project or get_config_value('project', config)
    dataset = dataset or get_config_value('dataset', config)
    generate_doc(project, dataset)
    os.system('mkdocs build')


@docs.command()
@click.argument('bigfunction')
def generate_use_case(bigfunction):
    """
    Generate markdown files for documentation from yaml bigfunctions files
    """
    bigfunctions = [bigfunction.strip() for bigfunction in bigfunction.split(',')]
    if bigfunction == 'ALL':
        bigfunctions = bf.BIGFUNCTIONS
    for name in bigfunctions:
        bigfunction = bf.BigFunction(name)
        bigfunction.generate_use_case()


@docs.command()
@click.option('--project', help='Google Cloud project where the table is created')
@click.option('--dataset', help='BigQuery dataset name where the table is created')
@click.option('--config', default='config.yaml', help='Path to the config file')
def serve(project, dataset, config):
    """
    Serve docs locally on http://localhost:8000
    """
    project = project or get_config_value('project', config)
    dataset = dataset or get_config_value('dataset', config)
    generate_doc(project, dataset)

    class EventHandler(RegexMatchingEventHandler):
        def on_any_event(self, event):
            print(f'File {event.src_path} {event.event_type} --> generating README files...')
            generate_doc(project, dataset)
    # event_handler = EventHandler(regexes=[r'.*\.yaml'])
    # observer = Observer()
    # observer.schedule(event_handler, BIGFUNCTIONS_FOLDER, recursive=True)
    # observer.start()
    # bf.generate_doc(project, dataset)
    os.system('mkdocs serve')
