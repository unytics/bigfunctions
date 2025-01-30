import json
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

.blog-post-abstract img {
  margin: 2.5em 0px 0em;
}


</style>

<div class="blog-posts">

    <h1>Blog</h1>


    {% for post in posts %}
    <a class="blog-post-abstract" href="{{ post.url }}" target="_blank">

        <div>

            <h3>{{ post.title | truncate(120) }}</h3>

            <p>{{ post.text | truncate(120) }}...</p>

            <p class="footer">{{ post.date }} • {{ post.author }}</p>
        </div>

        <div>

            {% if post.images %}
                <img src="{{ post.images[0] }}">
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

# def clean_text(text):
#     text = text.translate(letters_mapping).strip()
#     lines = [line for line in lines if line]
#     return '\n'.join(lines)


posts = json.loads(open('2025-01-30_linkedin_posts.json', encoding='utf-8').read())
# post = next(post for post in posts if 'numImpressions' not in post)
# print(post)
posts = [
    {
        'type': post['type'],
        'title': post['text'].split('\n')[0].translate(letters_mapping).strip().replace('#', ''),
        'text': '\n'.join(post['text'].split('\n')[1:]).translate(letters_mapping).strip().replace('#', ''),
        'article_title': post.get('article', {}).get('title'),
        'article_url': post.get('article', {}).get('url'),
        'images': post.get('images', []),
        'author': post['authorName'],
        'date': post['postedAtISO'][:10],
        'url': post['url'],
        'likes': post['numLikes'],
        'reshares': post['numShares'],
        'impressions': post.get('numImpressions'),
        'comments': post['numComments'],
    }
    for post in posts
    if (
        'type' in post and
        'text' in post and
        post['postedAtISO'] > '2022-09'
    )
]

content = template.render(posts=posts)

open('blog.md', 'w', encoding='utf-8').write(content)

# import pandas as pd
# df = pd.DataFrame(posts)
# breakpoint()