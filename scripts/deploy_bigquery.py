import argparse

from google.cloud import bigquery
import yaml
import jinja2


CONF = yaml.safe_load(open('conf.yaml', encoding='utf-8').read())
BQ = bigquery.Client()


parser = argparse.ArgumentParser(description='Deploy BigQuery asset among [dataset, table, function_js]')
parser.add_argument('asset_type', choices=['dataset', 'table', 'function_js'])
parser.add_argument('--name')
args = parser.parse_args()
assert args.asset_type == 'dataset' or args.name, 'a name argument must be given if asset_type != dataset. Run `python scripts/deploy_bigquery.py --help`'


template = jinja2.Template(open(f'scripts/templates/{args.asset_type}.sql', encoding='utf-8').read())
for region in CONF['bigquery_regions']:
    for environment in CONF['environments']:
        conf = {}
        if args.asset_type == 'table':
            conf = CONF['tables'][args.name]
        elif args.asset_type in ['function_js']:
            conf = yaml.safe_load(open(f'bigfunctions/{args.name}.yaml', encoding='utf-8').read())
            conf['name'] = args.name

        query = template.render(
            region=region,
            environment=environment,
            dataset=CONF['environments'][environment]['dataset_prefix'] + region.lower().replace('-', '_'),
            **CONF,
            **conf,
        )
        BQ.query(query, location=region).result()
        print('successfully created', args.asset_type, 'for region', region, 'and environment', environment)



