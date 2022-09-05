create schema if not exists {{ dataset.name }}
options (location = "{{ region }}");

alter schema {{ dataset.name }}
set options (description = """{{ dataset.description }}""");

grant `projects/bigfunctions/roles/bigquery_routine_get`
ON SCHEMA {{ dataset.name }}
TO 'specialGroup:allAuthenticatedUsers';
