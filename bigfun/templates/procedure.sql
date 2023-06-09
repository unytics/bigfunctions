create or replace procedure {{ dataset }}.{{ name }}({% for argument in arguments %}{% if argument.out %}out {% endif %}`{{ argument.name }}` {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ description }}'''
)
begin

{{ code }}


end;
