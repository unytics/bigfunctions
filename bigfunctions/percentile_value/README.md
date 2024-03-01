---
title: "percentile_value"
description: "BigFunction percentile_value: Returns percentile of an array with percentile a float in range [0, 1].

Algorithm to calculate percentile is based on *[R. J. Hyndman and Y. Fan, "Sample quantiles in statistical packages," The American Statistician, 50(4), pp. 361-365, 1996](https://www.amherst.edu/media/view/129116/original/Sample+Quantiles.pdf)*
"
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > percentile_value
</span>

# percentile_value


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/percentile_value.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
percentile_value(arr, percentile)
```

**Description**

Returns percentile of an array with percentile a float in range [0, 1].

Algorithm to calculate percentile is based on *[R. J. Hyndman and Y. Fan, "Sample quantiles in statistical packages," The American Statistician, 50(4), pp. 361-365, 1996](https://www.amherst.edu/media/view/129116/original/Sample+Quantiles.pdf)*






**Examples**













=== "EU"

    ```sql
    select bigfunctions.eu.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3], 0.74)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3], 0.74)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3], 0.74)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| percentile_value |
+------------------+
| 13.8             |
+------------------+
</code>
</pre>



















=== "EU"

    ```sql
    select bigfunctions.eu.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 0.9)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 0.9)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 0.9)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| percentile_value |
+------------------+
| 15.9             |
+------------------+
</code>
</pre>



















=== "EU"

    ```sql
    select bigfunctions.eu.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 2)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 2)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.percentile_value([20, 16, 15, 13, 10, 9, 8, 8, 7, 6, 3, 2], 2)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| percentile_value |
+------------------+
| null             |
+------------------+
</code>
</pre>









