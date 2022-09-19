import os
import shutil
import argparse

import google.cloud.bigquery
import yaml
import jinja2

PYTHON_BUILD_DIR = 'build_python'
DATASETS = ['bigfunctions.eu', 'bigfunctions.us', 'bigfunctions.asia_east1', 'bigfunctions.asia_east2', 'bigfunctions.asia_northeast1', 'bigfunctions.asia_northeast2', 'bigfunctions.asia_northeast3', 'bigfunctions.asia_south1', 'bigfunctions.asia_southeast1', 'bigfunctions.australia_southeast1', 'bigfunctions.europe_north1', 'bigfunctions.europe_west1', 'bigfunctions.europe_west2', 'bigfunctions.europe_west3', 'bigfunctions.europe_west4', 'bigfunctions.europe_west6', 'bigfunctions.northamerica_northeast1', 'bigfunctions.southamerica_east1', 'bigfunctions.us_central1', 'bigfunctions.us_east1', 'bigfunctions.us_east4', 'bigfunctions.us_west1', 'bigfunctions.us_west2']
BIGFUNCTIONS = [f.replace('.yaml', '') for f in os.listdir('bigfunctions')]

BQ = google.cloud.bigquery.Client()


def deploy(fully_qualified_bigfunction):
    project, dataset, bigfunction = fully_qualified_bigfunction.split('.')
    fully_qualified_dataset = f'{project}.{dataset}'
    bigfunction = fully_qualified_bigfunction.split('.')[-1]
    filename = f'bigfunctions/{bigfunction}.yaml'
    conf = yaml.safe_load(open(filename, encoding='utf-8').read().replace('{BIGFUNCTIONS_DATASET}', fully_qualified_dataset))

    if 'template' in conf:
        conf['code'] += f'''
            create or replace temp table bigfunction_result as
            select
                (select json from bigfunction_result) as json,
                (select {fully_qualified_dataset}.render_string(
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

    if conf['type'] == 'function_py':
        if os.path.exists(PYTHON_BUILD_DIR):
            shutil.rmtree(PYTHON_BUILD_DIR)
        os.makedirs(PYTHON_BUILD_DIR)

        template_file = f'scripts/templates/{conf["type"]}.py'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        python_code = template.render(**conf)
        with open(f'{PYTHON_BUILD_DIR}/main.py', 'w', encoding='utf-8') as out:
            out.write(python_code)

        with open(f'{PYTHON_BUILD_DIR}/requirements.txt', 'w', encoding='utf-8') as out:
            out.write('gunicorn\nflask\ngoogle-cloud-error-reporting\n' + conf['requirements'])

        shutil.copy('scripts/templates/Dockerfile', PYTHON_BUILD_DIR)

        deploy_command = f'gcloud run deploy {bigfunction.replace("_", "-")} --source {PYTHON_BUILD_DIR} --region europe-west1 --project {project} --no-allow-unauthenticated'
        print(f'deploying cloud run {bigfunction} with command `{deploy_command}`')
        os.system(deploy_command)

        add_invoker_role_command = f'gcloud run services add-iam-policy-binding {bigfunction.replace("_", "-")} --region europe-west1 --member=serviceAccount:bqcx-749389685934-ielt@gcp-sa-bigquery-condel.iam.gserviceaccount.com --role=roles/run.invoker'

        conf['remote_connection'] = '749389685934.eu.remote-bigfunctions'
        conf['remote_endpoint'] = 'https://transform-text2sentiment-score-ccbxjzt67q-ew.a.run.app'

    template_file = f'scripts/templates/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        dataset=fully_qualified_dataset,
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


