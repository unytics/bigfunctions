create or replace procedure {{ dataset.name }}.{{ name }}({% for argument in arguments %}{{ argument.name }} {{ argument.type}}{% if not loop.last %}, {% endif %}{% endfor %})
options(
    description = '''{{ documentation }}'''
)
begin

{{ code }}

end;
