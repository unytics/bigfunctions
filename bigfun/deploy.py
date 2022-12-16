import re
import os
import shutil

import yaml
import jinja2

from .utils import bigquery, CloudRun, handle_error, print_success, print_info, print_warning

REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
PYTHON_BUILD_DIR = 'build_python'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'


def deploy_cloud_run(bigfunction, conf, fully_qualified_dataset, project):
    if os.path.exists(PYTHON_BUILD_DIR):
        shutil.rmtree(PYTHON_BUILD_DIR)
    os.makedirs(PYTHON_BUILD_DIR)

    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.py'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    python_code = template.render(**conf)
    with open(f'{PYTHON_BUILD_DIR}/main.py', 'w', encoding='utf-8') as out:
        out.write(python_code)

    with open(f'{PYTHON_BUILD_DIR}/requirements.txt', 'w', encoding='utf-8') as out:
        out.write('gunicorn\nflask\ngoogle-cloud-error-reporting\n' + conf['requirements'])

    shutil.copy(f'{TEMPLATE_FOLDER}/Dockerfile', PYTHON_BUILD_DIR)

    dataset = bigquery.get_dataset(fully_qualified_dataset)

    remote_connection = bigquery.get_or_create_remote_connection(project, dataset.location, REMOTE_CONNECTION_NAME)
    try:
        bigquery.set_remote_connection_users(remote_connection.name, ["group:data-champions@nickel.eu"])
    except:
        print_warning('Could not change remote connections users')

    cloud_run_service = 'bf-' + bigfunction.replace("_", "-")
    cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(dataset.location, dataset.location)
    cloud_run = CloudRun(cloud_run_service, project, cloud_run_location)
    cloud_run.deploy(PYTHON_BUILD_DIR)
    cloud_run.add_invoker_permission(f'serviceAccount:{remote_connection.cloud_resource.service_account_id}')

    conf['remote_endpoint'] = cloud_run.url
    conf['remote_connection'] = re.sub(
        r"projects/(\d+)/locations/([\w-]+)/connections/([\w-]+)",
        r"\g<1>.\g<2>.\g<3>",
        remote_connection.name,
    )


def deploy(fully_qualified_bigfunction):
    project, dataset, bigfunction = fully_qualified_bigfunction.replace('`', '').split('.')
    fully_qualified_dataset = f'`{project}`.{dataset}'
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
        deploy_cloud_run(bigfunction, conf, fully_qualified_dataset, project)

    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        dataset=fully_qualified_dataset,
        name=bigfunction,
        filename=filename,
        **conf,
    )
    print_info('Creating function in dataset')
    bigquery.query(query)
    print_success('successfully created ' + fully_qualified_bigfunction)


