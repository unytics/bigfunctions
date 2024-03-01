---
description: "Catalog of open-source BigFunctions"
search:
  exclude: true
---

# BigFunctions


BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.


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
    {% for dataset in dataset.split(',') -%}    
    | `{{ dataset.replace('_', '-') }}` | `{{ project }}.{{ dataset }}` |
    {% endfor %}

{% endif %}



{% for category in categories -%}

## {{ category.emoticon }} {% if category.name == 'AI' %}AI{% else %}{{ category.name | replace('_', ' ') | capitalize }}{% endif %}

{% for bigfunction in category.bigfunctions -%}
{% set bigfunction_description_lines = bigfunction.description.split('\n') -%}
- [<code>{{ bigfunction.name }}({% for argument in bigfunction.arguments %}{{ argument.name }}{% if not loop.last %}, {% endif %}{% endfor %})</code>]({{ bigfunction.name }}/): {{ bigfunction_description_lines[0] }}
{% endfor %}

{% endfor %}

