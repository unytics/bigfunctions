import yaml
import jinja2

template = jinja2.Template(open('index.md.template', encoding='utf-8').read())

posts = yaml.safe_load(open('posts.yaml', encoding='utf-8').read())

content = template.render(posts=posts)

open('index.md', 'w', encoding='utf-8').write(content)