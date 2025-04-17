create or replace function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output.type }}
language js
as
r'''
{{ code | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) | replace('{BIGFUNCTIONS_DATASET_REGION}', '`region-' +  dataset_location|lower + '`') }}
'''
options(
    description = '''{{ description }}'''
    {% if js_libraries_urls %}
    , library = [
        {% for url in js_libraries_urls %}"{{ url }}"{% if not loop.last %}, {% endif %}{% endfor %}
    ]
    {% endif %}
)
