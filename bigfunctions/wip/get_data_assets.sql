create or replace table TEMP.data_assets as

with


----------------------------------------
--             SOURCES                --
----------------------------------------
superdashboards as (
  select
    dashs.*,
    (10 - offset) as popularity,
  from unnest([
    struct('Onboarding' as name,                       'eb4130d0-2fd7-4b81-a9c1-eb0b7c005d78' as report_id),
    struct('Point of Sales Experience' as name,        'c42204bf-9150-4e63-81fc-8c62c6a6be53' as report_id),
    struct('Pay & Get Paid' as name,                    '23457130-0caf-4d22-a04e-b0a768d94864' as report_id),
    struct('Customer Experience - Cockpit CX' as name, '535c514b-6569-4d26-a766-16565e261143' as report_id),
    struct('Customer Experience - Product' as name,    'f4c57f7e-e0cc-4ac9-b02a-d7b3a6080926' as report_id),
    struct('Compliance' as name,                        'a8f423e6-1f5a-46b6-9c0c-a5bd6ab33ca1' as report_id)
  ]) as dashs
  with offset as offset
),

dashboards as (
  select
    json_value(properties, '$.title') as name,
    json_value(properties, '$.description') as description,
    json_value(properties, '$.url') as url,
  from DATA_PORTAL.CONF
  where type = "dashboard_content"
  qualify row_number() over(partition by id order by updated_at desc) = 1
),

datasets as (
  select
    schema_name as name,
  from `region-eu`.INFORMATION_SCHEMA.SCHEMATA
),

datasets_descriptions as (
  select
    schema_name as name,
    regexp_extract(option_value, '^"(.*)"$') as description,
  from `region-eu`.INFORMATION_SCHEMA.SCHEMATA_OPTIONS
  where option_name = 'description'
),

datasets_labels as (
  select
    schema_name as name,
    ifnull(regexp_extract(option_value, '"confidentiality", "([^"]*)"'), '') as confidentiality,
    ifnull(regexp_extract(option_value, '"dataset_type", "([^"]*)"'), '') as dataset_type,
  from `region-eu`.INFORMATION_SCHEMA.SCHEMATA_OPTIONS
  where option_name = 'labels'
),

datasets_usage_by_user as (
  select
    referenced_table.dataset_id as name,
    user_email as user,
    count(*) as nb_queries_30d
  from `region-eu`.INFORMATION_SCHEMA.JOBS,
  unnest(referenced_tables) referenced_table
  where
    date(creation_time) >= current_date - 30
    and not starts_with(referenced_table.dataset_id, '_')
    and parent_job_id is null
  group by 1, 2
),

tables as (
  select
    table_schema || '.' || table_name as table,
    table_schema as dataset,
    table_name as name,
    creation_time as created_at,
  from `region-eu`.INFORMATION_SCHEMA.TABLES
  where not starts_with(table_schema, '_')
),

table_storage as (
  select
    table_schema || '.' || table_name as table,
    total_rows,
    (total_logical_bytes + total_physical_bytes) / pow(2, 20) as total_MB,
    (total_logical_bytes + total_physical_bytes) / pow(2, 30) as total_GB,
    (total_logical_bytes + total_physical_bytes) / pow(2, 40) as total_TB,
    ifnull(storage_last_modified_time, creation_time) as last_updated_at,
  from `region-eu`.INFORMATION_SCHEMA.TABLE_STORAGE
  where
    not starts_with(table_schema, '_')
    and deleted is false
),

table_descriptions as (
  select
    table_schema || '.' || table_name as table,
    regexp_extract(option_value, '^"(.*)"$') as description,
  from `region-eu`.INFORMATION_SCHEMA.TABLE_OPTIONS
  where option_name = 'description'
),

tables_usage_by_user as (
  select
    referenced_table.dataset_id || '.' || referenced_table.table_id as table,
    user_email as user,
    count(*) as nb_queries_30d
  from `region-eu`.INFORMATION_SCHEMA.JOBS,
  unnest(referenced_tables) referenced_table
  where
    date(creation_time) >= current_date - 30
    and not starts_with(referenced_table.dataset_id, '_')
    and parent_job_id is null
  group by 1, 2
),

columns as (
  select
    field_path as name,
    table_schema || '.' || table_name as table,
    data_type,
    description,
  from `region-eu`.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS
),

columns_details as (
  select
    column_name as name,
    table_schema || '.' || table_name as table,
    ordinal_position,
    is_partitioning_column,
  from `region-eu`.INFORMATION_SCHEMA.COLUMNS
),


----------------------------------------
--            TRANSFORMS              --
----------------------------------------
datasets_usage as (
  select
    name,
    count(*) as nb_users_30d,
    array_agg(struct(user, nb_queries_30d) order by nb_queries_30d desc) as nb_queries_by_user_30d,
  from datasets_usage_by_user
  group by name
),

tables_usage as (
  select
    table,
    count(*) as nb_users_30d,
    array_agg(struct(user, nb_queries_30d) order by nb_queries_30d desc) as nb_queries_by_user_30d,
  from tables_usage_by_user
  group by table
),

