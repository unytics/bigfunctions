---
hide:
  - navigation
---

#
<img src="../assets/logo_and_name.png" alt="drawing" width="300"/>

BigFunctions are public BigQuery routines that give you new *SQL powers* in BigQuery 💪.

We are introducing today the first two functions. [Tell us what you think](https://github.com/unytics/bigfunctions/discussions)! 😊.


---



## compute_columns_statistics

**Description**

This function compute statistics over columns.


**Input Parameters**

| Parameter Name      | Type   | Description                          |    Example  |
| ----------- | ------------------------------------ | ------------------ | ---------------- |
| table       | `string` | Fully qualified table name to compute statistics from  |  `your-project.your_dataset.your_table` |



**Usage**

=== "region-eu"

    ``` sql
    declare table string default '`your-project.your_dataset.your_table`'
    call bigfunctions.eu.compute_columns_statistics(table)
    ```

=== "region-us"

    ``` sql
    call bigfunctions.us.compute_columns_statistics('`your-project.your_dataset.your_table`')
    ```


**Code**


---


## render_template_simple


**Description**
This function compute statistics over columns


**Usage**

=== "region-eu"

    ``` sql
    call bigfunctions.eu.render_template_simple('`your-project.your_dataset.your_table`')
    ```

=== "region-us"

    ``` sql
    call bigfunctions.us.render_template_simple('`your-project.your_dataset.your_table`')
    ```







