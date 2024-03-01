---
title: "phone_number_info"
description: "BigFunction phone_number_info: Get `phone_number` info
such as:

- `country`,
- `isValid`,
- etc

using [libphonenumber-js library](https://www.npmjs.com/package/libphonenumber-js).

Argument `options` can be `null` or must be a json with the following keys:
`defaultCountry`, `defaultCallingCode` and `extract` as described in the
[library documentation](https://www.npmjs.com/package/libphonenumber-js#parsephonenumberstring-defaultcountry-string--options-object-phonenumber).
"
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > phone_number_info
</span>

# phone_number_info


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://lh3.googleusercontent.com/a-/ACB-R5RDf2yxcw1p_IYLCKmiUIScreatDdhG8B83om6Ohw=s260" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/phone_number_info.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
phone_number_info(phone_number, options)
```

**Description**

Get `phone_number` info
such as:

- `country`,
- `isValid`,
- etc

using [libphonenumber-js library](https://www.npmjs.com/package/libphonenumber-js).

Argument `options` can be `null` or must be a json with the following keys:
`defaultCountry`, `defaultCallingCode` and `extract` as described in the
[library documentation](https://www.npmjs.com/package/libphonenumber-js#parsephonenumberstring-defaultcountry-string--options-object-phonenumber).






**Examples**



<span style="color: var(--md-typeset-a-color);">1. Get info about an international `phone_number` (starting with `+`)</span>









=== "EU"

    ```sql
    select bigfunctions.eu.phone_number_info('+33123456789', null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.phone_number_info('+33123456789', null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.phone_number_info('+33123456789', null)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| info                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {
  &#34;isPossible&#34;: true,
  &#34;isValid&#34;: true,
  &#34;parseError&#34;: null,
  &#34;country&#34;: &#34;FR&#34;,
  &#34;countryCallingCode&#34;: &#34;33&#34;,
  &#34;formattedInternational&#34;: &#34;+33 1 23 45 67 89&#34;,
  &#34;formattedNational&#34;: &#34;01 23 45 67 89&#34;,
  &#34;isNonGeographic&#34;: false,
  &#34;nationalNumber&#34;: &#34;123456789&#34;,
  &#34;number&#34;: &#34;+33123456789&#34;,
  &#34;possibleCountries&#34;: [&#34;FR&#34;],
  &#34;type&#34;: &#34;FIXED_LINE&#34;,
  &#34;uri&#34;: &#34;tel:+33123456789&#34;
}
 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. Get info about a national `phone_number`</span>









=== "EU"

    ```sql
    select bigfunctions.eu.phone_number_info('0123456789', json '{"defaultCountry": "FR"}')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.phone_number_info('0123456789', json '{"defaultCountry": "FR"}')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.phone_number_info('0123456789', json '{"defaultCountry": "FR"}')
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| info                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {
  &#34;isPossible&#34;: true,
  &#34;isValid&#34;: true,
  &#34;parseError&#34;: null,
  &#34;country&#34;: &#34;FR&#34;,
  &#34;countryCallingCode&#34;: &#34;33&#34;,
  &#34;formattedInternational&#34;: &#34;+33 1 23 45 67 89&#34;,
  &#34;formattedNational&#34;: &#34;01 23 45 67 89&#34;,
  &#34;isNonGeographic&#34;: false,
  &#34;nationalNumber&#34;: &#34;123456789&#34;,
  &#34;number&#34;: &#34;+33123456789&#34;,
  &#34;possibleCountries&#34;: [&#34;FR&#34;],
  &#34;type&#34;: &#34;FIXED_LINE&#34;,
  &#34;uri&#34;: &#34;tel:+33123456789&#34;
}
 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">3. If no phone number is found in `phone_number` argument, a reason in given in `parseError`</span>









=== "EU"

    ```sql
    select bigfunctions.eu.phone_number_info('Hello!', null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.phone_number_info('Hello!', null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.phone_number_info('Hello!', null)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| info                                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {
  &#34;isPossible&#34;: false,
  &#34;isValid&#34;: false,
  &#34;parseError&#34;: &#34;NOT_A_NUMBER&#34;,
  &#34;country&#34;: null,
  &#34;countryCallingCode&#34;: null,
  &#34;formattedInternational&#34;: null,
  &#34;formattedNational&#34;: null,
  &#34;isNonGeographic&#34;: null,
  &#34;nationalNumber&#34;: null,
  &#34;number&#34;: null,
  &#34;possibleCountries&#34;: null,
  &#34;type&#34;: null,
  &#34;uri&#34;: null,
}
 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">4. By default, if the given `phone_number` text contains a phone number among other text, it will be extracted.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.phone_number_info('Hello +33123456789 !', null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.phone_number_info('Hello +33123456789 !', null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.phone_number_info('Hello +33123456789 !', null)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| info                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {
  &#34;isPossible&#34;: true,
  &#34;isValid&#34;: true,
  &#34;parseError&#34;: null,
  &#34;country&#34;: &#34;FR&#34;,
  &#34;countryCallingCode&#34;: &#34;33&#34;,
  &#34;formattedInternational&#34;: &#34;+33 1 23 45 67 89&#34;,
  &#34;formattedNational&#34;: &#34;01 23 45 67 89&#34;,
  &#34;isNonGeographic&#34;: false,
  &#34;nationalNumber&#34;: &#34;123456789&#34;,
  &#34;number&#34;: &#34;+33123456789&#34;,
  &#34;possibleCountries&#34;: [&#34;FR&#34;],
  &#34;type&#34;: &#34;FIXED_LINE&#34;,
  &#34;uri&#34;: &#34;tel:+33123456789&#34;
}
 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">5. To consider that `phone_number` cannot have additional text use `extract:  false` as option</span>









=== "EU"

    ```sql
    select bigfunctions.eu.phone_number_info('Hello +33123456789 !', json '{"extract": false}')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.phone_number_info('Hello +33123456789 !', json '{"extract": false}')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.phone_number_info('Hello +33123456789 !', json '{"extract": false}')
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| info                                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {
  &#34;isPossible&#34;: false,
  &#34;isValid&#34;: false,
  &#34;parseError&#34;: &#34;NOT_A_NUMBER&#34;,
  &#34;country&#34;: null,
  &#34;countryCallingCode&#34;: null,
  &#34;formattedInternational&#34;: null,
  &#34;formattedNational&#34;: null,
  &#34;isNonGeographic&#34;: null,
  &#34;nationalNumber&#34;: null,
  &#34;number&#34;: null,
  &#34;possibleCountries&#34;: null,
  &#34;type&#34;: null,
  &#34;uri&#34;: null,
}
 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
</code>
</pre>









