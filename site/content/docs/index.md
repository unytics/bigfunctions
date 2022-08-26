---
hide:
  - navigation
---

#
<img src="../assets/logo_and_name.png" alt="drawing" width="300"/>

BigFunctions are public BigQuery routines that give you new *SQL powers* in BigQuery 💪.

We are introducing today the first two functions. [Tell us what you think](https://github.com/unytics/bigfunctions/discussions)! 😊.

---


## GET_DATASET_TABLES

> Creates a temporary table called `GET_DATASET_TABLES_result` with tables of `fully_qualified_dataset` dataset
```
GET_DATASET_TABLES(fully_qualified_dataset)
```
> **Returns** ➜ `TEMP TABLE`

<h3>Example</h3>


=== "EU"

    ``` sql
    CALL bigfunctions.eu.GET_DATASET_TABLES('bigquery-public-data.samples');
    SELECT * FROM  GET_DATASET_TABLES_result;
    
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | table_catalog        | table_schema | table_name      | table_type | is_insertable_into | is_typed | creation_time            | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | bigquery-public-data | samples      | natality        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:47.183Z | ... |
    | bigquery-public-data | samples      | github_timeline | BASE TABLE | YES                | NO       | 2016-03-14T17:16:45.074Z | ... |
    | bigquery-public-data | samples      | github_nested   | BASE TABLE | YES                | NO       | 2016-03-14T17:16:44.113Z | ... |
    | bigquery-public-data | samples      | trigrams        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:50.399Z | ... |
    | ...                  | ...          | ...             | ...        | ...                | ...      | ...                      | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    ```

=== "US"

    ``` sql
    CALL bigfunctions.us.GET_DATASET_TABLES('bigquery-public-data.samples');
    SELECT * FROM  GET_DATASET_TABLES_result;
    
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | table_catalog        | table_schema | table_name      | table_type | is_insertable_into | is_typed | creation_time            | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | bigquery-public-data | samples      | natality        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:47.183Z | ... |
    | bigquery-public-data | samples      | github_timeline | BASE TABLE | YES                | NO       | 2016-03-14T17:16:45.074Z | ... |
    | bigquery-public-data | samples      | github_nested   | BASE TABLE | YES                | NO       | 2016-03-14T17:16:44.113Z | ... |
    | bigquery-public-data | samples      | trigrams        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:50.399Z | ... |
    | ...                  | ...          | ...             | ...        | ...                | ...      | ...                      | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    ```

=== "europe-west1"

    ``` sql
    CALL bigfunctions.europe_west1.GET_DATASET_TABLES('bigquery-public-data.samples');
    SELECT * FROM  GET_DATASET_TABLES_result;
    
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | table_catalog        | table_schema | table_name      | table_type | is_insertable_into | is_typed | creation_time            | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | bigquery-public-data | samples      | natality        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:47.183Z | ... |
    | bigquery-public-data | samples      | github_timeline | BASE TABLE | YES                | NO       | 2016-03-14T17:16:45.074Z | ... |
    | bigquery-public-data | samples      | github_nested   | BASE TABLE | YES                | NO       | 2016-03-14T17:16:44.113Z | ... |
    | bigquery-public-data | samples      | trigrams        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:50.399Z | ... |
    | ...                  | ...          | ...             | ...        | ...                | ...      | ...                      | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    ```

=== "your-region2"

    ``` sql
    CALL bigfunctions.your_region2.GET_DATASET_TABLES('bigquery-public-data.samples');
    SELECT * FROM  GET_DATASET_TABLES_result;
    
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | table_catalog        | table_schema | table_name      | table_type | is_insertable_into | is_typed | creation_time            | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    | bigquery-public-data | samples      | natality        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:47.183Z | ... |
    | bigquery-public-data | samples      | github_timeline | BASE TABLE | YES                | NO       | 2016-03-14T17:16:45.074Z | ... |
    | bigquery-public-data | samples      | github_nested   | BASE TABLE | YES                | NO       | 2016-03-14T17:16:44.113Z | ... |
    | bigquery-public-data | samples      | trigrams        | BASE TABLE | YES                | NO       | 2016-03-14T17:16:50.399Z | ... |
    | ...                  | ...          | ...             | ...        | ...                | ...      | ...                      | ... |
    +----------------------+--------------+-----------------+------------+--------------------+----------+--------------------------+-----+
    ```


<a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/GET_DATASET_TABLES.yaml" target="_blank">Source Code</a>

---




## RENDER_TEMPLATE

> Replaces the variables surrounded by brackets such as `{{variable_name}}` in `template` by their values defined in `context`.
> Beware that `context` keys and string values must be surrounded by double-quotes `"` and not single-quotes `'`.
```
RENDER_TEMPLATE(template, context)
```
> **Returns** ➜ `STRING`

<h3>Example</h3>


=== "EU"

    ``` sql
    SELECT bigfunctions.eu.RENDER_TEMPLATE('Hello {{who}}', '{"who": "world"}') as content;
    
    +-------------+
    | content     |
    +-------------+
    | Hello World |
    +-------------+
    ```

=== "US"

    ``` sql
    SELECT bigfunctions.us.RENDER_TEMPLATE('Hello {{who}}', '{"who": "world"}') as content;
    
    +-------------+
    | content     |
    +-------------+
    | Hello World |
    +-------------+
    ```

=== "europe-west1"

    ``` sql
    SELECT bigfunctions.europe_west1.RENDER_TEMPLATE('Hello {{who}}', '{"who": "world"}') as content;
    
    +-------------+
    | content     |
    +-------------+
    | Hello World |
    +-------------+
    ```

=== "your-region2"

    ``` sql
    SELECT bigfunctions.your_region2.RENDER_TEMPLATE('Hello {{who}}', '{"who": "world"}') as content;
    
    +-------------+
    | content     |
    +-------------+
    | Hello World |
    +-------------+
    ```


<a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/RENDER_TEMPLATE.yaml" target="_blank">Source Code</a>

---

