BEGIN

  create or replace table {{ dataset }}.{{ name }}(
    {% for column in schema -%}
    {{ column.name }} {{ column.type }} {% if column.default %}default {{column.default}}{% endif %} options (description = "{{ column.description }}"){% if not loop.last %}, {% endif %}
    {% endfor %}
  )
  {% if partition_column %}partition by date({{ partition_column }}){% endif %}
  options (description = "{{ description }}")
  as
  select
    {% for column in schema -%}
      {{ column.name }},
    {% endfor %}
  from {{ dataset }}.{{ name }};


EXCEPTION WHEN ERROR THEN

  create table {{ dataset }}.{{ name }}(
    {% for column in schema -%}
    {{ column.name }} {{ column.type }} {% if column.default %}default {{column.default}}{% endif %} options (description = "{{ column.description }}"){% if not loop.last %}, {% endif %}
    {% endfor %}
  )
  {% if partition_column %}partition by date({{ partition_column }}){% endif %}
  options (description = "{{ description }}");

END


