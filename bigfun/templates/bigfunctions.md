---
title: "Explore"
description: "Catalog of open-source BigFunctions"
---


{% if project == 'bigfunctions' %}


!!! note ""

    **✅ You can call ANY of the following public BigFunctions from your Google Cloud Project** (*no install*).

    - The functions are deployed in `bigfunctions` GCP project in 39 datasets for all of the 39 BigQuery regions.
    - They are public, so they can be called by anyone.
    - For any question or difficulties, please read [Getting Started](../).
    - If you prefer to deploy the BigFunction in your own project, read [Getting Started](../).
    - Found a bug? Please raise an issue [here](https://github.com/unytics/bigfunctions/issues/new/choose)

??? info "All BigFunctions Datasets >"

    | Region | Dataset |
    |--------|---------|
    | `EU` | `bigfunctions.eu` |
    | `US` | `bigfunctions.us` |
    | `asia-east1` | `bigfunctions.asia_east1` |
    | `asia-east2` | `bigfunctions.asia_east2` |
    | `asia-northeast1` | `bigfunctions.asia_northeast1` |
    | `asia-northeast2` | `bigfunctions.asia_northeast2` |
    | `asia-northeast3` | `bigfunctions.asia_northeast3` |
    | `asia-south1` | `bigfunctions.asia_south1` |
    | `asia-south2` | `bigfunctions.asia_south2` |
    | `asia-southeast1` | `bigfunctions.asia_southeast1` |
    | `asia-southeast2` | `bigfunctions.asia_southeast2` |
    | `australia-southeast1` | `bigfunctions.australia_southeast1` |
    | `australia-southeast2` | `bigfunctions.australia_southeast2` |
    | `europe-central2` | `bigfunctions.europe_central2` |
    | `europe-north1` | `bigfunctions.europe_north1` |
    | `europe-southwest1` | `bigfunctions.europe_southwest1` |
    | `europe-west1` | `bigfunctions.europe_west1` |
    | `europe-west2` | `bigfunctions.europe_west2` |
    | `europe-west3` | `bigfunctions.europe_west3` |
    | `europe-west4` | `bigfunctions.europe_west4` |
    | `europe-west6` | `bigfunctions.europe_west6` |
    | `europe-west8` | `bigfunctions.europe_west8` |
    | `europe-west9` | `bigfunctions.europe_west9` |
    | `europe-west12` | `bigfunctions.europe_west12` |
    | `me-central1` | `bigfunctions.me_central1` |
    | `me-west1` | `bigfunctions.me_west1` |
    | `northamerica-northeast1` | `bigfunctions.northamerica_northeast1` |
    | `northamerica-northeast2` | `bigfunctions.northamerica_northeast2` |
    | `southamerica-east1` | `bigfunctions.southamerica_east1` |
    | `southamerica-west1` | `bigfunctions.southamerica_west1` |
    | `us-central1` | `bigfunctions.us_central1` |
    | `us-east1` | `bigfunctions.us_east1` |
    | `us-east4` | `bigfunctions.us_east4` |
    | `us-east5` | `bigfunctions.us_east5` |
    | `us-south1` | `bigfunctions.us_south1` |
    | `us-west1` | `bigfunctions.us_west1` |
    | `us-west2` | `bigfunctions.us_west2` |
    | `us-west3` | `bigfunctions.us_west3` |
    | `us-west4` | `bigfunctions.us_west4` |


{% endif %}

## 📄 Overview


BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.

!!! note ""



    {% for category in categories %}

    **{{ category.emoticon }} {% if category.name == 'AI' %}AI{% else %}{{ category.name | replace('_', ' ') | capitalize }}{% endif %}**

    {% for bigfunction in category.bigfunctions -%}
    {% set bigfunction_description_lines = bigfunction.description.split('\n') %}
    - [<code>{{ bigfunction.name }}({% for argument in bigfunction.arguments %}{{ argument.name }}{% if not loop.last %}, {% endif %}{% endfor %})</code>](#{{ bigfunction.name }}): {{ bigfunction_description_lines[0] }}
    {% endfor %}

    {% endfor %}




{% for category in categories %}


<div style="margin-top: 6rem;"></div>


## {{ category.emoticon }} {% if category.name == 'AI' %}AI{% else %}{{ category.name | replace('_', ' ') | capitalize }}{% endif %}

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

{% for dataset in datasets %}

{% set dataset_name = dataset.split('.')[1] %}

=== "{% if dataset_name|length <=2 %}{{ dataset_name | upper | replace('_', '-') }}{% else %}{{ dataset_name | replace('_', '-') }}{% endif %}"

    ```sql
    {% if bigfunction.type == 'procedure' %}call{% elif bigfunction.type == 'table_function' %}select * from{% else %}select{% endif %} {{ dataset }}.{{ bigfunction.name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}', dataset) | replace('\n', '\n      ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if bigfunction.type == 'procedure' %};{% elif 'output' in bigfunction and bigfunction.type != 'table_function' %} as {{ bigfunction.output.name }}{% endif %}
    {% if bigfunction.type == 'procedure' and bigfunction.template %}select html from bigfunction_result;{% endif %}
    {%- if bigfunction.type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}
    ```

{% endfor %}


{% else %}

{% for dataset in datasets %}

```sql
{% if bigfunction.type == 'procedure' %}call{% elif bigfunction.type == 'table_function' %}select * from{% else %}select{% endif %} {{ dataset }}.{{ bigfunction.name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}', dataset) | replace('\n', '\n  ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if bigfunction.type == 'procedure' %};{% elif 'output' in bigfunction and bigfunction.type != 'table_function' %} as {{ bigfunction.output.name }}{% endif %}
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


{% if example.screenshot %}<a href="{{ example.screenshot }}"><img alt="screenshot" src="{{ example.screenshot }}" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>{% endif %}
{% endfor %}


---


{% endfor %}



{% endfor %}
