---
hide:
  - navigation
---

#
<img src="../assets/logo_and_name.png" alt="drawing" width="300"/>

BigFunctions are public BigQuery routines that give you new *SQL powers* in BigQuery 💪.

We are introducing today the first two functions. [Tell us what you think](https://github.com/unytics/bigfunctions/discussions)! 😊.

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

