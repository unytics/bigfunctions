---
title: "upsert"
description: "BigFunction upsert: Merges `query_or_table_or_view` into the `destination_table`."
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > upsert
</span>

# upsert


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/axel-thevenot/" title="Author: Axel Thevenot" target="_blank">
    <img src="https://avatars.githubusercontent.com/u/39374103?v=4" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/upsert.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
upsert(query_or_table_or_view, destination_table, insertion_mode, primary_keys, recency_field)
```

**Description**

Merges `query_or_table_or_view` into the `destination_table`.

A record is identified by its `primary_keys`. A unique combination of those fields is a unique record.
Before the merging operation, the records are identified and deduplicated according to the `primary_keys`.
If `recency_field` is filled then the last record version is kept else it is chosen arbitrarily.


| Param  | Possible values  |
|---|---|
| `query_or_table_or_view` | Can be a fully qualified table or view `(<project-id>.)?<dataset_id>.<table_or_view_name>`. <br> Can also be a plain query in BigQuery Standard SQL. |
| `destination_table` | Must be a fully qualified table `(<project-id>.)?<dataset_id>.<table_or_view_name>`. |
| `insertion_mode` | Three insertion mode are available:<ul><li> `"insert_only"`: existing records in `query_or_table_or_view` and not existing in `destination_table` are inserted. Deletion and update are not possible. </li><li> `"delta"`: same as `insert_only` with the updatable records. Records existing both in `query_or_table_or_view` and in  `destination_table` are updated. If `recency_field` is filled, only the most recent version from source and destination is kept. </li><li> `"full"`: same as `delta` with the deletable records. Records not existing in `query_or_table_or_view` and existing in `destination_table` are deleted. </li> </ul> |
| `primary_keys` | Combination of field identifying a record. If `primary_keys = []`, every row will be considered as a unique record. |
| `recency_field` | Orderable field (ie. `timestamp`, `integer`, ...) to identify the relative frechness of a record version. |





**Examples**



<span style="color: var(--md-typeset-a-color);">1. Merge tables in delta mode</span>









=== "EU"

    ```sql
    call bigfunctions.eu.upsert('dataset_id.source_table_or_view', 'dataset_id.destination_table', 'delta', ['id'], 'timestamp_field');
    
    ```




=== "US"

    ```sql
    call bigfunctions.us.upsert('dataset_id.source_table_or_view', 'dataset_id.destination_table', 'delta', ['id'], 'timestamp_field');
    
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.upsert('dataset_id.source_table_or_view', 'dataset_id.destination_table', 'delta', ['id'], 'timestamp_field');
    
    ```















<span style="color: var(--md-typeset-a-color);">2. Merge from query in full</span>









=== "EU"

    ```sql
    call bigfunctions.eu.upsert('select * from dataset_id.source_table_or_view where filter_field = true', 'dataset_id.destination_table', 'full', ['id'], null);
    
    ```




=== "US"

    ```sql
    call bigfunctions.us.upsert('select * from dataset_id.source_table_or_view where filter_field = true', 'dataset_id.destination_table', 'full', ['id'], null);
    
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.upsert('select * from dataset_id.source_table_or_view where filter_field = true', 'dataset_id.destination_table', 'full', ['id'], null);
    
    ```















