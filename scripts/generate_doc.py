import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
REPO = 'https://github.com/unytics/bigfunctions'
BIGFUNCTIONS = [
    {
        **yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read()),
        **{'name': f.replace('.yaml', '')},
    }
    for f in os.listdir('bigfunctions')
]


CATEGORIES = [
    {
        'name': 'explore',
        'emoticon': '👀',
        'title': 'Explore data within BigQuery console',
        'subtitle': 'Make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.',
    },
    {
        'name': 'transform_string',
        'emoticon': '✨',
        'title': 'Transform data creatively',
        'subtitle': 'Be amazed with your new SQL powers.',
    },
    {
        'name': 'transform_date',
        'emoticon': '📆',
        'title': 'Transform data creatively',
        'subtitle': 'Be amazed with your new SQL powers.',
    },
    {
        'name': 'notify',
        'emoticon': '💬',
        'title': 'Send infos to your customers, alert the operations teams, send reportings to business',
        'subtitle': 'Spread the word to the world!',
    },
    {
        'name': 'export',
        'emoticon': '🚀',
        'title': 'Get the data out to the outside world',
        'subtitle': 'Make BigQuery as the golden source of all your SAAS and for all your usages',
    },
    {
        'name': 'utils',
        'emoticon': '🔨',
        'title': '"Utils" BigFunctions',
        'subtitle': '',
    },
]

for category in CATEGORIES:
    category['bigfunctions'] = [bigfunction for bigfunction in BIGFUNCTIONS if bigfunction['category'] == category['name']]


def generate_bigfunctions_category_page():
    template = f'scripts/templates/doc_reference.md'
    documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
        regions=REGIONS_TO_DISPLAY,
        repo=REPO,
        categories=CATEGORIES,
    )
    with open('site/content/reference.md', 'w', encoding='utf-8') as out:
        out.write(documentation)


if __name__ == '__main__':
    generate_bigfunctions_category_page()
