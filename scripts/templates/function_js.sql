create or replace function {{ dataset.name }}.{{ name }}({% for argument in arguments %}{{ argument.name }} {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output_value.type }}
language js
as
'''
{{ code }}
'''
options(
    description = '''{{ documentation }}'''
)
