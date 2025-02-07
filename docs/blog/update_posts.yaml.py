'''
Update posts.yaml file with linkedin posts exported with apify
'''
import json
import re

import jinja2

YAML_TEMPLATE = jinja2.Template('''
{% for post in posts %}
- id: {{ post.id }}
  type: {{ post.type }}
  title: |
    {{ post.title }}
  author: {{ post.author }}
  date: "{{ post.date }}"
  url: {{ post.url }}
  likes: {{ post.likes }}
  reshares: {{ post.reshares }}
  impressions: {{ post.impressions }}
  comments: {{ post.comments }}
  article_title: |
    {{ post.article_title }}
  article_url: {{ post.article_url }}
  images: {{ post.images }}
  image_url: {{ post.image_url }}
  text: |
    {{ post.text | indent(width=4) }}
{% endfor %}
''')


LINKEDIN_POSTS_FILENAME = '2025-01-30_linkedin_posts.json'


def clean_letters(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]
    bold_letters = ['𝐚', '𝐛', '𝐜', '𝐝', '𝐞', '𝐟', '𝐠', '𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', '𝐬', '𝐭', '𝐮', '𝐯', '𝐰', '𝐱', '𝐲', '𝐳', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '𝟎', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '❗', '❓', '.', ',', '"', "'"]
    # italic_letters = ['𝑎', '𝑏', '𝑐', '𝑑', '𝑒', '𝑓', '𝑔', 'ℎ', '𝑖', '𝑗', '𝑘', '𝑙', '𝑚', '𝑛', '𝑜', '𝑝', '𝑞', '𝑟', '𝑠', '𝑡', '𝑢', '𝑣', '𝑤', '𝑥', '𝑦', '𝑧', '𝐴', '𝐵', '𝐶', '𝐷', '𝐸', '𝐹', '𝐺', '𝐻', '𝐼', '𝐽', '𝐾', '𝐿', '𝑀', '𝑁', '𝑂', '𝑃', '𝑄', '𝑅', '𝑆', '𝑇', '𝑈', '𝑉', '𝑊', '𝑋', '𝑌', '𝑍', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]
    italic_letters = ['𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘮', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻', '𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]
    capitalized_letters = ['ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ꜰ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'q', 'ʀ', 'ꜱ', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '﹗', '﹖', '﹒', '﹐', '"', "'"]

    letters_mapping = str.maketrans({
        **{bold_letter: letter for letter, bold_letter in zip(letters, bold_letters)},
        **{italic_letter: letter for letter, italic_letter in zip(letters, italic_letters)},
        **{capitalized_letters: letter for letter, capitalized_letters in zip(letters, capitalized_letters)},
    })

    return text.translate(letters_mapping)


def format_post(post):
    date = post['postedAtISO'][:10]
    text = clean_letters(post['text']).strip().replace('#', '')
    title = text.split('\n')[0].strip()
    text = '\n'.join(text.split('\n')[1:]).strip()
    slug = re.sub('[^0-9a-z ]+', '', title.lower()).replace(' ', '_')[:50]
    id = date + '_' + slug
    image_url = '../assets/blog/' + id if 'images' in post else None
    return {
        'type': post['type'],
        'id': id,
        'title': title,
        'text': text,
        'article_title': post.get('article', {}).get('title') or 'null',
        'article_url': post.get('article', {}).get('url') or 'null',
        'images': post.get('images', []),
        'image_url': image_url or 'null',
        'author': post['authorName'],
        'date': date,
        'url': post['url'],
        'likes': post['numLikes'],
        'reshares': post['numShares'],
        'impressions': post.get('numImpressions') or 'null',
        'comments': post['numComments'],
    }


def str_presenter(dumper, data):
    """
    Preserve multiline strings when dumping yaml.
    https://github.com/yaml/pyyaml/issues/240
    """
    if "\n" in data:
        # Remove trailing spaces messing out the output.
        block = "\n".join([line.rstrip() for line in data.splitlines()])
        if data.endswith("\n"):
            block += "\n"
        return dumper.represent_scalar("tag:yaml.org,2002:str", block, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)

posts = json.loads(open(LINKEDIN_POSTS_FILENAME, encoding='utf-8').read())
posts = [
    format_post(post)
    for post in posts
    if (
        'type' in post and
        'text' in post and
        post['postedAtISO'] > '2022-09'
    )
]

content = YAML_TEMPLATE.render(posts=posts)
open('posts.yaml', 'w', encoding='utf-8').write(content)
