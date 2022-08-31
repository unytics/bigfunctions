import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
HEADER = '''---
hide:
  - navigation
---

#
<img src="../assets/logo_and_name.png" alt="drawing" width="300"/>

BigFunctions are public BigQuery routines that give you new *SQL powers* in BigQuery 💪.

We are introducing today the first two functions. [Tell us what you think](https://github.com/unytics/bigfunctions/discussions)! 😊.

---


'''
MULTI_TABS = '''
=== "{region}"

    {content}
'''

CONF = yaml.safe_load(open('conf.yaml', encoding='utf-8').read())


documentations = []
for filename in sorted(os.listdir('bigfunctions')):
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
    conf['description'] = '> ' + conf['description'].replace('\n', '\n> ')
    # example = conf['example'].replace('\n', '\n    ')
    example = conf['example']
    example_codes = re.findall(r'```[^`]*```', example, re.DOTALL)
    for example_code in example_codes:
        new_example_code = example_code.replace('\n', '\n    ')
        new_example_code = ''.join([
            MULTI_TABS.format(
                region=region,
                content=new_example_code.replace('{BIGFUNCTIONS_DATASET}', f'bigfunctions.{region.lower().replace("-", "_")}'),
            )
            for region in REGIONS_TO_DISPLAY
        ])
        example = example.replace(example_code, new_example_code)

    conf['example'] = example

    template = f'scripts/templates/{conf["type"]}.md'
    documentation = jinja2.Template(open(template, encoding='utf-8').read()).render(
        **CONF,
        **conf,
    )
    documentation = re.sub(r'###\s*(.*)', r'<h3>\g<1></h3>', documentation)
    documentation = f'## {name}\n\n{documentation}\n\n---\n\n'
    documentations.append(documentation)



documentation = HEADER + '\n\n\n'.join(documentations)

with open('site/content/docs/index.md', 'w', encoding='utf-8') as out:
    out.write(documentation)