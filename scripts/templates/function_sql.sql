create or replace function {{ dataset }}.{{ name }}({% for argument in arguments %}{{ argument.name }} {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output.type }}
as (
{{ code }}
)
options(
    description = '''{{ description }}'''
)
