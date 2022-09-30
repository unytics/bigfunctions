import os

import yaml
import jinja2

CONF = yaml.safe_load(open(f'mkdocs.yml', encoding='utf-8').read())
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
        datasets=CONF['bigfunctions_datasets'],
        repo_url=CONF['repo_url'],
        categories=categories,
    )
    with open('site/content/reference.md', 'w', encoding='utf-8') as out:
        out.write(documentation)


if __name__ == '__main__':
    generate_bigfunctions_category_page()
