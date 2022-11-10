import re
import os
import shutil
import subprocess

import yaml
import jinja2

from .utils import bigquery, handle_error, print_success, print_info


PYTHON_BUILD_DIR = 'build_python'
TEMPLATE_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/templates'


def deploy(fully_qualified_bigfunction):
    project, dataset, bigfunction = fully_qualified_bigfunction.split('.')
    project =  "`" + project.replace("`", "") + "`"
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

        template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.py'
        template = jinja2.Template(open(template_file, encoding='utf-8').read())
        python_code = template.render(**conf)
        with open(f'{PYTHON_BUILD_DIR}/main.py', 'w', encoding='utf-8') as out:
            out.write(python_code)

        with open(f'{PYTHON_BUILD_DIR}/requirements.txt', 'w', encoding='utf-8') as out:
            out.write('gunicorn\nflask\ngoogle-cloud-error-reporting\n' + conf['requirements'])

        shutil.copy(f'{TEMPLATE_FOLDER}/Dockerfile', PYTHON_BUILD_DIR)

        cloud_run_service = 'bf-' + bigfunction.replace("_", "-")
        print_info('Cloud Run Service to deploy: ' + cloud_run_service)

        print_info('getting dataset location')
        dataset_location = bigquery.get_dataset(fully_qualified_dataset).location
        cloud_run_location = {'EU': 'europe-west1', 'US': 'us-west1'}.get(dataset_location, dataset_location)

        deploy_command = f'gcloud run deploy {cloud_run_service} --quiet --source {PYTHON_BUILD_DIR} --region {cloud_run_location} --project {project} --no-allow-unauthenticated'
        print_info(f'deploying cloud run {bigfunction} with command `{deploy_command}`')
        os.system(deploy_command)

        get_cloud_run_url_command = f'gcloud run services describe {cloud_run_service} --platform managed --region {cloud_run_location} --format "value(status.url)"'
        print_info('getting cloud run URL with command ' + get_cloud_run_url_command)
        cloud_run_url = subprocess.check_output(get_cloud_run_url_command, shell=True).decode().strip()
        print_info('Cloud Run URL: ' + cloud_run_url)

        print_info('getting remote connection')
        remote_connection = bigquery.get_or_create_bigfunctions_remote_connection(project, dataset_location)
        remote_connection_name = re.sub(
            r"projects/(\d+)/locations/([\w-]+)/connections/([\w-]+)",
            r"\g<1>.\g<2>.\g<3>",
            remote_connection.name,
        )
        print_info('Remote connection name: ' + remote_connection_name)

        # bigquery.share_bigfunctions_remote_connection(remote_connection.name)


        add_invoker_role_command = f'gcloud run services add-iam-policy-binding {cloud_run_service} --region {cloud_run_location} --member=serviceAccount:{remote_connection.cloud_resource.service_account_id} --role=roles/run.invoker'
        print_info(f'giving invoker permission to connection service account with command `{add_invoker_role_command}`')
        os.system(add_invoker_role_command)

        conf['remote_connection'] = remote_connection_name
        conf['remote_endpoint'] = cloud_run_url

    template_file = f'{TEMPLATE_FOLDER}/{conf["type"]}.sql'
    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        dataset=fully_qualified_dataset,
        name=bigfunction,
        filename=filename,
        **conf,
    )
    bigquery.query(query)
    print_success('successfully created ' + fully_qualified_bigfunction)


