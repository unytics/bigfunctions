import os
from functools import reduce

import yaml
import jinja2

CONF = yaml.safe_load(open(f'mkdocs.yml', encoding='utf-8').read())

THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
TEMPLATE_FOLDER = THIS_FOLDER + '/templates'


class BasePage:

    output_filename = None

    def generate(self):
        assert self.output_filename is not None, 'missing output filename attribute'
        context = self.get_context()
        template = f'{TEMPLATE_FOLDER}/doc/{self.output_filename}'
        content = jinja2.Template(open(template, encoding='utf-8').read()).render(**context)
        with open(f'site/content/{self.output_filename}', 'w', encoding='utf-8') as out:
            out.write(content)

    def get_context(self):
        raise NotImplementedError()


class ContentPage(BasePage):

    def __init__(self, content_filename, output_filename):
        self.output_filename = output_filename
        self.content_filename = content_filename

    def get_context(self):
        if os.path.isfile(self.content_filename):
            self.content = open(self.content_filename, encoding='utf-8').read()
            return {'content': self.content}
        return {'content': ''}


class ReferencePage(BasePage):

    output_filename = 'reference.md'

    def get_context(self):
        bigfunctions = []
        for filename in sorted(os.listdir('bigfunctions')):
            if not filename.endswith('.yaml'):
                continue
            conf = yaml.safe_load(open(f'bigfunctions/{filename}', encoding='utf-8').read())
            assert isinstance(conf, dict), f'Could not load yaml config of bigfunction `{filename}`'
            conf['name'] = filename.replace('.yaml', '')
            bigfunctions.append(conf)

        categories = CONF['bigfunctions_categories']
        for category in categories:
            category['bigfunctions'] = [bigfunction for bigfunction in bigfunctions if bigfunction['category'] == category['name']]
        return {
            'datasets': CONF['bigfunctions_datasets'],
            'repo_url': CONF['repo_url'],
            'categories': categories,
        }


def generate_doc():
    ContentPage('README.md', 'index.md').generate()
    ContentPage('CONTRIBUTING.md', 'contribute.md').generate()
    ReferencePage().generate()


if __name__ == '__main__':
    generate_doc()