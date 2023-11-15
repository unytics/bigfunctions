import os

import yaml
import jinja2

THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
TEMPLATE_FOLDER = THIS_FOLDER + '/templates'
TEMPLATE_MKDOCS_YAML = TEMPLATE_FOLDER + '/mkdocs.yml'
DOCUMENTATION_CONFIG_FILENAME = 'config_documentation.yaml'
BIGFUNCTIONS_FOLDER = 'bigfunctions'


def create_mkdocs_yaml_if_not_exist():
    mkdocs_yaml = open(TEMPLATE_MKDOCS_YAML, encoding='utf-8').read()


def get_bigfunctions():
    bigfunctions = {}
    for filename in sorted(os.listdir(BIGFUNCTIONS_FOLDER)):
        if not filename.endswith('.yaml'):
            continue
        conf = yaml.safe_load(open(f'bigfunctions/{filename}', encoding='utf-8').read())
        assert isinstance(conf, dict), f'Could not load yaml config of bigfunction `{filename}`'
        name = filename.replace('.yaml', '')
        conf['name'] = name
        bigfunctions[name] = conf
    return bigfunctions


# def get_documentation_config():
#     if not os.path.isfile(DOCUMENTATION_CONFIG_FILENAME):
#         print(f'WARNING: Could not find file `{DOCUMENTATION_CONFIG_FILENAME}` in current directory.')
#         print('WARNING: We generate `{DOCUMENTATION_CONFIG_FILENAME}` in current directory')
#         print('Edit it to change how the documentation is generated')
#         default_config = {
#             ''
#         }


BIGFUNCTIONS = get_bigfunctions()
# DOC_CONFIG = get_documentation_config()


CONF = yaml.safe_load(open(f'site/mkdocs.yml', encoding='utf-8').read())



class BasePage:


    def generate(self):
        context = self.get_context()
        template = f'{TEMPLATE_FOLDER}/{self.template_filename}'
        content = jinja2.Template(open(template, encoding='utf-8').read()).render(**context)
        with open(f'bigfunctions/README.md', 'w', encoding='utf-8') as out:
            out.write(content)

    def get_context(self):
        raise NotImplementedError()


class ReferencePage(BasePage):

    template_filename = 'bigfunctions.md'

    def get_context(self):
        categories = CONF['bigfunctions_categories']
        for category in categories:
            category['bigfunctions'] = [bigfunction for bigfunction in BIGFUNCTIONS.values() if bigfunction['category'] == category['name']]
        return {
            'datasets': CONF['bigfunctions_datasets'],
            'repo_url': CONF['repo_url'],
            'categories': categories,
        }


def generate_doc():
    ReferencePage().generate()


if __name__ == '__main__':
    generate_doc()