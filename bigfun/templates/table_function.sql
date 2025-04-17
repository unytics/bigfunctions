create or replace table function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ description }}'''
)
as (
{{ code | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) | replace('{BIGFUNCTIONS_DATASET_REGION}', '`region-' +  dataset_location|lower + '`') }}
)
