create or replace procedure `{{ project }}`.`{{ dataset }}`.{{ name }}({% for argument in arguments %}{% if argument.out %}out {% endif %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ description }}'''
)
begin

{{ code | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) }}

{% if template %}
create or replace temp table bigfunction_result as
select
    (select json from bigfunction_result) as json,
    (select `{{ project }}`.`{{ dataset }}`.render_template(
        """<html>
        {{ template }}
        </html>""",
        json
    )
    from bigfunction_result) as html
;
{% endif %}

end;
