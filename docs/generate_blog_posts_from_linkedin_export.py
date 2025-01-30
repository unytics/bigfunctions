import json
import os
import re
import shutil
import time
import urllib.request

import jinja2

template = jinja2.Template('''---
title: "BigFunctions - Blog"
description: "Blog Posts related to BigFunctions"
hide:
  - navigation
  - toc
search:
  exclude: true
---

<style>

.blog-posts {
    max-width: 800px;
    margin: auto;
}

.blog-post-abstract {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 20%;
    grid-column-gap: 5%;
}

.blog-post-abstract p {
  color: rgb(38, 38, 38);
}

.blog-post-abstract p.footer, .blog-post-abstract:hover p {
  color: rgb(92, 92, 92);
}

.blog-post-abstract img, .lg\:two-columns img {
  margin: 2.5em 0px 0em;
}


</style>

<div class="blog-posts">

    <h1>Blog</h1>

    <hr>


    <a class="blog-post-abstract" href="https://timodechau.com/from-sql-to-slack-automating-data-workflows-with-big-functions/" target="_blank">

        <div>

            <h3 style="font-size: 2em;">From SQL to Slack: Automating Data Workflows with BigFunctions</h3>

            <img src="../assets/blog/timo_dechau_blog.png" style="margin: 0; max-width: 400px">

            <p>BigFunctions bridges the gap between data analysis and action by enabling analysts to trigger actions.</p>

            <p class="footer">2025-01-23 • Timo Dechau</p>
        </div>

        <div>

        </div>

    </a>
    <hr>


    {% for post in posts %}
    <a class="blog-post-abstract" href="{{ post.url }}" target="_blank">

        <div>

            <h3>{{ post.title | truncate(120) }}</h3>

            <p>{{ post.text | truncate(120) }}...</p>

            <p class="footer">{{ post.date }} • {{ post.author }}</p>
        </div>

        <div>

            {% if post.image_url %}
                <img src="{{ post.image_url }}">
            {% endif %}

        </div>

    </a>
    <hr>

    {% endfor %}

</div>
''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]
bold_letters = ['𝐚', '𝐛', '𝐜', '𝐝', '𝐞', '𝐟', '𝐠', '𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', '𝐬', '𝐭', '𝐮', '𝐯', '𝐰', '𝐱', '𝐲', '𝐳', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '𝟎', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '❗', '❓', '.', ',', '"', "'"]
# italic_letters = ['𝑎', '𝑏', '𝑐', '𝑑', '𝑒', '𝑓', '𝑔', 'ℎ', '𝑖', '𝑗', '𝑘', '𝑙', '𝑚', '𝑛', '𝑜', '𝑝', '𝑞', '𝑟', '𝑠', '𝑡', '𝑢', '𝑣', '𝑤', '𝑥', '𝑦', '𝑧', '𝐴', '𝐵', '𝐶', '𝐷', '𝐸', '𝐹', '𝐺', '𝐻', '𝐼', '𝐽', '𝐾', '𝐿', '𝑀', '𝑁', '𝑂', '𝑃', '𝑄', '𝑅', '𝑆', '𝑇', '𝑈', '𝑉', '𝑊', '𝑋', '𝑌', '𝑍', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]
italic_letters = ['𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘮', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻', '𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '.', ',', '"', "'"]

letters_mapping = str.maketrans({
    **{bold_letter: letter for letter, bold_letter in zip(letters, bold_letters)},
    **{italic_letter: letter for letter, italic_letter in zip(letters, italic_letters)}
})

def format_post(post):
    date = post['postedAtISO'][:10]
    text = post['text'].translate(letters_mapping).strip().replace('#', '')
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
        'article_title': post.get('article', {}).get('title'),
        'article_url': post.get('article', {}).get('url'),
        'images': post.get('images', []),
        'image_url': image_url,
        'author': post['authorName'],
        'date': date,
        'url': post['url'],
        'likes': post['numLikes'],
        'reshares': post['numShares'],
        'impressions': post.get('numImpressions'),
        'comments': post['numComments'],
    }

def download_images(posts):
    os.makedirs('assets/blog', exist_ok=True)
    existing_images = os.listdir('assets/blog')
    for post in posts:
        if not post['images']:
            continue
        url = post['images'][0]
        destination_filename = 'assets/blog/' + post['id']
        if post['id'] in existing_images:
            continue
        print(destination_filename)
        urllib.request.urlretrieve(url, destination_filename)
        time.sleep(2)

posts = json.loads(open('2025-01-30_linkedin_posts.json', encoding='utf-8').read())
# post = next(post for post in posts if 'numImpressions' not in post)
# print(post)
posts = [
    format_post(post)
    for post in posts
    if (
        'type' in post and
        'text' in post and
        post['postedAtISO'] > '2022-09'
    )
]

content = template.render(posts=posts)
open('blog.md', 'w', encoding='utf-8').write(content)


download_images(posts)

# import pandas as pd
# df = pd.DataFrame(posts)
# breakpoint()
