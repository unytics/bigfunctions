---
template: main.html
title: "BigFunctions"
ogtitle: "BigFunctions supercharge BigQuery"
description: "BigFunctions are open-source BigQuery routines that give you SQL-superpowers. BigFunctions can show data-visualizations inside BigQuery console, compute advanced transforms such as sentiment score of a text, or send data to any of your favorite SAAS tool. BigFunctions is dbt's best friend."
image: "https://unytics.io/bigfunctions/assets/logo_and_name.png"
image_alt: "Supercharge BigQuery with BigFunctions"
image_width: "2500"
image_height: "541"
hide:
  - navigation
---

## 📄 Overview

BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.

!!! note ""



    {% for category in categories %}

    **{{ category.emoticon }} {% if category.name = 'AI' %}AI{% else %}{{ category.name | replace('_', ' ') | capitalize }}{% endif %}**

    {% for bigfunction in category.bigfunctions -%}
    {% set bigfunction_description_lines = bigfunction.description.split('\n') %}
    - [<code>{{ bigfunction.name }}({% for argument in bigfunction.arguments %}{{ argument.name }}{% if not loop.last %}, {% endif %}{% endfor %})</code>](#{{ bigfunction.name }}): {{ bigfunction_description_lines[0] }}
    {% endfor %}

    {% endfor %}

    **🔴 Before using see --> [Getting Started](/bigfunctions/getting_started/)**



{% for category in categories %}


<div style="margin-top: 6rem;"></div>


## {{ category.emoticon }} {{ category.name | replace('_', ' ') | capitalize }}

!!! note ""
    **{{ category.title }} **

    {{ category.subtitle }}

---

{% for bigfunction in category.bigfunctions %}

### {{ bigfunction.name }}
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  {% if bigfunction.author %}
  <a href="{{ bigfunction.author.url }}" title="{% if not bigfunction.author.name.startswith('Credits') %}Author: {% endif %}{{ bigfunction.author.name }}" target="_blank">
    <img src="{{ bigfunction.author.avatar_url }}" width="32" style=" border-radius: 50% !important">
  </a>
  {% endif %}
  <a href="{{ repo_url }}/blob/main/bigfunctions/{{ bigfunction.name }}.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
{{ bigfunction.name }}({% for argument in bigfunction.arguments %}{{ argument.name }}{% if not loop.last %}, {% endif %}{% endfor %})
```

**Description**

{{ bigfunction.description }}

**Examples**

{% for example in bigfunction.examples %}

{% if example.description %}<span style="color: var(--md-typeset-a-color);">{% if bigfunction.examples|length > 1 %}{{ loop.index }}. {% endif %}{{ example.description }}</span>{% endif %}


{% if datasets|length > 1 %}

{% for dataset in datasets if example.region == 'ALL' or dataset.region == example.region %}

=== "{{ dataset.region }}"

    ```sql
    {% if bigfunction.type == 'procedure' %}call{% elif bigfunction.type == 'table_function' %}select * from{% else %}select{% endif %} {{ dataset.name }}.{{ bigfunction.name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}', dataset.name) | replace('\n', '\n      ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if bigfunction.type == 'procedure' %};{% elif 'output' in bigfunction and bigfunction.type != 'table_function' %} as {{ bigfunction.output.name }}{% endif %}
    {% if bigfunction.type == 'procedure' and bigfunction.template %}select html from bigfunction_result;{% endif %}
    {%- if bigfunction.type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}
    ```

{% endfor %}


{% else %}

{% for dataset in datasets if example.region == 'ALL' or dataset.region == example.region %}

```sql
{% if bigfunction.type == 'procedure' %}call{% elif bigfunction.type == 'table_function' %}select * from{% else %}select{% endif %} {{ dataset.name }}.{{ bigfunction.name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}', dataset.name) | replace('\n', '\n  ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if bigfunction.type == 'procedure' %};{% elif 'output' in bigfunction and bigfunction.type != 'table_function' %} as {{ bigfunction.output.name }}{% endif %}
{% if bigfunction.type == 'procedure' and bigfunction.template %}select html from bigfunction_result;{% endif %}
{%- if bigfunction.type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}
```

{% endfor %}

{% endif %}


{% if bigfunction.type not in ('procedure', 'table_function') and 'output' in example %}

<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
{%- set output_name_length = bigfunction.output.name | length -%}
{%- set output_length = example.output | length -%}
{%- set hyphens_length = [output_name_length, output_length] | max -%}
{%- set hyphens = '-' * hyphens_length -%}
{%- set name_padding_length = [0, output_length - output_name_length] | max -%}
{%- set name_padding = ' ' * name_padding_length -%}
{%- set value_padding_length = [0, output_name_length - output_length] | max -%}
{%- set value_padding = ' ' * value_padding_length -%}
+-{{ hyphens }}-+
| {{ bigfunction.output.name }}{{ name_padding }} |
+-{{ hyphens }}-+
| {{ example.output | escape }}{{ value_padding }} |
+-{{ hyphens }}-+
</code>
</pre>

{% endif %}

{% if bigfunction.type in ('procedure', 'table_function') and 'output' in example %}

<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
{{ example.output }}
</code>
</pre>

{% endif %}


{% if example.screenshot %}<a href="../assets/images/{{ example.screenshot }}"><img alt="screenshot" src="../assets/images/{{ example.screenshot }}" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>{% endif %}
{% endfor %}


---


{% endfor %}



{% endfor %}
