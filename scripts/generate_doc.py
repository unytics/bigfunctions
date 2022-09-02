import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
HEADER = '''
---

<img src="../../assets/logo_and_name.png" alt="drawing" width="300"/>


**"Explore" BigFunctions are great for data-analysts to explore data**.

The functions make computations on BigQuery and enable you to display results as data-vizualizations directly in BigQuery console.

---


'''
MULTI_TABS = '''
=== "{region}"

    {content}
'''

CONF = yaml.safe_load(open('conf.yaml', encoding='utf-8').read())


def generate_doc(bigfunctions_filenames, output_filename):
    documentations = []
    for filename in bigfunctions_filenames:
        if not filename.endswith('.yaml'):
            pass

        conf = {}
        name = filename.replace('.yaml', '')
        filename = f'bigfunctions/{filename}'
        conf = yaml.safe_load(open(filename, encoding='utf-8').read())
        if not conf or not isinstance(conf, dict):
            continue
        conf['name'] = name
        conf['filename'] = filename
        template = f'scripts/templates/{conf["type"]}.md'
        documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
            regions=REGIONS_TO_DISPLAY,
            **CONF,
            **conf,
        )
        documentation = re.sub(r'###\s*(.*)', r'<h3>\g<1></h3>', documentation)
        documentations.append(documentation)



    documentation = HEADER + '\n\n\n'.join(documentations)

    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write(documentation)


generate_doc(sorted([f for f in os.listdir('bigfunctions') if f.startswith('explore_')]), 'site/content/docs/explore.md')
