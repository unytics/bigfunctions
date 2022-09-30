import argparse

import google.cloud.bigquery
import yaml

DATA_FOLDER = 'data'
DATASETS = ['bigfunctions.eu', 'bigfunctions.us', 'bigfunctions.asia_east1', 'bigfunctions.asia_east2', 'bigfunctions.asia_northeast1', 'bigfunctions.asia_northeast2', 'bigfunctions.asia_northeast3', 'bigfunctions.asia_south1', 'bigfunctions.asia_southeast1', 'bigfunctions.australia_southeast1', 'bigfunctions.europe_north1', 'bigfunctions.europe_west1', 'bigfunctions.europe_west2', 'bigfunctions.europe_west3', 'bigfunctions.europe_west4', 'bigfunctions.europe_west6', 'bigfunctions.northamerica_northeast1', 'bigfunctions.southamerica_east1', 'bigfunctions.us_central1', 'bigfunctions.us_east1', 'bigfunctions.us_east4', 'bigfunctions.us_west1', 'bigfunctions.us_west2']


BQ = google.cloud.bigquery.Client()


def create_or_replace_destination_table(table, conf):
    BQ.query(f'''
        create or replace table `{table}`
        (
            {','.join([col['name'] + ' ' + col['type'] + ' options(description="' + col['description'] + '")' for col in conf['schema']])}
        )
        options(
            description="""{conf['description']}"""
        )
    ''').result()


def load(table):
    table_name = table.split('.')[-1]
    conf = yaml.safe_load(open(f'{DATA_FOLDER}/{table_name}.yaml', encoding='utf-8').read())
    with open(f'{DATA_FOLDER}/{table_name}.csv', 'rb') as file:
        create_or_replace_destination_table(table, conf)
        job_config = google.cloud.bigquery.job.LoadJobConfig(source_format= 'CSV')
        BQ.load_table_from_file(file, table, job_config=job_config)
    print('successfully loaded', table)


parser = argparse.ArgumentParser(description='create or replace table with data contained in data folder')
parser.add_argument('table')
args = parser.parse_args()


if args.table.startswith('*.'):
    table = args.table[2:]
    for dataset in DATASETS:
        load(f'{dataset}.{table}')
else:
    load(args.table)
