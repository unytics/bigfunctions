create schema if not exists {{ dataset }}
options (location = "{{ region }}");

alter schema {{ dataset }}
set options (description = "{{ dataset_description }} (region={{ region }}, environment={{ environment }})");
