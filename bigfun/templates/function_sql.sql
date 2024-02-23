create or replace function {{ fully_qualified_dataset }}.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
{% if output.type != 'any type' %}returns {{ output.type }}{% endif %}
as (
{{ code }}
)
options(
    description = '''{{ description }}'''
)
