
content = open('scripts/bookmarklet.js', encoding='utf-8').read()
content = 'javascript:' + content.replace('\n', ' ')

with open('site/content/getting_started.md', 'a', encoding='utf-8') as f:
	f.write(f'\n<div><a href="{content}" class="md-button md-button--primary">BigFunctions</a><div>')