create schema if not exists {{ dataset.name }}
options (location = "{{ region }}");

alter schema {{ dataset.name }}
set options (description = """{{ dataset.description }}""");

grant `roles/bigquery.dataViewer`
ON SCHEMA {{ dataset.name }}
TO 'specialGroup:allAuthenticatedUsers';
