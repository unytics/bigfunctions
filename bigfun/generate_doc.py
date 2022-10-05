import os

import yaml
import jinja2

CONF = yaml.safe_load(open(f'mkdocs.yml', encoding='utf-8').read())

THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
TEMPLATE_FOLDER = THIS_FOLDER + '/templates'


class Page:
    name = ''

    def generate(self):
        context = self.get_context()
        template = f'{TEMPLATE_FOLDER}/doc_{self.name}.md'
        content = jinja2.Template(open(template, encoding='utf-8').read()).render(**context)
        with open(f'site/content/{self.name}.md', 'w', encoding='utf-8') as out:
            out.write(content)

    def get_context(self):
        raise NotImplementedError()


class GettingStartedPage(Page):
    name = 'getting_started'

    def get_context(self):
        bookmarklet = open(f'{THIS_FOLDER}/bookmarklet.js', encoding='utf-8').read()
        bookmarklet = 'javascript:' + bookmarklet.replace('\n', ' ')
        return {'bookmarklet': bookmarklet}


class ReferencePage(Page):
    name = 'reference'

    def get_context(self):
        bigfunctions = [
            {
                **yaml.safe_load(open(f'bigfunctions/{f}', encoding='utf-8').read()),
                **{'name': f.replace('.yaml', '')},
            }
            for f in os.listdir('bigfunctions')
        ]
        categories = CONF['bigfunctions_categories']
        for category in categories:
            category['bigfunctions'] = [bigfunction for bigfunction in bigfunctions if bigfunction['category'] == category['name']]
        return {
            'datasets': CONF['bigfunctions_datasets'],
            'repo_url': CONF['repo_url'],
            'categories': categories,
        }


def generate_doc():
    GettingStartedPage().generate()
    ReferencePage().generate()
