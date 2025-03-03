create or replace function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type | replace('yaml', 'string') }}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output.type }}
remote with connection `{{ remote_connection }}`
options (
    endpoint = '{{ remote_endpoint }}',
    user_defined_context = [("dataset_location", "{{ dataset_location }}")]
    {% if max_batching_rows %}, max_batching_rows = {{ max_batching_rows }}{% endif %}
);
