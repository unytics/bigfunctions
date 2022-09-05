create table if not exists {{ dataset.name }}.{{ name }}(
  {% for column in schema -%}
  {{ column.name }} {{ column.type }} {% if column.default %}default {{column.default}}{% endif %} options (description = "{{ column.description }}"){% if not loop.last %}, {% endif %}
  {% endfor %}
)
{% if partition_column %}partition by date({{ partition_column }}){% endif %}
options (description = "{{ description }}");


{% for permission in permissions %}
grant `{{ permission.permission }}`
ON TABLE {{ dataset.name }}.{{ name }}
TO '{{ permission.who }}';
{% endfor %}
