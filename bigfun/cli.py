import os 

import yaml
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from .utils import print_color

CONFIG_FILENAME = 'config.yaml'
CONFIG = {}
if os.path.exists(CONFIG_FILENAME):
    CONFIG = yaml.safe_load(open(CONFIG_FILENAME, encoding='utf-8').read())
BIGFUNCTIONS = [f.replace('.yaml', '') for f in os.listdir('bigfunctions')]


def get_config_value(name):
    if name in CONFIG:
        return CONFIG[name]

    text, default = {
        'default_gcp_project':          ("Default GCP project where to deploy bigfunctions", "bigfunctions"),
        'default_gcp_project_for_test': ("Default GCP project where to deploy bigfunctions for testing purposes", "bigfunctions"),
        'default_datasets':             ("Default dataset(s) where to deploy bigfunctions (comma separated is many)", "eu,us,asia_east1,asia_east2,asia_northeast1,asia_northeast2,asia_northeast3,asia_south1,asia_southeast1,australia_southeast1,europe_north1,europe_west1,europe_west2,europe_west3,europe_west4,europe_west6,northamerica_northeast1,southamerica_east1,us_central1,us_east1,us_east4,us_west1,us_west2"),
        'default_datasets_for_test':    ("Default dataset(s) where to deploy bigfunctions for testing purposes (comma separated is many)", "test_eu,test_us,test_asia_east1,test_asia_east2,test_asia_northeast1,test_asia_northeast2,test_asia_northeast3,test_asia_south1,test_asia_southeast1,test_australia_southeast1,test_europe_north1,test_europe_west1,test_europe_west2,test_europe_west3,test_europe_west4,test_europe_west6,test_northamerica_northeast1,test_southamerica_east1,test_us_central1,test_us_east1,test_us_east4,test_us_west1,test_us_west2"),
    }[name]
    CONFIG[name] = click.prompt(text, default=default)
    with open(CONFIG_FILENAME, 'w', encoding='utf-8') as outfile:
        yaml.dump(CONFIG, outfile, default_flow_style=False)
    return value


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='cyan'
)
def cli():
    pass


@cli.command()
@click.argument('bigfunction')
def deploy(bigfunction):
    '''
    Deploy BIGFUNCTION

    - If BIGFFUNCTION = '{project}.{dataset}.{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in dataset {dataset} of project {project}

    - If BIGFFUNCTION = '{dataset}.{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in dataset {dataset} of default project defined in `config.yaml` file. If no default dataset is defined yet, it will be prompted and saved in `config.yaml`.

    - If BIGFFUNCTION = '{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in default dataset of default project defined in `config.yaml` file. If these default values are not defined yet, they will be prompted and saved in `config.yaml`.

    - If BIGFUNCTION = '*' then all bigfunctions contained in bigfunctions folder will be deployed in default datasets of default project in `config.yaml` file. If these default values are not defined yet, they will be prompted and saved in `config.yaml`.
    '''
    from .deploy import deploy
    if bigfunction == '*':
        project = get_config_value('default_gcp_project')
        datasets = get_config_value('default_datasets')
        bigfunctions = BIGFUNCTIONS
    elif len(bigfunction.split('.')) == 1:
        project = get_config_value('default_gcp_project')
        datasets = get_config_value('default_datasets')
        bigfunctions = [bigfunction]
    elif len(bigfunction.split('.')) == 2:
        project = get_config_value('default_gcp_project')
        datasets = [bigfunction.split('.')[0]]
        bigfunctions = [bigfunction.split('.')[1]]
    elif len(bigfunction.split('.')) == 3:
        project = bigfunction.split('.')[0]
        datasets = [bigfunction.split('.')[1]]
        bigfunctions = [bigfunction.split('.')[2]]
    else:
        raise

    for dataset in datasets:
        for bigfunction in bigfunctions:
            assert bigfunction in bigfunctions, f'Could not find {bigfunction} bigfunction in bigfunctions folder'
            deploy(f'{project}.{dataset}.{bigfunction}')


@cli.command()
@click.argument('bigfunction')
def test(bigfunction):
    '''
    Test BIGFUNCTION

    - If BIGFFUNCTION = '{project}.{dataset}.{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in dataset {dataset} of project {project}

    - If BIGFFUNCTION = '{dataset}.{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in dataset {dataset} of default project defined in `config.yaml` file. If no default dataset is defined yet, it will be prompted and saved in `config.yaml`.

    - If BIGFFUNCTION = '{name}' then bigfunction of name {name} in bigfunctions folder will be deployed in default dataset of default project defined in `config.yaml` file. If these default values are not defined yet, they will be prompted and saved in `config.yaml`.

    - If BIGFUNCTION = '*' then all bigfunctions contained in bigfunctions folder will be deployed in default datasets of default project in `config.yaml` file. If these default values are not defined yet, they will be prompted and saved in `config.yaml`.
    '''
    deploy(bigfunction)         
    # [TODO] make some tests


@cli.group()
def doc():
    '''
    Generate, serve and publish documentation
    '''
    pass

@doc.command()
def generate():
    '''
    Generate markdown files for documentation from yaml bigfunctions files
    '''
    from .generate_doc import generate_doc