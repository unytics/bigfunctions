import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']


INDEX_PAGE_TEMPLATE= jinja2.Template('''---
hide:
  - navigation
---

!!! note ""

    BigFunctions are public BigQuery routines that give you **super-SQL-powers** in BigQuery 💪.


    {% for category, category_conf in categories.items() %}

    **{{ category_conf.emoticon }} {{ category|title }}**

    {{ category_conf.description|replace('\n', '')|replace('*', '') }}

    {% for name, conf in category_conf.bigfunctions.items() -%}
    - [<code>{{ conf.usage }}</code>](#{{ name }}): {{ conf.description }}
    {% endfor %}

    {% endfor %}

    **🔴 Before using see --> [Getting Started](/bigfunctions/getting_started/)**


''')



CATEGORY_PAGE_HEADER_TEMPLATE = jinja2.Template('''

---

## {{ category_emoticon }} {{ category|title }}

!!! note ""

    {{ category_description|replace('\n', '\n    ') }}

''')


CATEGORIES = {
    'explore': {
        'emoticon': '👀',
        'description': (
            '**"Explore" BigFunctions are great for data-analysts to explore data**.\n\n'
            'They make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.'
        ),
        'bigfunctions': {
            f.replace('.yaml', ''): yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read())
            for f in sorted([f for f in os.listdir('bigfunctions') if f.startswith('explore_')])
        },
    },
    'utils': {
        'emoticon': '🔨',
        'description': '**"Utils" BigFunctions** are tools used by other BigFunctions.',
        'bigfunctions': {
            f.replace('.yaml', ''): yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read())
            for f in sorted([f for f in os.listdir('bigfunctions') if not f.startswith('explore_')])
        },
    },
}


def generate_bigfunctions_index_page():
    output_filename = f'site/content/reference/index.md'
    content = INDEX_PAGE_TEMPLATE.render(categories=CATEGORIES)
    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write(content)


def generate_bigfunctions_category_page(category, category_emoticon, category_description, bigfunctions):
    output_filename = f'site/content/reference/{category}.md'
    documentations = []
    for name, conf in bigfunctions.items():
        if not conf or not isinstance(conf, dict):
            continue
        conf['name'] = name
        template = f'scripts/templates/{conf["type"]}.md'
        documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
            regions=REGIONS_TO_DISPLAY,
            **conf,
        )
        # documentation = re.sub(r'###\s*(.*)', r'<h3>\g<1></h3>', documentation)
        documentations.append(documentation)


    header = CATEGORY_PAGE_HEADER_TEMPLATE.render(category=category, category_emoticon=category_emoticon, category_description=category_description)
    with open('site/content/reference/index.md', 'a', encoding='utf-8') as out:
        out.write(header)
        out.write('\n\n\n'.join(documentations))


if __name__ == '__main__':
    generate_bigfunctions_index_page()
    for category, category_conf in CATEGORIES.items():
        generate_bigfunctions_category_page(category, category_conf['emoticon'], category_conf['description'], category_conf['bigfunctions'])
