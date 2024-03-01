---
title: "ip2continent_name"
description: "BigFunction ip2continent_name: Get `continent` of `ip`

> This functions uses IP address data powered by [IPinfo](https://ipinfo.io)
> and released under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
> You are required to attribute IPinfo to use their free datasets.
> The attribution requirements can be met by giving their service credit as your data source.
> Simply place a link to IPinfo on the website, application, or social media account that uses their data.
"
---

<span>style="color: gray; position: relative; top: -1rem"><a href="..">BigFunctions </a> / ip2continent_name</span>

# ip2continent_name


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://lh3.googleusercontent.com/a-/ACB-R5RDf2yxcw1p_IYLCKmiUIScreatDdhG8B83om6Ohw=s260" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="ip2continent_name.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
ip2continent_name(ip)
```

**Description**

Get `continent` of `ip`

> This functions uses IP address data powered by [IPinfo](https://ipinfo.io)
> and released under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
> You are required to attribute IPinfo to use their free datasets.
> The attribution requirements can be met by giving their service credit as your data source.
> Simply place a link to IPinfo on the website, application, or social media account that uses their data.






**Examples**













=== "EU"

    ```sql
    select bigfunctions.eu.ip2continent_name('152.216.7.110')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.ip2continent_name('152.216.7.110')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.ip2continent_name('152.216.7.110')
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------------+
| continent     |
+---------------+
| North America |
+---------------+
</code>
</pre>









