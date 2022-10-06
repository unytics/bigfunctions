---
hide:
  - navigation
---

## 📄 Overview

BigFunctions are public BigQuery routines that give you **super-SQL-powers** in BigQuery 💪.

!!! note ""



    

    **👀 Explore**

    
    - [<code>explore_column(fully_qualified_column)</code>](#explore_column): Show column statistics
    
    - [<code>explore_dataset(fully_qualified_dataset)</code>](#explore_dataset): Shows infos about dataset tables
    
    - [<code>explore_table(fully_qualified_table)</code>](#explore_table): Show table infos and column statistics
    

    

    **✨ Transform string**

    
    - [<code>levenshtein(string1, string2)</code>](#levenshtein): Computes levenshtein distance between `string1` and `string2`
    
    - [<code>render_string(template, context)</code>](#render_string): Render template with context using nunjucks.js templating library
    
    - [<code>sentiment_score(content)</code>](#sentiment_score): Compute sentiment score of text
    

    

    **📆 Transform date**

    
    - [<code>is_public_holiday(date, country_code)</code>](#is_public_holiday): Returns true if `date` corresponds to a public holiday in `country_code`
    

    

    **🌐 Graph**

    
    - [<code>connected_components(fully_qualified_table)</code>](#connected_components): Compute the connected components of a non-directed graph.
    

    

    **💬 Notify**

    
    - [<code>notify_gmail(recipients, subject, body, attachment_filename, attachment_content)</code>](#notify_gmail): Send email via gmail
    

    

    **🚀 Export**

    
    - [<code>export_to_gmail(table_or_view_or_query, recipients, email_subject, email_body)</code>](#export_to_gmail): Send email (via gmail) with data attached as excel file
    

    

    **🔨 Utils**

    
    - [<code>chart(data, chart_type, ylabel)</code>](#chart): Returns html with a chartjs chart
    
    - [<code>dump_to_excel(data)</code>](#dump_to_excel): Dump data to excel file returned as base64
    
    - [<code>get_table_columns(fully_qualified_table)</code>](#get_table_columns): Get the column information of the given table from `INFORMATION_SCHEMA.COLUMNS`
    

    

    **🔴 Before using see --> [Getting Started](/bigfunctions/getting_started/)**






<div style="margin-top: 6rem;"></div>


## 👀 Explore

!!! note ""
    **Explore data within BigQuery console **

    Make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.

---



### explore_column
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_column.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_column(fully_qualified_column)
```

**Description**

Show column statistics

**Examples**






=== "US"

    ```sql
    call bigfunctions.us.explore_column("bigquery-public-data.samples.natality.weight_pounds");
    select html from bigfunction_result;
    ```





<a href="../assets/images/explore_column.png"><img alt="screenshot" src="../assets/images/explore_column.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---




### explore_dataset
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_dataset.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_dataset(fully_qualified_dataset)
```

**Description**

Shows infos about dataset tables

**Examples**






=== "US"

    ```sql
    call bigfunctions.us.explore_dataset("bigquery-public-data.samples");
    select html from bigfunction_result;
    ```





<a href="../assets/images/explore_dataset.png"><img alt="screenshot" src="../assets/images/explore_dataset.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---




### explore_table
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/explore_table.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
explore_table(fully_qualified_table)
```

**Description**

Show table infos and column statistics

**Examples**






=== "US"

    ```sql
    call bigfunctions.us.explore_table("bigquery-public-data.samples.natality");
    select html from bigfunction_result;
    ```





<a href="../assets/images/explore_column.png"><img alt="screenshot" src="../assets/images/explore_column.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>



---









<div style="margin-top: 6rem;"></div>


## ✨ Transform string

!!! note ""
    **Transform data creatively **

    Be amazed with your new SQL powers.

---



### levenshtein
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/levenshtein.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
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
<code style="padding-top: 0px; padding-bottom: 0px;">+----------+
| distance |
+----------+
| 2        |
+----------+
</code>
</pre>







---




### render_string
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/render_string.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
render_string(template, context)
```

**Description**

Render template with context using nunjucks.js templating library

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
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| rendered_content |
+------------------+
| Hello James      |
+------------------+
</code>
</pre>







---




### sentiment_score
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/sentiment_score.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
sentiment_score(content)
```

**Description**

Compute sentiment score of text

**Examples**






=== "EU"

    ```sql
    select bigfunctions.eu.sentiment_score('BigFunctions Rock!') as sentiment_score

    ```


=== "US"

    ```sql
    select bigfunctions.us.sentiment_score('BigFunctions Rock!') as sentiment_score

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.sentiment_score('BigFunctions Rock!') as sentiment_score

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.sentiment_score('BigFunctions Rock!') as sentiment_score

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------+
| sentiment_score |
+-----------------+
| 0.945           |
+-----------------+
</code>
</pre>







---









<div style="margin-top: 6rem;"></div>


## 📆 Transform date

!!! note ""
    **Transform data creatively **

    Be amazed with your new SQL powers.

---



### is_public_holiday
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/is_public_holiday.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
is_public_holiday(date, country_code)
```

**Description**

Returns true if `date` corresponds to a public holiday in `country_code`

- Always return `false` if date is not between year 1974 and year 2076.
- `country_code` must be among `[AO, AR, AW, AU, AT, AZ, BD, BY, BE, BO, BW, BR, BG, BI, CA, CL, CN, CO, HR, CU, CW, CY, CZ, DK, DJ, DO, EG, EE, ET, FI, FR, GE, DE, GR, HN, HK, HU, IS, IN, IE, IL, IT, JM, JP, KZ, KE, KR, LV, LS, LT, LU, MG, MW, MY, MT, MX, MD, MA, MZ, NA, NL, NZ, NI, NG, MK, NO, PY, PE, PL, PT, RO, RU, SA, RS, SG, SK, SI, ZA, ES, SZ, SE, CH, TW, TN, TR, UA, AE, GB, US, UY, UZ, VE, VN, ZM, ZW]`
- Holiday dates come from <a href="https://python-holidays.readthedocs.io/" target="_blank">`python-holidays`</a>.


**Examples**






=== "EU"

    ```sql
    select bigfunctions.eu.is_public_holiday(date('2022-07-14'), 'FR') as is_public_holiday

    ```


=== "US"

    ```sql
    select bigfunctions.us.is_public_holiday(date('2022-07-14'), 'FR') as is_public_holiday

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.is_public_holiday(date('2022-07-14'), 'FR') as is_public_holiday

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.is_public_holiday(date('2022-07-14'), 'FR') as is_public_holiday

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-------------------+
| is_public_holiday |
+-------------------+
| true              |
+-------------------+
</code>
</pre>







---









<div style="margin-top: 6rem;"></div>


## 🌐 Graph

!!! note ""
    **Graph Algorithms **

    No need for neo4j nor spark graphframes --> go BigQuery boosted by BigFunctions!

---



### connected_components
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/furcy-pin-3790b028/" title="Author: Furcy Pin" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4D03AQFK5YDJyod_3A/profile-displayphoto-shrink_200_200/0/1590431668428?e=1670457600&v=beta&t=f0Fd9bV-sSssoLBQ2R03WgEUvP52gdBLv120z-Q-OGc" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/connected_components.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
connected_components(fully_qualified_table)
```

**Description**

Compute the connected components of a non-directed graph.

Given a table with two columns of the same type STRING or INTEGER representing the edges of a graph,
this computes a new temporary table called `bigfunction_result` containing two columns of the same type
named `node_id` and `connected_component_id`.

This is an implementation of the Alternating Algorithm (large-star, small-star) described in the 2014 paper
"Connected Components in MapReduce and Beyond" written by {rkiveris, silviol, mirrokni, rvibhor, sergeiv} @google.com

PERFORMANCE AND COST CONSIDERATIONS

- This algorithm has been proved to converge in O(log(n)²) and is conjectured to converge in O(log(n)), where n
is the number of nodes in the graph. It was the most performant known distributed connected component algorithm
last time I checked (in 2017).
- This implementation persists temporary results at each iteration loop: for the BigQuery pricing, you should
be expecting it to cost the equivalent of 15 to 30 scans on your input table. Since the input table has only
two columns, this should be reasonable, and we recommend using INTEGER columns rather than STRING when possible.
- If your graph contains nodes with a very high number of neighbors, the algorithm may crash. It is recommended
to apply a pre-filtering on your nodes and remove nodes with a pathologically high cardinality.
You should also monitor actively the number of nodes filtered this way and their cardinality, as this could help
you detect a data quality deterioration in your input graph.
If the input graph contains duplicate edges, they will be automatically removed by the algorithm.

ISOLATED NODES: If you want to have isolated nodes (nodes that have no neighbors)
in the resulting graph, there is two possible ways to achieve this:

- Add self-loops edges to all your nodes in your input graph (it also works if you add edges between all the graph
   nodes and a fictitious node with id NULL)
- Only add edges between distinct nodes to your input, and perform a join between your input graph and the
   algorithm's output to find all the nodes that have disappeared. These will be the isolated nodes.
   This second method requires a little more work but it should also be cheaper.


**Examples**






=== "EU"

    ```sql
    call bigfunctions.eu.connected_components(bigfunctions.eu.test_connected_components_input_1);
    
    ```









---









<div style="margin-top: 6rem;"></div>


## 💬 Notify

!!! note ""
    **Send infos to your customers, alert the operations teams, send reportings to business **

    Spread the word to the world!

---



### notify_gmail
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/notify_gmail.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
notify_gmail(recipients, subject, body, attachment_filename, attachment_content)
```

**Description**

Send email via gmail

**Examples**



<span style="color: var(--md-typeset-a-color);">1. Send email without file attached</span>


=== "EU"

    ```sql
    select bigfunctions.eu.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null) as success

    ```


=== "US"

    ```sql
    select bigfunctions.us.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null) as success

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null) as success

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null) as success

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------+
| success |
+---------+
| true    |
+---------+
</code>
</pre>






<span style="color: var(--md-typeset-a-color);">2. Send email with plain text file attached</span>


=== "EU"

    ```sql
    select bigfunctions.eu.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4') as success

    ```


=== "US"

    ```sql
    select bigfunctions.us.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4') as success

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4') as success

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4') as success

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------+
| success |
+---------+
| true    |
+---------+
</code>
</pre>






<span style="color: var(--md-typeset-a-color);">3. Send email with excel file attached</span>


=== "EU"

    ```sql
    select bigfunctions.eu.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select bigfunctions.eu.dump_to_excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]'))) as success

    ```


=== "US"

    ```sql
    select bigfunctions.us.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select bigfunctions.us.dump_to_excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]'))) as success

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select bigfunctions.europe_west1.dump_to_excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]'))) as success

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.notify_gmail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select bigfunctions.your_region2.dump_to_excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]'))) as success

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------+
| success |
+---------+
| true    |
+---------+
</code>
</pre>







---









<div style="margin-top: 6rem;"></div>


## 🚀 Export

!!! note ""
    **Get the data out to the outside world **

    Make BigQuery as the golden source of all your SAAS and for all your usages

---



### export_to_gmail
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/export_to_gmail.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
export_to_gmail(table_or_view_or_query, recipients, email_subject, email_body)
```

**Description**

Send email (via gmail) with data attached as excel file

**Examples**






=== "EU"

    ```sql
    call bigfunctions.eu.export_to_gmail('bigfunctions.samples.natality', 'contact@unytics.io', 'Finance Figures for Today', 'Hey Paul, you fill find the figures in the attached excel file. Enjoy 🔥');
    
    ```









---









<div style="margin-top: 6rem;"></div>


## 🔨 Utils

!!! note ""
    **Utils BigFunctions **

    

---



### chart
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/chart.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
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




### dump_to_excel
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4E03AQF92ENRMYC3Mw/profile-displayphoto-shrink_200_200/0/1656924490995?e=1670457600&v=beta&t=JDu8feKR5-bKs4xbHdmsiatSwOgE2BY31KHJcVHhUYI" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/dump_to_excel.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
dump_to_excel(data)
```

**Description**

Dump data to excel file returned as base64

**Examples**






=== "EU"

    ```sql
    select bigfunctions.eu.dump_to_excel('[{"col1": "row1", "col2": 1}, {"col1": "row2", "col2": 2}]') as excel_base64

    ```


=== "US"

    ```sql
    select bigfunctions.us.dump_to_excel('[{"col1": "row1", "col2": 1}, {"col1": "row2", "col2": 2}]') as excel_base64

    ```


=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.dump_to_excel('[{"col1": "row1", "col2": 1}, {"col1": "row2", "col2": 2}]') as excel_base64

    ```


=== "your-region2"

    ```sql
    select bigfunctions.your_region2.dump_to_excel('[{"col1": "row1", "col2": 1}, {"col1": "row2", "col2": 2}]') as excel_base64

    ```





<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| excel_base64     |
+------------------+
| UEsDBBQAAAAAA... |
+------------------+
</code>
</pre>







---




### get_table_columns
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/furcy-pin-3790b028/" title="Author: Furcy Pin" target="_blank">
    <img src="https://media-exp1.licdn.com/dms/image/C4D03AQFK5YDJyod_3A/profile-displayphoto-shrink_200_200/0/1590431668428?e=1670457600&v=beta&t=f0Fd9bV-sSssoLBQ2R03WgEUvP52gdBLv120z-Q-OGc" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/get_table_columns.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>
```
get_table_columns(fully_qualified_table)
```

**Description**

Get the column information of the given table from `INFORMATION_SCHEMA.COLUMNS`
and put them in a temporary table called `bigfunction_result`.


**Examples**



<span style="color: var(--md-typeset-a-color);">1. call `bigfunctions.eu._get_columns`("bigfunctions.samples.natality");
select column_name, data_type from bigfunction_result ;
</span>


=== "EU"

    ```sql
    call bigfunctions.eu.get_table_columns('bigfunctions.samples.natality');
    
    ```









---






