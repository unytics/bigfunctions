import os
import argparse

import google.cloud.bigquery
import yaml
import jinja2


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
            'cloudstorage_url': f"gs://{CONF['js_libs_bucket']}/{library}",
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
    print(query)
    BQ.query(query).result()
    print('successfully created', fully_qualified_bigfunction)





parser = argparse.ArgumentParser(description='Deploy BigFunction')
parser.add_argument('bigfunction')
args = parser.parse_args()

deploy(args.bigfunction)

