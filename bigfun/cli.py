import multiprocessing
import os
import shutil

import click
import jinja2
import yaml
from click_help_colors import HelpColorsGroup
from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer

from . import bigfunctions as bf
from . import utils

TABLES_FOLDER = 'data'
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
WEBSITE_CONFIG_FOLDER = THIS_FOLDER + '/website'
CATEGORIES_DOC_TEMPLATE_FILENAME = f'{THIS_FOLDER}/templates/categories.md'
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

    def init_docs_folder():
        os.makedirs('docs', exist_ok=True)
        shutil.rmtree('docs/bigfunctions', ignore_errors=True)
        os.makedirs('docs/bigfunctions')

    def copy_readme_and_contributing():
        if not os.path.isfile('README.md'):
            print('INFO: CREATING A README.md FILE IN CURRENT DIRECTORY WHICH WILL BE THE ROOT CONTENT OF THE WEBSITE')
            open('README.md', 'w', encoding='utf-8').write('# Hello from README!')
        shutil.copyfile('README.md', 'docs/README.md')
        if os.path.isfile('CONTRIBUTING.md'):
            shutil.copyfile('CONTRIBUTING.md', 'docs/CONTRIBUTING.md')

    def copy_default_site_config():
        if not os.path.isfile('mkdocs.yml'):
            print('INFO: CREATING mkdocs.yml FILE in CURRENT DIRECTORY. It is the configuration file of the website...')
            shutil.copyfile(WEBSITE_CONFIG_FOLDER + '/mkdocs.yml', 'mkdocs.yml')
        if not os.path.isdir('docs/assets'):
            print('INFO: COPYING assets FOLDER into docs FOLDER...')
            shutil.copytree(WEBSITE_CONFIG_FOLDER + '/assets', 'docs/assets')
        if not os.path.isdir('docs/theme_overrides'):
            print('INFO: COPYING theme_overrides FOLDER into docs FOLDER...')
            shutil.copytree(WEBSITE_CONFIG_FOLDER + '/theme_overrides', 'docs/theme_overrides')

    def generate_bigfunctions_markdown(bigfunctions):
        for bigfunction in bigfunctions:
            open(f'docs/bigfunctions/{bigfunction.name}.md', 'w', encoding='utf-8').write(bigfunction.doc)

    def copy_screenshots_to_docs_folder():
        for image in [f for f in os.listdir('bigfunctions') if f.endswith('.png')]:
            shutil.copy(f'bigfunctions/{image}', f'docs/bigfunctions/{image}')

    def generate_bigfunctions_list_markdown(bigfunctions):
        mkdocs_config = yaml.safe_load(open('mkdocs.yml', encoding='utf-8').read())
        categories = mkdocs_config['bigfunctions_categories']
        for category in categories:
            category['bigfunctions'] = [b.config for b in bigfunctions if b.config['category'] == category['name']]
        categories = [category for category in categories if category['bigfunctions']]
        categories_template = jinja2.Template(open(CATEGORIES_DOC_TEMPLATE_FILENAME, encoding='utf-8').read())
        categories_doc = categories_template.render(categories=categories, project=project, dataset=dataset)
        open('bigfunctions/README.md', 'w', encoding='utf-8').write(categories_doc)
        open('docs/bigfunctions/README.md', 'w', encoding='utf-8').write(categories_doc)

    bigfunctions = [
        bf.BigFunction(bigfunction_name, project=project, dataset=dataset)
        for bigfunction_name in bf.list_bigfunctions()
    ]
    init_docs_folder()
    copy_readme_and_contributing()
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
    if not os.path.isdir('bigfunctions'):
        os.makedirs('bigfunctions')
    url = f'https://raw.githubusercontent.com/unytics/bigfunctions/main/bigfunctions/{bigfunction}.yaml'
    if bigfunction.startswith('https://'):
        url = bigfunction
        bigfunction = bigfunction.split('/')[-1].split('.')[0]
    utils.download(url, f'bigfunctions/{bigfunction}.yaml')


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
        bigfunctions = bf.list_bigfunctions()

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
    # observer.start()
    # bf.generate_doc(project, dataset)
    os.system('mkdocs serve')
