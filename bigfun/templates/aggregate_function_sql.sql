create or replace aggregate function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
{% if output.type != 'any type' %}returns {{ output.type }}{% endif %}
as (
{{ code | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) | replace('{BIGFUNCTIONS_DATASET_REGION}', '`region-' +  dataset_location|lower + '`') }}
)
options(
    description = '''{{ description }}'''
)
