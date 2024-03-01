---
title: "remove_value"
description: "BigFunction remove_value: Return an array with all values except `value`."
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > remove_value
</span>

# remove_value


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/company/esmoz/" title="Author: Sid Ali" target="_blank">
    <img src="https://esmoz.fr/wp-content/uploads/2022/03/logo_esmoz_40x20-1.png" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/remove_value.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
remove_value(arr, value)
```

**Description**

Return an array with all values except `value`.





**Examples**













=== "EU"

    ```sql
    select bigfunctions.eu.remove_value([1, 4, 3, 8], 4)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.remove_value([1, 4, 3, 8], 4)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.remove_value([1, 4, 3, 8], 4)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------+
| arr       |
+-----------+
| [1, 3, 8] |
+-----------+
</code>
</pre>









