import os
import subprocess
import shutil
from functools import reduce

import requests
import yaml
import jinja2

CONF = yaml.safe_load(open(f'mkdocs.yml', encoding='utf-8').read())

THIS_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
TEMPLATE_FOLDER = THIS_FOLDER + '/templates'
CONTRIBUTORS_AVATARS_FOLDER = 'site/content/assets/contributors'
AVATAR_COLORS = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#16a085', '#27ae60', '#2980b9', '#8e44ad', '#2c3e50', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1', '#95a5a6', '#f39c12', '#d35400', '#c0392b', '#bdc3c7', '#7f8c8d']


def get_author_avatar(bigfunction):
    author = subprocess.check_output(f"git log --diff-filter=A --pretty=format:%an -- bigfunctions/{bigfunction}.yaml", shell=True).decode()
    avatar_url = ''
    if 'marcombes' and 'paul' in author.lower():
        author = 'unytics'
    response = requests.get(f'https://github.com/{author}.png?size=32', stream=True)
    if not response.ok:
        author_id = (reduce(lambda x,y:x+y, map(ord, author.lower().strip().split('\n')[0])) + 1)% 20
        bcolor = AVATAR_COLORS[author_id][1:]
        response = requests.get(f'https://ui-avatars.com/api/?size=64&rounded=true&format=png&name={author}&background={bcolor}&color=fff', stream=True)
        assert response.ok, 'could not download avatar'
    with open(f'{CONTRIBUTORS_AVATARS_FOLDER}/{bigfunction}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    print(bigfunction, author)



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


class ReferencePage(Page):
    name = 'reference'

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
    ReferencePage().generate()


if __name__ == '__main__':
    generate_doc()