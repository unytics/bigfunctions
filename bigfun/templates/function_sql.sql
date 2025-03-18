create or replace function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
{% if output.type != 'any type' %}returns {{ output.type }}{% endif %}
as (
    ({{ code | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) }})
)
options(
    description = '''{{ description }}'''
)
