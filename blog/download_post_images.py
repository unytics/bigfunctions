import urllib.request

import yaml


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

posts = yaml.safe_load(open('posts.yaml', encoding='utf-8').read())
download_images(posts)
