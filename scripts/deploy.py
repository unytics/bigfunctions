import os
import shutil
import argparse
import math

from google.api_core.exceptions import BadRequest
import google.cloud.bigquery
import yaml
import jinja2

PYTHON_BUILD_DIR = 'build_python'
DATASETS = os.environ.get('BIGFUNCTIONS_DATASETS', '').split(',')
BIGFUNCTIONS = [f.replace('.yaml', '') for f in os.listdir('bigfunctions')]

BQ = google.cloud.bigquery.Client()


def prefix_lines_with_line_number(string: str, starting_index: int = 1) -> str:
    """Example:

    >>> print(prefix_lines_with_line_number('Hello\\nWorld!'))
    1: Hello
    2: World!
    """
    lines = string.split("\n")
    max_index = starting_index + len(lines) - 1
    nb_zeroes = int(math.log10(max_index)) + 1
    numbered_lines = [str(index + starting_index).zfill(nb_zeroes) + ": " + line for index, line in enumerate(lines)]
    return "\n".join(numbered_lines)


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
        print(f'giving invoker permission to connection service account with command `{add_invoker_role_command}`')
        os.system(add_invoker_role_command)

        conf['remote_connection'] = '749389685934.eu.remote-bigfunctions'
        conf['remote_endpoint'] = f'https://{bigfunction.replace("_", "-")}-ccbxjzt67q-ew.a.run.app'

    template_file = f'scripts/templates/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        dataset=fully_qualified_dataset,
        name=bigfunction,
        filename=filename,
        **conf,
    )
    try:
        BQ.query(query).result()
    except BadRequest as e:
        e.message += "\nQuery:\n" + prefix_lines_with_line_number(query)
        raise e
    print('successfully created', fully_qualified_bigfunction)





parser = argparse.ArgumentParser(description='Deploy BigFunction')
parser.add_argument('bigfunction')
args = parser.parse_args()

if args.bigfunction == '*':
    for dataset in DATASETS:
        for bigfunction in BIGFUNCTIONS:
            deploy(f'{dataset}.{bigfunction}')
elif '.' in args.bigfunction:
    deploy(args.bigfunction)
else:
    for dataset in DATASETS:
        deploy(f'{dataset}.{args.bigfunction}')

