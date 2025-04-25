import multiprocessing
import os

import click
import requests
import yaml
from click_help_colors import HelpColorsGroup
from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer

from . import bigfunctions as bf
from . import utils

TABLES_FOLDER = 'data'
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
        for dataset in datasets:
            bigfunction = bf.BigFunction(name, project=project, dataset=dataset)
            bigfunction.deploy()
        # bigfunction = bf.BigFunction(name, project=project, dataset=datasets[0])
        # bigfunction.deploy()
        # if len(datasets) > 1:
        #     with multiprocessing.Pool(processes=8) as pool:
        #         pool.map(
        #             bf.BigFunction.deploy,
        #             [
        #                 bf.BigFunction(name, project=project, dataset=dataset)
        #                 for dataset in datasets[1:]
        #             ]
        #         )


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
@click.option('--config', default='config.yaml', help='Path to the config file')
def generate(config):
    """
    Generate markdown files for documentation from yaml bigfunctions files
    """
    bf.generate_doc()
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
@click.argument('bigfunction')
def generate_description_improvement(bigfunction):
    """
    Generate markdown files for documentation from yaml bigfunctions files
    """
    bigfunctions = [bigfunction.strip() for bigfunction in bigfunction.split(',')]
    if bigfunction == 'ALL':
        bigfunctions = bf.BIGFUNCTIONS
    for name in bigfunctions:
        bigfunction = bf.BigFunction(name)
        bigfunction.generate_description_improvement()


@docs.command()
@click.argument('folder_path')
def generate_folder_readme(folder_path):
    """
    Generate README.md for bigfunctions folder
    """
    folder = bf.Folder(folder_path)
    folder.generate_readme()


@docs.command()
@click.option('--config', default='config.yaml', help='Path to the config file')
@click.option('--port', default='8000', help='Port to serve docs on')
def serve(config, port):
    """
    Serve docs locally on http://localhost:8000
    """
    bf.generate_doc()

    class EventHandler(RegexMatchingEventHandler):
        def on_any_event(self, event):
            print(f'File {event.src_path} {event.event_type} --> generating README files...')
            bf.generate_doc()
    # event_handler = EventHandler(regexes=[r'.*\.yaml'])
    # observer = Observer()
    # observer.schedule(event_handler, BIGFUNCTIONS_FOLDER, recursive=True)
    # observer.start()
    # bf.bf.generate_doc()
    os.system(f'mkdocs serve -a localhost:{port}')


@cli.group()
def config():
    """
    Get, set or generate config
    """
    pass


@config.command('get')
@click.argument('name')
@click.option('--config', default='config.yaml', help='Path to the config file')
def get_value(name, config):
    '''
    Print value of config named NAME in config.yaml
    '''
    print(get_config_value(name, config))


@config.command()
@click.option('--config', default='config.yaml', help='Path to the config file')
def generate_key_pair_for_secrets(config):
    """
    Generate a key pair for secret encrytion/decryption
    """
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # PRINT PRIVATE KEY
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    print(pem.decode())

    # STORE PUBLIC KEY IN CONFIG
    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key = pem.decode()

    with open(config, 'a', encoding='utf-8') as file:
        file.write(
            '\npublic_key_to_encrypt_secrets: |\n  ' +
            '\n  '.join(public_key.split('\n'))
        )
