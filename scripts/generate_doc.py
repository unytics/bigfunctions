import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
REPO = 'https://github.com/unytics/bigfunctions'
BIGFUNCTIONS = {
    f.replace('.yaml', ''): yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read())
    for f in os.listdir('bigfunctions')
}



INDEX_PAGE_TEMPLATE= jinja2.Template('''---
hide:
  - navigation
---

## 📄 Overview

!!! note ""

    BigFunctions are public BigQuery routines that give you **super-SQL-powers** in BigQuery 💪.


    {% for category, category_conf in categories.items() %}

    **{{ category_conf.emoticon }} {{ category | replace('_', ' ') | capitalize }}**

    {% for name, conf in category_conf.bigfunctions.items() -%}
    {% set bigfunction_description_lines = conf.description.split('\n') %}
    - [<code>{{ name }}({% for argument in conf.arguments %}{{ argument.name | replace('{{region}}', region) }}{% if not loop.last %}, {% endif %}{% endfor %})</code>](#{{ name }}): {{ bigfunction_description_lines[0] }}
    {% endfor %}

    {% endfor %}

    **🔴 Before using see --> [Getting Started](/bigfunctions/getting_started/)**


''')



CATEGORY_PAGE_HEADER_TEMPLATE = jinja2.Template('''
<div style="margin-top: 6rem;"></div>


## {{ category_emoticon }} {{ category | replace('_', ' ') | capitalize }}

!!! note ""
    **{{ category_title }} **

    {{ category_subtitle }}

''')


CATEGORIES = {
    'explore': {
        'emoticon': '👀',
        'title': 'Explore data within BigQuery console',
        'subtitle': 'Make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'explore'},
    },
    'transform_string': {
        'emoticon': '✨',
        'title': 'Transform data creatively',
        'subtitle': 'Be amazed with your new SQL powers.',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'transform_string'},
    },
    'transform_date': {
        'emoticon': '📆',
        'title': 'Transform data creatively',
        'subtitle': 'Be amazed with your new SQL powers.',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'transform_date'},
    },
    'notify': {
        'emoticon': '💬',
        'title': 'Send infos to your customers, alert the operations teams, send reportings to business',
        'subtitle': 'Spread the word to the world!',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'notify'},
    },
    'export': {
        'emoticon': '🚀',
        'title': 'Get the data out to the outside world',
        'subtitle': 'Make BigQuery as the golden source of all your SAAS and for all your usages',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'export'},
    },
    'utils': {
        'emoticon': '🔨',
        'title': '"Utils" BigFunctions',
        'subtitle': '',
        'bigfunctions': {
            name: conf
            for name, conf in BIGFUNCTIONS.items() if conf['category'] == 'utils'},
    },
}


def generate_bigfunctions_index_page():
    output_filename = f'site/content/reference.md'
    content = INDEX_PAGE_TEMPLATE.render(categories=CATEGORIES)
    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write(content)


def generate_bigfunctions_category_page(category, category_emoticon, category_title, category_subtitle, bigfunctions):
    documentations = []
    for name, conf in bigfunctions.items():
        if not conf or not isinstance(conf, dict):
            continue
        conf['name'] = name
        template = f'scripts/templates/doc_reference.md'
        documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
            regions=REGIONS_TO_DISPLAY,
            repo=REPO,
            **conf,
        )
        documentations.append(documentation)


    header = CATEGORY_PAGE_HEADER_TEMPLATE.render(category=category, category_emoticon=category_emoticon, category_title=category_title, category_subtitle=category_subtitle)
    with open('site/content/reference.md', 'a', encoding='utf-8') as out:
        out.write(header)
        out.write('\n\n\n'.join(documentations))


if __name__ == '__main__':
    generate_bigfunctions_index_page()
    for category, category_conf in CATEGORIES.items():
        generate_bigfunctions_category_page(category, category_conf['emoticon'], category_conf['title'], category_conf['subtitle'], category_conf['bigfunctions'])
