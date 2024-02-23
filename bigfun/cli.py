import os
import multiprocessing

import yaml
import click
from click_help_colors import HelpColorsGroup
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

from . import utils



BIGFUNCTIONS_FOLDER = 'bigfunctions'
TABLES_FOLDER = 'data'
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
    }[name]
    CONFIG[name] = click.prompt(text, default=default)
    with open(CONFIG_FILENAME, 'w', encoding='utf-8') as outfile:
        yaml.dump(CONFIG, outfile, default_flow_style=False)
    return CONFIG[name]


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
    print(bigfunction)


@cli.command()
@click.argument('bigfunction')
@click.option('--project', help='Google Cloud project where the function will be deployed')
@click.option('--dataset', help='BigQuery dataset name where the function will be deployed')
def deploy(bigfunction, project, dataset):
    '''
    Deploy BIGFUNCTION

    Deploy the function defined in `bigfunctions/{BIGFUNCTION}.yaml` file. If BIGFUNCTION = 'ALL' then all bigfunctions contained in bigfunctions folder are deployed.
    '''
    from .bigfunctions import BaseBigFunction
    project = project or get_config_value('project')
    dataset = dataset or get_config_value('dataset')
    datasets = [dataset.strip() for dataset in dataset.split(',')]
    bigfunctions = [bigfunction.strip() for bigfunction in bigfunction.split(',')]
    if bigfunction == 'ALL':
        bigfunctions = [f.replace('.yaml', '') for f in os.listdir(BIGFUNCTIONS_FOLDER)]

    for bigfunction_name in bigfunctions:
        bigfunction = BaseBigFunction(bigfunction_name)
        dataset = datasets[0]
        bigfunction.deploy(project, dataset)
        if len(datasets) > 1:
            with multiprocessing.Pool(processes=8) as pool:
                pool.starmap(
                    bigfunction.deploy,
                    [[project, dataset] for dataset in datasets[1:]]
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
    from .generate_doc import generate_doc
    project = get_config_value('project')
    dataset = get_config_value('project')
    generate_doc(project, dataset)


@docs.command()
def serve():
    '''
    Serve docs locally on http://localhost:8000
    '''
    from .generate_doc import generate_doc
    project = get_config_value('project')
    dataset = get_config_value('dataset')
    class EventHandler(RegexMatchingEventHandler):
        def on_any_event(self, event):
            print(f'File {event.src_path} {event.event_type} --> generating README files...')
            generate_doc(project, dataset)
    # event_handler = EventHandler(regexes=[r'.*\.yaml'])
    # observer = Observer()
    # observer.schedule(event_handler, BIGFUNCTIONS_FOLDER, recursive=True)
    # observer.start()
    generate_doc(project, dataset)
    os.system('mkdocs serve --config-file site/mkdocs.yml')
