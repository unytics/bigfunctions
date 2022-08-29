create or replace function {{ dataset.name }}.{{ name }}({% for argument in arguments %}{{ argument.name }} {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output.type }}
language js
as
'''
{{ code }}
'''
options(
    description = '''{{ documentation }}'''
    {% if libraries %}
    , library = [
        {% for library in libraries %}"{{ library.cloudstorage_url }}"{% if not loop.last %}, {% endif %}{% endfor %}
    ]
    {% endif %}
)
