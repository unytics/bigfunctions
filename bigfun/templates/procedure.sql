create or replace procedure {{ fully_qualified_dataset }}.{{ name }}({% for argument in arguments %}{% if argument.out %}out {% endif %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ description }}'''
)
begin

{{ code }}

{% if template %}
create or replace temp table bigfunction_result as
select
    (select json from bigfunction_result) as json,
    (select {{ fully_qualified_dataset }}.render_template(
        """<html>
        {{ template }}
        </html>""",
        json
    )
    from bigfunction_result) as html
;
{% endif %}

end;
