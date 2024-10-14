import os

import google.cloud.bigquery
import yaml

from .utils import BigQuery, print_success

DATA_FOLDER = 'data'


def load_table(table):
    project, dataset, table_name = table.split('.')
    conf = yaml.safe_load(open(f'{DATA_FOLDER}/{table_name}.yaml', encoding='utf-8').read())
    load_config = conf['load_config']
    source_format = load_config['source_format']
    filename = f'{DATA_FOLDER}/{table_name}.{source_format.lower()}'
    if not os.path.isfile(filename):
        return
    bigquery = BigQuery(project)
    with open(filename, 'rb') as file:
        bigquery.create_or_replace_destination_table(table, conf)
        job_config = google.cloud.bigquery.job.LoadJobConfig(**load_config)
        bigquery.load_table_from_file(file, table, job_config=job_config).result()
    print_success('successfully loaded ' + table)
