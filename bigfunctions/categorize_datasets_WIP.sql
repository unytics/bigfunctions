create temp table schema as

with 

tables as (

  select 
    dataset,
    (
      '<table>' ||
        '<name>' || table || '</name>' ||
        if(description != '', '<description>' || description || '</description>', '') ||
        '<columns>' || (select array_to_string(array_agg(col.name order by col.name), ', ') from unnest(columns) as col) || '</columns>' ||
    '</table>'
    ) as table_xml
  from bigfunctions.us.bigquery_public_tables
  qualify 
    (row_number() over (partition by (dataset || '.' || regexp_replace(regexp_replace(table, r'\d', ''), '(_*)$', '')) order by table desc) = 1) and
    (row_number() over (partition by dataset order by table desc) < 15)
  order by table

),

datasets as (

  select (
    '<dataset>' ||
      '<name>' || dataset || '</name>' || 
      '<tables>' || array_to_string(array_agg(table_xml), '') || '</tables>' ||
    '</dataset>' 
  ) as dataset_xml
  from tables
  group by dataset
  order by dataset

),

context as (

  select array_to_string(array_agg(dataset_xml), '\n\n') as datasets_xml
  from datasets

),

datasets_categories as (
  select bigfunctions.us.categorize_datasets(datasets_xml) as datasets_with_categories
  from context
)

select 
  dataset.dataset,
  dataset.path,
from datasets_categories, 
unnest(json_query_array(datasets_with_categories, '$')) dataset

;
select 1