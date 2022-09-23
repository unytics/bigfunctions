---
hide:
  - navigation
---

## 📄 Overview

!!! note ""

    BigFunctions are public BigQuery routines that give you **super-SQL-powers** in BigQuery 💪.


    

    **👀 Explore**

    "Explore" BigFunctions are great for data-analysts to explore data.They make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.

    - [<code>explore_column(fully_qualified_column)</code>](#explore_column): Show column statistics
    - [<code>explore_dataset(fully_qualified_dataset)</code>](#explore_dataset): Shows infos about dataset tables
    - [<code>explore_table(fully_qualified_table)</code>](#explore_table): Show table infos and column statistics
    

    

    **✨ Transform**

    "Transform" BigFunctions transform data.Get ready to be amazed.

    - [<code>transform_text2sentiment_score(content)</code>](#transform_text2sentiment_score): Compute sentiment score of text
    

    

    **💬 Notify**

    "Notify" BigFunctions send notifications such as emails, chats, sms, etc.Spread the word to the world!

    - [<code>notify_gmail(to, subject, body)</code>](#notify_gmail): Send email via gmail
    

    

    **🔨 Utils**

    "Utils" BigFunctions are tools used by other BigFunctions.

    - [<code>chart(data, chart_type, ylabel)</code>](#chart): Returns html with a chartjs chart
    - [<code>levenshtein(string1, string2)</code>](#levenshtein): Computes levenshtein distance between `string1` and `string2`
    - [<code>render_string(template, context)</code>](#render_string): Render template with context json object using nunjucks.js templating library
    

    

    **🔴 Before using see --> [Getting Started](/bigfunctions/getting_started/)**


<div style="margin-top: 6rem;"></div>


## 👀 Explore

!!! note ""

    **"Explore" BigFunctions are great for data-analysts to explore data**.
    
    They make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.
### explore_column
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_column.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_column(fully_qualified_column)
```

**Description**

Show column statistics

**Examples**










```sql
call bigfunctions.us.explore_column("bigquery-public-data.samples.natality.weights_pounds");
select html from bigfunction_result;
```


<a href="../assets/images/explore_column.png"><img alt="screenshot" src="../assets/images/explore_column.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---



### explore_dataset
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_dataset.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_dataset(fully_qualified_dataset)
```

**Description**

Shows infos about dataset tables

**Examples**










```sql
call bigfunctions.us.explore_dataset("bigquery-public-data.samples");
select html from bigfunction_result;
```


<a href="../assets/images/explore_dataset.png"><img alt="screenshot" src="../assets/images/explore_dataset.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---



### explore_table
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_table.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_table(fully_qualified_table)
```

**Description**

Show table infos and column statistics

**Examples**










```sql
call bigfunctions.us.explore_table("bigquery-public-data.samples.natality");
select html from bigfunction_result;
```


<a href="../assets/images/explore_column.png"><img alt="screenshot" src="../assets/images/explore_column.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---

<div style="margin-top: 6rem;"></div>


## ✨ Transform

!!! note ""

    **"Transform" BigFunctions transform data**.
    
    Get ready to be amazed.
### transform_text2sentiment_score
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/transform_text2sentiment_score.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
transform_text2sentiment_score(content)
```

**Description**

Compute sentiment score of text

**Examples**








=== "EU"

    ```sql
    select bigfunctions.eu.transform_text2sentiment_score('BigFunctions Rock!') as sentiment_score
    ```


=== "US"

    ```sql
    select bigfunctions.us.transform_text2sentiment_score('BigFunctions Rock!') as sentiment_score
    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.transform_text2sentiment_score('BigFunctions Rock!') as sentiment_score
    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.transform_text2sentiment_score('BigFunctions Rock!') as sentiment_score
    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
+------------------+
| sentiment_score  |
+------------------+
| 0.945            |
+------------------+

</code>
</pre>







---
<div style="margin-top: 6rem;"></div>


## 💬 Notify

!!! note ""

    **"Notify" BigFunctions send notifications such as emails, chats, sms, etc**.
    
    Spread the word to the world!
### notify_gmail
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/notify_gmail.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
notify_gmail(to, subject, body)
```

**Description**

Send email via gmail

**Examples**








=== "EU"

    ```sql
    select bigfunctions.eu.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?') as success
    ```


=== "US"

    ```sql
    select bigfunctions.us.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?') as success
    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?') as success
    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?') as success
    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
+---------+
| success |
+---------+
| true    |
+---------+

</code>
</pre>







---
<div style="margin-top: 6rem;"></div>


## 🔨 Utils

!!! note ""

    **"Utils" BigFunctions** are tools used by other BigFunctions.
### chart
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/chart.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
chart(data, chart_type, ylabel)
```

**Description**

Returns html with a chartjs chart

**Examples**








=== "EU"

    ```sql
    select bigfunctions.eu.chart([('2022-08-01', 10000.), ('2022-08-02', 20000.), ('2022-08-03', 40000.), ('2022-08-04', 80000.)], 'bar', 'sales') as html
    ```


=== "US"

    ```sql
    select bigfunctions.us.chart([('2022-08-01', 10000.), ('2022-08-02', 20000.), ('2022-08-03', 40000.), ('2022-08-04', 80000.)], 'bar', 'sales') as html
    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.chart([('2022-08-01', 10000.), ('2022-08-02', 20000.), ('2022-08-03', 40000.), ('2022-08-04', 80000.)], 'bar', 'sales') as html
    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.chart([('2022-08-01', 10000.), ('2022-08-02', 20000.), ('2022-08-03', 40000.), ('2022-08-04', 80000.)], 'bar', 'sales') as html
    ```


<a href="../assets/images/chart.png"><img alt="screenshot" src="../assets/images/chart.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---


### levenshtein
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/levenshtein.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
levenshtein(string1, string2)
```

**Description**

Computes levenshtein distance between `string1` and `string2`

**Examples**








=== "EU"

    ```sql
    select bigfunctions.eu.levenshtein('bak', 'book') as distance
    ```


=== "US"

    ```sql
    select bigfunctions.us.levenshtein('bak', 'book') as distance
    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.levenshtein('bak', 'book') as distance
    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.levenshtein('bak', 'book') as distance
    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
+-------------+
| distance    |
+-------------+
| 2           |
+-------------+

</code>
</pre>







---


### render_string
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;"><a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/render_string.yaml" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
render_string(template, context)
```

**Description**

Render template with context json object using nunjucks.js templating library

**Examples**








=== "EU"

    ```sql
    select bigfunctions.eu.render_string('Hello {{ username }}', '{"username": "James"}') as rendered_content
    ```


=== "US"

    ```sql
    select bigfunctions.us.render_string('Hello {{ username }}', '{"username": "James"}') as rendered_content
    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.render_string('Hello {{ username }}', '{"username": "James"}') as rendered_content
    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.render_string('Hello {{ username }}', '{"username": "James"}') as rendered_content
    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
+------------------+
| rendered_content |
+------------------+
| Hello James      |
+------------------+

</code>
</pre>







---