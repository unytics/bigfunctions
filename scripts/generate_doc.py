import os

import yaml
import jinja2

CONF = yaml.safe_load(open(f'mkdocs.yml', encoding='utf-8').read())

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
REPO = 'https://github.com/unytics/bigfunctions'
BIGFUNCTIONS = [
    {
        **yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read()),
        **{'name': f.replace('.yaml', '')},
    }
    for f in os.listdir('bigfunctions')
]


def generate_bigfunctions_category_page():
    template = f'scripts/templates/doc_reference.md'
    categories = CONF['bigfunctions_categories']
    for category in categories:
        category['bigfunctions'] = [bigfunction for bigfunction in BIGFUNCTIONS if bigfunction['category'] == category['name']]
    documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
        regions=REGIONS_TO_DISPLAY,
        repo=REPO,
        categories=categories,
    )
    with open('site/content/reference.md', 'w', encoding='utf-8') as out:
        out.write(documentation)


if __name__ == '__main__':
    generate_bigfunctions_category_page()
