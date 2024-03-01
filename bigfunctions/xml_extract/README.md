---
title: "xml_extract"
description: "BigFunction xml_extract: Returns content extracted from XML from given XPATH"
---

<a style="color: gray; position: relative; top: -1rem" href="..">BigFunctions </a> / 

# xml_extract


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="xml_extract.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
xml_extract(xml, x_path)
```

**Description**

Returns content extracted from XML from given XPATH





**Examples**



<span style="color: var(--md-typeset-a-color);">1. Only one element for the xpath</span>









=== "EU"

    ```sql
    select bigfunctions.eu.xml_extract("<customer><name>John Doe</name></customer>", "/customer/name")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.xml_extract("<customer><name>John Doe</name></customer>", "/customer/name")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.xml_extract("<customer><name>John Doe</name></customer>", "/customer/name")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------+
| extracted_value |
+-----------------+
| [&#34;John Doe&#34;]    |
+-----------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. Multiple elements for the xpath</span>









=== "EU"

    ```sql
    select bigfunctions.eu.xml_extract("<customer><name>John Doe</name><name>Jane Doe</name></customer>", "/customer/name")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.xml_extract("<customer><name>John Doe</name><name>Jane Doe</name></customer>", "/customer/name")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.xml_extract("<customer><name>John Doe</name><name>Jane Doe</name></customer>", "/customer/name")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+--------------------------+
| extracted_value          |
+--------------------------+
| [&#34;John Doe&#34;, &#34;Jane Doe&#34;] |
+--------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">3. Incorrect xpath</span>









=== "EU"

    ```sql
    select bigfunctions.eu.xml_extract("<customer><name>John Doe</name></customer>", "/customer/na")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.xml_extract("<customer><name>John Doe</name></customer>", "/customer/na")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.xml_extract("<customer><name>John Doe</name></customer>", "/customer/na")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------+
| extracted_value |
+-----------------+
| null            |
+-----------------+
</code>
</pre>









