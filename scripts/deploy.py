import argparse

import requests
import google.cloud.bigquery
# import google.cloud.storage
import yaml
import jinja2


CONF = yaml.safe_load(open('conf.yaml', encoding='utf-8').read())
ENVIRONMENTS = [dataset['env'] for dataset in CONF['datasets']]
BQ = google.cloud.bigquery.Client()
# STORAGE = google.cloud.storage.Client()

# JS_LIBS_BUCKET = STORAGE.get_bucket(CONF['js_libs_bucket'])



parser = argparse.ArgumentParser(description='Deploy BigQuery asset among [dataset, table, bigfunction]')
parser.add_argument('environment', choices=ENVIRONMENTS)
parser.add_argument('asset_type', choices=['dataset', 'table', 'bigfunction'])
parser.add_argument('--name')
parser.add_argument('--region')
args = parser.parse_args()
assert args.asset_type == 'dataset' or args.name, 'a name argument must be given if asset_type != dataset. Run `python scripts/deploy_bigquery.py --help`'


for region in [args.region] if args.region else CONF['bigquery_regions']:
    CONF['region__lowercase_and_wo_hyphens'] = region.lower().replace('-', '_')

    dataset = {**[dataset for dataset in CONF['datasets'] if dataset['env'] == args.environment][0]}
    dataset['name'] = dataset['name'].format(**CONF)
    dataset['description'] = dataset['description'].format(**CONF)
    full_dataset_name = f"{CONF['project']}.{dataset['name']}"

    conf = {}
    template_file = f'scripts/templates/{args.asset_type}.sql'
    if args.asset_type == 'table':
        conf = CONF['tables'][args.name]
    elif args.asset_type == 'bigfunction':
        filename = f'bigfunctions/{args.name}.yaml'
        conf = yaml.safe_load(open(filename, encoding='utf-8').read().replace('{BIGFUNCTIONS_DATASET}', full_dataset_name))
        conf['name'] = args.name
        conf['filename'] = filename
        conf['description'] = conf['description'] + f'\n\nSee full documentation --> "{CONF["doc_base_url"]}#{args.name}"'
        if 'template' in conf:
            conf['code'] += f'''
                set output = to_json(struct(
                    output as json,
                    {full_dataset_name}.render_string(
                        """
                        {conf['template']}
                        """,
                        to_json_string(output)
                    ) as html
                ));
            '''
        template_file = f'scripts/templates/{conf["type"]}.sql'
        conf['libraries'] = [
            {
                'source_url': library,
                # 'filename': library.replace('https://', '').replace('http://', '').split('/', 1)[1],
                'cloudstorage_url': f"gs://{CONF['js_libs_bucket']}/{library}",
            }
            for library in conf.get('libraries', [])
        ]

    template = jinja2.Template(open(template_file, encoding='utf-8').read())
    query = template.render(
        environment=args.environment,
        region=region,
        dataset=dataset,
        **CONF,
        **conf,
    )

    # for library in conf['libraries']:
    #     js = requests.get(library['source_url']).content
    #     # destination_filename =
    #     blob = google.cloud.storage.Blob(library['filename'], JS_LIBS_BUCKET)
    #     blob.upload_from_string(js)

    print(query)
    BQ.query(query, location=region).result()
    print('successfully created', args.asset_type, 'for region', region, 'and environment', args.environment)



