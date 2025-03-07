---
{{ frontmatter }}
---

{% set path_parts = path.split('/') %}

{% if path_parts|length > 1 %}

<div class="breadcrumb" markdown>

{% for part in path_parts -%}
- [{{ part }}]({{ '../' * loop.revindex0 }}README.md){% if not loop.last %}<span style="margin: 0 20px">❯</span>{% endif %}
{% endfor -%}

</div>

{% endif %}


{% if not content_contains_title %}
# {{ title }}
{% endif %}


{{ content }}


{% if subfolders %}

!!! note ""

    #### Function Categories

    {% for subfolder in subfolders -%}
    {{ loop.index }}. <a href="{{ subfolder.inner_link }}-{{ subfolder.nb_bigfunctions }}-functions">{{ subfolder.title }}</a>
    {% endfor %}

---
{% endif %}


{% for subfolder in subfolders -%}

## {{ subfolder.title }} [({{ subfolder.nb_bigfunctions }} functions)]({{ subfolder.name }}/README.md)

> {{ subfolder.content | replace('\n', '\n> ') }}


{% for subsubfolder in subfolder.subfolders -%}


!!! note "{{ subsubfolder.title }}"

    > {{ subsubfolder.content | replace('\n', '\n    > ') }}

    {% for subsubsubfolder in subsubfolder.subfolders -%}
    - [{{ subsubsubfolder.title }}]({{ subsubsubfolder.name }}.md)
    {% endfor %}


    {% for bigfunction in subsubfolder.bigfunctions if not bigfunction.hide_in_doc -%}
    - [<code>{{ bigfunction.name }}</code>]({{ '../' * depth }}{{ bigfunction.name }}.md): {{ bigfunction.short_description }}
    {% endfor %}


{% endfor %}


{% if subfolder.bigfunctions %}

!!! note ""

    {% for bigfunction in subfolder.bigfunctions if not bigfunction.hide_in_doc -%}
    - [<code>{{ bigfunction.name }}</code>]({{ '../' * depth }}{{ bigfunction.name }}.md): {{ bigfunction.short_description }}
    {% endfor %}

{% endif %}


{% endfor %}



{% if bigfunctions %}

!!! note ""

    {% for bigfunction in bigfunctions if not bigfunction.hide_in_doc -%}
    - [<code>{{ bigfunction.name }}</code>]({{ '../' * depth }}{{ bigfunction.name }}.md): {{ bigfunction.short_description }}
    {% endfor %}


{% endif %}
