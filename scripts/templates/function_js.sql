create or replace function {{ dataset }}.{{ name }}({% for argument in arguments %}{{ argument.name }} {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
returns {{ output_value.type }}
language js
as
'''
{{ code }}
'''
options(
	description = '''{{ description }}
(region={{ region }}, environment={{ environment }})


Test:
```
{% for argument in arguments -%}
declare {{ argument.name }} {{ argument.type}} default {% if argument.type == "STRING" %}'{% endif %}{{ argument.example }}{% if argument.type == "STRING" %}'{% endif %};
{% endfor -%}
select {{ dataset }}.{{ name }}({% for argument in arguments %}{{ argument.name }}{% if not loop.last %}, {% endif %}{% endfor %});
```

This example will return `{`

'''
)
