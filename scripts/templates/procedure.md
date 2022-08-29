{{ description }}
```
{% for sample in samples -%}
{{ sample }}
{% endfor -%}
```
> **Returns** ➜ {% for output in outputs %}`{{ output.name }} {{ output.type}}`{% if not loop.last %}, {% endif %}{% endfor %}

### Example

{{ example }}

<a href="{{ repo }}/blob/main/{{ filename }}" target="_blank">Source Code</a>