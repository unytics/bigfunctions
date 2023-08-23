import tempfile
import re
import os
import shutil

import yaml
import jinja2

from .utils import BigQuery, CloudRun, handle_error, print_success, print_info, build_and_upload_npm_package


REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'


def get_dataset_users(dataset):

    def access_entry2user(access_entry):
        if access_entry.entity_id == 'allAuthenticatedUsers':
            return 'allAuthenticatedUsers'
        entity_type = 'user'
        if access_entry.entity_id.endswith('gserviceaccount.com'):
            entity_type = 'serviceAccount'
        elif access_entry.entity_type == 'groupByEmail':
            entity_type = 'group'
        return f'{entity_type}:{access_entry.entity_id}'

    return [
        access_entry2user(access_entry)
        for access_entry in dataset.access_entries
        if access_entry.entity_id not in ['projectOwners', 'projectWriters', 'projectReaders']
    ]


def create_folder_with_cloudrun_code(conf, folder):
    print_info(f'Creating folder with Cloud Run code `{folder}`')
    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.py'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    python_code = template.render(**conf)
    with open(f'{folder}/main.py', 'w', encoding='utf-8') as out:
        out.write(python_code)

    with open(f'{folder}/requirements.txt', 'w', encoding='utf-8') as out:
        out.write(
            '\n'.join([
                'gunicorn',
                'flask',
                'google-cloud-error-reporting',
                'google-cloud-datastore',
                'google-cloud-secret-manager',
                conf.get('requirements', '')
            ])
        )

    template = jinja2.Template(open(f'{TEMPLATE_FOLDER}/Dockerfile', encoding='utf-8').read())
    dockerfile = template.render(**conf)
    with open(f'{folder}/Dockerfile', 'w', encoding='utf-8') as out:
        out.write(dockerfile)


def deploy_cloud_run(bigquery, bigfunction, conf, fully_qualified_dataset, project):
    if shutil.which('gcloud') is None:
        handle_error('`gcloud` is not installed while needed to deploy a Remote Function.')

    with tempfile.TemporaryDirectory() as folder:

        dataset = bigquery.get_dataset(fully_qualified_dataset)

        remote_connection = bigquery.get_or_create_remote_connection(project, dataset.location, REMOTE_CONNECTION_NAME)
        remote_connection_users = get_dataset_users(dataset)
        bigquery.set_remote_connection_users(remote_connection.name, remote_connection_users)

        create_folder_with_cloudrun_code(conf, folder)
        cloud_run_service = 'bf-' + bigfunction.replace("_", "-")
        cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(dataset.location, dataset.location)
        cloud_run = CloudRun(cloud_run_service, project, cloud_run_location)
        cloud_run_options = conf.get('cloud_run', {})
        cloud_run.deploy(folder, cloud_run_options)
        cloud_run.add_invoker_permission(f'serviceAccount:{remote_connection.cloud_resource.service_account_id}')

        conf['remote_endpoint'] = cloud_run.url
        conf['remote_connection'] = re.sub(
            r"projects/(\d+)/locations/([\w-]+)/connections/([\w-]+)",
            r"\g<1>.\g<2>.\g<3>",
            remote_connection.name,
        )


def deploy(fully_qualified_bigfunction, quotas):
    project, dataset, bigfunction = fully_qualified_bigfunction.replace('`', '').split('.')
    bigquery = BigQuery(project)
    fully_qualified_dataset = f'`{project}`.{dataset}'
    filename = f'bigfunctions/{bigfunction}.yaml'
    if not os.path.isfile(filename):
        handle_error(f'File {filename} does not exist. Cannot deploy {fully_qualified_bigfunction}')
    conf = open(filename, encoding='utf-8').read()
    conf = conf.replace('{BIGFUNCTIONS_DATASET}', fully_qualified_dataset)
    conf = yaml.safe_load(conf)
    conf['name'] = bigfunction
    conf['dataset'] = fully_qualified_dataset
    conf['filename'] = filename
    conf['quotas'] = {**quotas, **conf.get('quotas', {})}

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

    if 'npm_packages' in conf:
        conf['js_libraries_urls'] = [
            build_and_upload_npm_package(npm_package, 'bigfunctions_js_libs', project)
            for npm_package in conf['npm_packages']
        ]
    if conf['type'] == 'function_py':
        deploy_cloud_run(bigquery, bigfunction, conf, fully_qualified_dataset, project)

    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(**conf)
    print_info('Creating function in dataset')
    bigquery.query(query)
    print_success('successfully created ' + fully_qualified_bigfunction)


