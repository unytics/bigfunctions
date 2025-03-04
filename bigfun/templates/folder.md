{{ readme }}


{% if subfolders %}

## Function Categories

<div class="grid cards  " markdown>

{% for subfolder in subfolders -%}

-   ### [{{ subfolder.title }}]({{ subfolder.name }}/README.md)

    {% if subfolder.content -%}
    ---

    {{ subfolder.content | indent(4) }}
    {% endif %}

{% endfor %}

{% endif %}



{% if bigfunctions %}

## Functions

<div class="functions-table" markdown>

| Signature | Short Description |
|------|---------|
{% for bigfunction in bigfunctions if not bigfunction.hide_in_doc -%}
| [<code>{{ bigfunction.signature }}</code>]({{ '../' * depth }}{{ bigfunction.name }}.md) | {{ bigfunction.short_description }} |
{% endfor -%}

</div>

{% endif %}
