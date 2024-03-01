---
title: "upload_table_to_gsheet"
description: "BigFunction upload_table_to_gsheet: Upload data from `table_or_view_or_query` to Google Sheet
(maximum `max_rows` rows will be uploaded).

> 1. 💡 For this to work, share your Google Sheet in edit mode to `749389685934-compute@developer.gserviceaccount.com`
> 2. `write_mode` controls what is done if a worksheet with `worksheet_name` already exists. It must be one of:
>     - `write_truncate`: if the sheet already exists, it will be recreated.
>     - `write_append`: if the sheet already exists, data will be appended to it.
>     - `raise_error`:  if the sheet already exists, an error will be raised.
>     - `do_nothing`:  if the sheet already exists, nothing will be done.
>     - `null`: same as `write_truncate`
"
---

<span style="color: gray; position: relative; top: -1rem">
  <a href=".." style="color: gray">bigfunctions </a> ＞ upload_table_to_gsheet
</span>

# upload_table_to_gsheet


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="upload_table_to_gsheet.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
upload_table_to_gsheet(table_or_view_or_query, max_rows, spreadsheet_url, worksheet_name, write_mode)
```

**Description**

Upload data from `table_or_view_or_query` to Google Sheet
(maximum `max_rows` rows will be uploaded).

> 1. 💡 For this to work, share your Google Sheet in edit mode to `749389685934-compute@developer.gserviceaccount.com`
> 2. `write_mode` controls what is done if a worksheet with `worksheet_name` already exists. It must be one of:
>     - `write_truncate`: if the sheet already exists, it will be recreated.
>     - `write_append`: if the sheet already exists, data will be appended to it.
>     - `raise_error`:  if the sheet already exists, an error will be raised.
>     - `do_nothing`:  if the sheet already exists, nothing will be done.
>     - `null`: same as `write_truncate`






**Examples**



<span style="color: var(--md-typeset-a-color);">1. upload 1000 rows from a table</span>









=== "EU"

    ```sql
    call bigfunctions.eu.upload_table_to_gsheet(
      'eu.sales', 
      1000, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```




=== "US"

    ```sql
    call bigfunctions.us.upload_table_to_gsheet(
      'us.sales', 
      1000, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.upload_table_to_gsheet(
      'europe_west1.sales', 
      1000, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```












<a href="upload_table_to_gsheet.png"><img alt="screenshot" src="upload_table_to_gsheet.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>


<span style="color: var(--md-typeset-a-color);">2. with a query</span>









=== "EU"

    ```sql
    call bigfunctions.eu.upload_table_to_gsheet(
      '(select 1 as foo)', 
      null, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```




=== "US"

    ```sql
    call bigfunctions.us.upload_table_to_gsheet(
      '(select 1 as foo)', 
      null, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.upload_table_to_gsheet(
      '(select 1 as foo)', 
      null, 
      'https://docs.google.com/spreadsheets/d/xxxxxxxxx', 
      'my worksheet', 
      'write_truncate');
    
    ```















