
content = open('bookmarklet.js', encoding='utf-8').read()
content = 'javascript:' + content.replace('\n', ' ')
print(content)