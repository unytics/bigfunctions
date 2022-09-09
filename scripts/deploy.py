import os
import argparse

import google.cloud.bigquery
import yaml
import jinja2

DATASETS = ['bigfunctions.eu', 'bigfunctions.us', 'bigfunctions.asia_east1', 'bigfunctions.asia_east2', 'bigfunctions.asia_northeast1', 'bigfunctions.asia_northeast2', 'bigfunctions.asia_northeast3', 'bigfunctions.asia_south1', 'bigfunctions.asia_southeast1', 'bigfunctions.australia_southeast1', 'bigfunctions.europe_north1', 'bigfunctions.europe_west1', 'bigfunctions.europe_west2', 'bigfunctions.europe_west3', 'bigfunctions.europe_west4', 'bigfunctions.europe_west6', 'bigfunctions.northamerica_northeast1', 'bigfunctions.southamerica_east1', 'bigfunctions.us_central1', 'bigfunctions.us_east1', 'bigfunctions.us_east4', 'bigfunctions.us_west1', 'bigfunctions.us_west2']
BIGFUNCTIONS = [f.replace('.yaml', '') for f in os.listdir('bigfunctions')]

BQ = google.cloud.bigquery.Client()


def deploy(fully_qualified_bigfunction):
    dataset = '.'.join(fully_qualified_bigfunction.split('.')[:2])
    bigfunction = fully_qualified_bigfunction.split('.')[-1]
    filename = f'bigfunctions/{bigfunction}.yaml'
    conf = yaml.safe_load(open(filename, encoding='utf-8').read().replace('{BIGFUNCTIONS_DATASET}', dataset))

    if 'template' in conf:
        conf['code'] += f'''
            create or replace temp table bigfunction_result as
            select
                (select json from bigfunction_result) as json,
                (select {dataset}.render_string(
                    """
                    {conf['template']}
                    """,
                    to_json_string(json)
                )
                from bigfunction_result) as html
            ;
        '''
    conf['libraries'] = [
        {
            'source_url': library,
            # 'filename': library.replace('https://', '').replace('http://', '').split('/', 1)[1],
            'cloudstorage_url': f"gs://bigfunctions_js_libs/{library}",
        }
        for library in conf.get('libraries', [])
    ]

    template_file = f'scripts/templates/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        dataset=dataset,
        name=bigfunction,
        filename=filename,
        **conf,
    )
    BQ.query(query).result()
    print('successfully created', fully_qualified_bigfunction)





parser = argparse.ArgumentParser(description='Deploy BigFunction')
parser.add_argument('bigfunction')
args = parser.parse_args()

if args.bigfunction == '*':
    for dataset in DATASETS:
        for bigfunction in BIGFUNCTIONS:
            deploy(f'{dataset}.{bigfunction}')
else:
    deploy(args.bigfunction)


