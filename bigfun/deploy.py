import tempfile
import re
import os
import shutil
import json

import yaml
import jinja2

from .utils import BigQuery, CloudRun, handle_error, print_success, print_info, build_and_upload_npm_package


REMOTE_CONNECTION_NAME = 'remote-bigfunctions'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'


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


def deploy_cloud_run(bigquery, bigfunction_name, conf, project, dataset):
    with tempfile.TemporaryDirectory() as folder:
        remote_connection = bigquery.get_or_create_remote_connection(project, dataset.location, REMOTE_CONNECTION_NAME)
        bigquery.set_remote_connection_users(remote_connection.name, dataset.users)

        create_folder_with_cloudrun_code(conf, folder)
        cloud_run_service = 'bf-' + bigfunction_name.replace("_", "-")
        cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(dataset.location, dataset.location)
        cloud_run = CloudRun(cloud_run_service, project, cloud_run_location)
        cloud_run.deploy(folder, conf.get('cloud_run', {}))
        cloud_run.add_invoker_permission(f'serviceAccount:{remote_connection.cloud_resource.service_account_id}')

        conf['remote_endpoint'] = cloud_run.url
        conf['remote_connection'] = re.sub(
            r"projects/(\d+)/locations/([\w-]+)/connections/([\w-]+)",
            r"\g<1>.\g<2>.\g<3>",
            remote_connection.name,
        )


def deploy(bigfunction, project, dataset_name):
    fully_qualified_dataset = f'`{project}`.`{dataset_name}`'
    conf = json.loads(json.dumps(bigfunction.config).replace('{BIGFUNCTIONS_DATASET}', fully_qualified_dataset))
    conf['fully_qualified_dataset'] = fully_qualified_dataset
    bigquery = BigQuery(project)
    dataset = bigquery.get_dataset(fully_qualified_dataset)

    if 'npm_packages' in conf:
        if 'bucket_js_dependencies' not in conf:
            handle_error('Please provide the name of the cloud storage bucket to host js dependencies. The bucket name must be set in config as a variable named: `bucket_js_dependencies`. You must have objectAdmin permissions on it to create or replace files. The users of your function must have read access')
        conf['js_libraries_urls'] = [
            build_and_upload_npm_package(npm_package, conf['bucket_js_dependencies'], project)
            for npm_package in conf['npm_packages']
        ]
    if conf['type'] == 'function_py':
        deploy_cloud_run(bigquery, bigfunction.name, conf, project, dataset)

    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(**conf)
    print_info('Creating function in dataset')
    bigquery.query(query)
    print_success(f'successfully created {fully_qualified_dataset}.{bigfunction.name}')


