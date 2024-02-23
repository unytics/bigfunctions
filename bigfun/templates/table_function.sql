create or replace table function {{ fully_qualified_dataset }}.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ description }}'''
)
as (
{{ code }}
)
