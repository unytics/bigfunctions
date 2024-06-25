create or replace function `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output.type }}
remote with connection `{{ remote_connection }}`
options (
    endpoint = '{{ remote_endpoint }}'
    {% if max_batching_rows %}, max_batching_rows = {{ max_batching_rows }}{% endif %}
);
