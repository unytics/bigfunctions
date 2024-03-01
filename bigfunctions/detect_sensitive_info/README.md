---
title: "detect_sensitive_info"
description: "BigFunction detect_sensitive_info: Detect sensitive information in `text`
using [Cloud Data Loss Prevention](https://cloud.google.com/dlp)
"
---

<span style="color: gray; position: relative; top: -1rem">
  <a href=".." style="color: gray">bigfunctions </a> ＞ detect_sensitive_info
</span>

# detect_sensitive_info


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/detect_sensitive_info.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
detect_sensitive_info(text)
```

**Description**

Detect sensitive information in `text`
using [Cloud Data Loss Prevention](https://cloud.google.com/dlp)






**Examples**



<span style="color: var(--md-typeset-a-color);">1. String with email in it.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.detect_sensitive_info("My email is shivam@google.co.in")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.detect_sensitive_info("My email is shivam@google.co.in")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.detect_sensitive_info("My email is shivam@google.co.in")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensitive_info                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [{&#34;string&#34;: &#34;shivam&#34;, &#34;info_type&#34;: &#34;PERSON_NAME&#34;, &#34;confidence&#34;: &#34;POSSIBLE&#34;}, {&#34;string&#34;: &#34;shivam&#34;, &#34;info_type&#34;: &#34;FIRST_NAME&#34;, &#34;confidence&#34;: &#34;POSSIBLE&#34;}, {&#34;string&#34;: &#34;shivam&#34;, &#34;info_type&#34;: &#34;FEMALE_NAME&#34;, &#34;confidence&#34;: &#34;POSSIBLE&#34;}, {&#34;string&#34;: &#34;shivam&#34;, &#34;info_type&#34;: &#34;MALE_NAME&#34;, &#34;confidence&#34;: &#34;POSSIBLE&#34;}, {&#34;string&#34;: &#34;google&#34;, &#34;info_type&#34;: &#34;ORGANIZATION_NAME&#34;, &#34;confidence&#34;: &#34;POSSIBLE&#34;}, {&#34;string&#34;: &#34;shivam@google.co.in&#34;, &#34;info_type&#34;: &#34;EMAIL_ADDRESS&#34;, &#34;confidence&#34;: &#34;VERY_LIKELY&#34;}, {&#34;string&#34;: &#34;google.co.in&#34;, &#34;info_type&#34;: &#34;DOMAIN_NAME&#34;, &#34;confidence&#34;: &#34;LIKELY&#34;}] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. String with phone number in it.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.detect_sensitive_info("My phone number is 0123456789")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.detect_sensitive_info("My phone number is 0123456789")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.detect_sensitive_info("My phone number is 0123456789")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------------------------------------------------------------------------------+
| sensitive_info                                                                  |
+---------------------------------------------------------------------------------+
| [{&#34;string&#34;: &#34;0123456789&#34;, &#34;info_type&#34;: &#34;PHONE_NUMBER&#34;, &#34;confidence&#34;: &#34;LIKELY&#34;}] |
+---------------------------------------------------------------------------------+
</code>
</pre>









