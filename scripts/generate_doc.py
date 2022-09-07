import re
import os

import yaml
import jinja2

REGIONS_TO_DISPLAY = ['EU', 'US', 'europe-west1', 'your-region2']
HEADER_EXPLORE = '''
---

<img src="../../assets/logo_and_name.png" alt="drawing" width="300"/>


**"Explore" BigFunctions are great for data-analysts to explore data**.

They make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.

⚠️ *To see the data-vizualisation in BigQuery Console make sure you read [Getting Started](/docs/get_started/)!*

---

'''

HEADER_UTILS = '''
---

<img src="../../assets/logo_and_name.png" alt="drawing" width="300"/>


**"Utils" BigFunctions** used by other BigFunctions.

⚠️ *To see the data-vizualisation in BigQuery Console make sure you read [Getting Started](/docs/get_started/)!*

---

'''




def generate_doc(bigfunctions_filenames, output_header, output_filename):
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
            **conf,
        )
        documentation = re.sub(r'###\s*(.*)', r'<h3>\g<1></h3>', documentation)
        documentations.append(documentation)



    documentation = output_header + '\n\n\n'.join(documentations)

    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write(documentation)


generate_doc(sorted([f for f in os.listdir('bigfunctions') if f.startswith('explore_')]), HEADER_EXPLORE, 'site/content/docs/explore.md')
generate_doc(sorted([f for f in os.listdir('bigfunctions') if not f.startswith('explore_')]), HEADER_UTILS, 'site/content/docs/utils.md')