users_usage as (
  select
    user,
    initcap(
      replace(replace(regexp_replace(
        regexp_extract(user, '([^@]*)@'),
        '^s-', ''),
        '.', ' '),
        '-dataprod', ''
      )
    ) as name,
    sum(nb_queries_30d) as nb_queries_30d,
    count(*) as nb_tables_queried_30d,
    array_agg(struct(table, nb_queries_30d) order by nb_queries_30d desc) as nb_queries_by_table_30d,
  from tables_usage_by_user
  group by user
),


----------------------------------------
--              JOINS                 --
----------------------------------------
dashboards_enriched as (
  select
    *,
    'dashboard' as type,
    'dashboard.' || report_id as id,
    name as names,
    name as description,
    0 as popularity
  from superdashboards
),

superdashboards_enriched as (
  select
    *,
    'dashboard' as type,
    name as names,
  from dashboards
),

datasets_enriched as (
  select
    'dataset' as type,
    'dataset.' || name as id,
    name || ' ' || regexp_replace(name, r'[^a-zA-Z]', ' ') as names,
    ifnull(description, '') as description,
    ifnull(nb_users_30d, 0) as popularity,
    ifnull(nb_users_30d, 0) as nb_users_30d,
    * except(description, nb_users_30d),
    (select count(*) from tables where tables.dataset = datasets.name) as nb_tables,
    array(select table from tables where tables.dataset = datasets.name) as tables,
  from datasets
  left join datasets_descriptions using(name)
  left join datasets_labels using(name)
  left join datasets_usage using(name)
),


columns_enriched as (
  select *
  from columns
  left join columns_details using(table, name)
),

tables_enriched as (
  select
    'table' as type,
    'table.' || dataset || '.' || name as id,
    dataset || ' ' || name || ' ' || regexp_replace(dataset, r'[^a-zA-Z]', ' ') || ' ' || regexp_replace(name, r'[^a-zA-Z]', ' ') as names,
    ifnull(description, '') as description,
    ifnull(nb_users_30d, 0) as popularity,
    ifnull(nb_users_30d, 0) as nb_users_30d,
    * except(description),
    case
      when total_TB > 1 then format('%.2f TB', total_TB)
      when total_GB > 1 then format('%.2f GB', total_GB)
      else format('%.2f MB', total_MB)
    end as total_size,
    (select array_agg((select as struct columns_enriched.* except(table))) from columns_enriched where columns_enriched.table = tables.table) as columns,

  from tables
  left join table_storage using(table)
  left join table_descriptions using (table)
  left join tables_usage using (table)
),

data4all_tables_enriched as (
  select * replace('supertable' as type)
  from tables_enriched
  where dataset = 'DATA4ALL'
),

other_tables_enriched as (
  select * replace('table' as type)
  from tables_enriched
  where
    dataset != 'DATA4ALL'
),

columns_stats as (
  select
    name,
    count(*) as nb_tables,
    array_agg(table) as tables,
    array_agg(data_type) as data_types,
    array_agg(description) as descriptions,
  from columns_enriched
  group by name
),

columns_stats_enriched as (
  select
    'column' as type,
    'column.' || name as id,
    nb_tables as popularity,
    name || ' ' || replace(name, '.', ' ') || ' ' || regexp_replace(name, r'[^a-zA-Z]', ' ') as names,
    * except(data_types, descriptions),
    (select struct(v as value, count(v) as nb) from columns_stats.data_types v group by v order by count(1) desc limit 1 ) as most_represented_data_type,
    (select struct(v as value, count(v) as nb) from columns_stats.descriptions v where v is not null group by v order by count(1) desc limit 1 ) as most_represented_description,
    ifnull((select v from columns_stats.descriptions v where v is not null group by v order by count(1) desc limit 1 ), '') as description,
  from columns_stats
),

users_enriched as (
  select
    *,
    'user' as type,
    'user.' || user as id,
    'Compte Individuel' as description,
    user || ' ' || name as names,
    nb_queries_30d as popularity,
  from users_usage
  where ends_with(user, '@nickel.eu')
),

apps_enriched as (
  select
    *,
    'app' as type,
    'app.' || user as id,
    'App Data' as description,
    user || ' ' || name as names,
    nb_queries_30d as popularity,
  from users_usage
  where not ends_with(user, '@nickel.eu')
)


----------------------------------------
--              FINAL                 --
----------------------------------------
select to_json_string(struct(dashboards_enriched).dashboards_enriched) as data from dashboards_enriched union all
select to_json_string(struct(datasets_enriched).datasets_enriched) as data from datasets_enriched union all
select to_json_string(struct(data4all_tables_enriched).data4all_tables_enriched) as data from data4all_tables_enriched union all
select to_json_string(struct(other_tables_enriched).other_tables_enriched) as data from other_tables_enriched union all
select to_json_string(struct(columns_stats_enriched).columns_stats_enriched) as data from columns_stats_enriched union all
select to_json_string(struct(users_enriched).users_enriched) as data from users_enriched union all
select to_json_string(struct(apps_enriched).apps_enriched) as data from apps_enriched
