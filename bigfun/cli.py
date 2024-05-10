import os
import shutil
import multiprocessing

import yaml
import click
from click_help_colors import HelpColorsGroup
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

from . import bigfunctions as bf
from . import utils



TABLES_FOLDER = 'data'
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
WEBSITE_CONFIG_FOLDER = THIS_FOLDER + '/website'
CONFIG_FILENAME = 'config.yaml'
CONFIG = {}
if os.path.exists(CONFIG_FILENAME):
    CONFIG = yaml.safe_load(open(CONFIG_FILENAME, encoding='utf-8').read()) or {}


def get_config_value(name):
    if name in CONFIG:
        return CONFIG[name]

    text, default = {
        'project':                   ("Default GCP project where to deploy bigfunctions", None),
        'dataset':                   ("Default dataset where to deploy bigfunctions", None),  # eu,us,asia_east1,asia_east2,asia_northeast1,asia_northeast2,asia_northeast3,asia_south1,asia_southeast1,australia_southeast1,europe_north1,europe_west1,europe_west2,europe_west3,europe_west4,europe_west6,northamerica_northeast1,southamerica_east1,us_central1,us_east1,us_east4,us_west1,us_west2
        'project_for_tests':         ("Default GCP project where to deploy bigfunctions for TESTING purposes", None),
        'dataset_for_tests':         ("Default dataset where to deploy bigfunctions for TESTING purposes", None),  # eu,us,asia_east1,asia_east2,asia_northeast1,asia_northeast2,asia_northeast3,asia_south1,asia_southeast1,australia_southeast1,europe_north1,europe_west1,europe_west2,europe_west3,europe_west4,europe_west6,northamerica_northeast1,southamerica_east1,us_central1,us_east1,us_east4,us_west1,us_west2
    }[name]
    CONFIG[name] = click.prompt(text, default=default)
    with open(CONFIG_FILENAME, 'w', encoding='utf-8') as outfile:
        yaml.dump(CONFIG, outfile, default_flow_style=False)
    return CONFIG[name]


def generate_doc():
    os.makedirs('docs', exist_ok=True)

    if not os.path.isfile('README.md'):
        print('INFO: CREATING A README.md FILE IN CURRENT DIRECTORY WHICH WILL BE THE ROOT CONTENT OF THE WEBSITE')
        open('README.md', 'w', encoding='utf-8').write('# Hello from README!')

    if not os.path.isfile('mkdocs.yml'):
        print('INFO: CREATING mkdocs.yml FILE in CURRENT DIRECTORY. It is the configuration file of the website...')
        shutil.copyfile(WEBSITE_CONFIG_FOLDER + '/mkdocs.yml', 'mkdocs.yml')

    if not os.path.isdir('docs/assets'):
        print('INFO: COPYING assets FOLDER into docs FOLDER...')
        shutil.copytree(WEBSITE_CONFIG_FOLDER + '/assets', 'docs/assets')

    if not os.path.isdir('docs/mkdocs_material_overrides'):
        print('INFO: COPYING mkdocs_material_overrides FOLDER into docs FOLDER...')
        shutil.copytree(WEBSITE_CONFIG_FOLDER + '/mkdocs_material_overrides', 'docs/mkdocs_material_overrides')

    shutil.copyfile('README.md', 'docs/README.md')
    if os.path.isfile('CONTRIBUTING.md'):
        shutil.copyfile('CONTRIBUTING.md', 'docs/CONTRIBUTING.md')

    project = get_config_value('project')
    dataset = get_config_value('dataset')
    bf.generate_doc(project, dataset)

    for image in [f for f in os.listdir('bigfunctions') if f.endswith('.png')]:
        shutil.copy(f'bigfunctions/{image}', f'docs/bigfunctions/{image}')


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
    '''
    Download BIGFUNCTION yaml file from unytics/bigfunctions github repo
    '''
    if not os.path.isdir('bigfunctions'):
        os.makedirs('bigfunctions')
    url = f'https://raw.githubusercontent.com/unytics/bigfunctions/main/bigfunctions/{bigfunction}.yaml'
    utils.download(url, f'bigfunctions/{bigfunction}.yaml')




@cli.command()
@click.argument('bigfunction')
def test(bigfunction):
    '''
    Test BIGFUNCTION
    '''
    project = get_config_value('project_for_tests')
    dataset = get_config_value('dataset_for_tests')
    bigfunction = bf.BigFunction(bigfunction, project=project, dataset=dataset)
    bigfunction.test()


@cli.command()
@click.argument('bigfunction')
@click.option('--project', help='Google Cloud project where the function will be deployed')
@click.option('--dataset', help='BigQuery dataset name where the function will be deployed')
def deploy(bigfunction, project, dataset):
    '''
    Deploy BIGFUNCTION

    Deploy the function defined in `bigfunctions/{BIGFUNCTION}.yaml` file. If BIGFUNCTION = 'ALL' then all bigfunctions contained in bigfunctions folder are deployed.
    '''
    project = project or get_config_value('project')
    dataset = dataset or get_config_value('dataset')
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
                    BigFunction.deploy,
                    [
                        bf.BigFunction(name, project=project, dataset=dataset)
                        for dataset in datasets[1:]
                    ]
                )



@cli.command()
@click.argument('table')
@click.option('--project', help='Google Cloud project where the table is created')
@click.option('--dataset', help='BigQuery dataset name where the table is created')
def load_table(table, project, dataset):
    '''
    Create or replace bigquery table TABLE with data contained in `data/{TABLE}.csv`.
    If TABLE=ALL, then all tables defined in `data` folder are created.
    '''
    from .load_table import load_table as upload_table
    project = project or get_config_value('project')
    dataset = dataset or get_config_value('dataset')
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
    '''
    Generate, serve and publish documentation
    '''
    pass


@docs.command()
def generate():
    '''
    Generate markdown files for documentation from yaml bigfunctions files
    '''
    generate_doc()
    os.system('mkdocs build')



@docs.command()
def serve():
    '''
    Serve docs locally on http://localhost:8000
    '''
    generate_doc()

    class EventHandler(RegexMatchingEventHandler):
        def on_any_event(self, event):
            print(f'File {event.src_path} {event.event_type} --> generating README files...')
            generate_doc()
    # event_handler = EventHandler(regexes=[r'.*\.yaml'])
    # observer = Observer()
    # observer.schedule(event_handler, BIGFUNCTIONS_FOLDER, recursive=True)
    # observer.start()
    # bf.generate_doc(project, dataset)
    os.system('mkdocs serve')
