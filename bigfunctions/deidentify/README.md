---
title: "deidentify"
description: "BigFunction deidentify: Masks sensitive information of type `info_types` in `text`
using [Cloud Data Loss Prevention](https://cloud.google.com/dlp)

| Param  | Possible values (can be one or any combination of the following values separated by comma)  |
|---|---|
| `info_types` | `ADVERTISING_ID`, `AGE`, `AUTH_TOKEN`, `AWS_CREDENTIALS`, `AZURE_AUTH_TOKEN`, `BASIC_AUTH_HEADER`, `CREDIT_CARD_NUMBER`, `CREDIT_CARD_TRACK_NUMBER`, `DATE`, `DATE_OF_BIRTH`, `DOMAIN_NAME`, `EMAIL_ADDRESS`, `ENCRYPTION_KEY`, `ETHNIC_GROUP`, `FEMALE_NAME`, `FIRST_NAME`, `GCP_API_KEY`, `GCP_CREDENTIALS`, `GENDER`, `GENERIC_ID`, `HTTP_COOKIE`, `HTTP_COOKIE`, `IBAN_CODE`, `ICCID_NUMBER`, `ICD10_CODE`, `ICD9_CODE`, `IMEI_HARDWARE_ID`, `IMSI_ID`, `IP_ADDRESS`, `JSON_WEB_TOKEN`, `LAST_NAME`, `LOCATION`, `LOCATION_COORDINATES`, `MAC_ADDRESS`, `MAC_ADDRESS_LOCAL`, `MALE_NAME`, `MARITAL_STATUS`, `MEDICAL_RECORD_NUMBER`, `MEDICAL_TERM`, `OAUTH_CLIENT_SECRET`, `ORGANIZATION_NAME`, `PASSPORT`, `PASSWORD`, `PERSON_NAME`, `PHONE_NUMBER`, `SSL_CERTIFICATE`, `STORAGE_SIGNED_POLICY_DOCUMENT`, `STORAGE_SIGNED_URL`, `STREET_ADDRESS`, `SWIFT_CODE`, `TIME`, `URL`, `VAT_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`, `WEAK_PASSWORD_HASH`, `XSRF_TOKEN` |
"
---

<span>style="color: gray; position: relative; top: -1rem"><a href="..">BigFunctions </a> / deidentify</span>

# deidentify


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="deidentify.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
deidentify(text, info_types)
```

**Description**

Masks sensitive information of type `info_types` in `text`
using [Cloud Data Loss Prevention](https://cloud.google.com/dlp)

| Param  | Possible values (can be one or any combination of the following values separated by comma)  |
|---|---|
| `info_types` | `ADVERTISING_ID`, `AGE`, `AUTH_TOKEN`, `AWS_CREDENTIALS`, `AZURE_AUTH_TOKEN`, `BASIC_AUTH_HEADER`, `CREDIT_CARD_NUMBER`, `CREDIT_CARD_TRACK_NUMBER`, `DATE`, `DATE_OF_BIRTH`, `DOMAIN_NAME`, `EMAIL_ADDRESS`, `ENCRYPTION_KEY`, `ETHNIC_GROUP`, `FEMALE_NAME`, `FIRST_NAME`, `GCP_API_KEY`, `GCP_CREDENTIALS`, `GENDER`, `GENERIC_ID`, `HTTP_COOKIE`, `HTTP_COOKIE`, `IBAN_CODE`, `ICCID_NUMBER`, `ICD10_CODE`, `ICD9_CODE`, `IMEI_HARDWARE_ID`, `IMSI_ID`, `IP_ADDRESS`, `JSON_WEB_TOKEN`, `LAST_NAME`, `LOCATION`, `LOCATION_COORDINATES`, `MAC_ADDRESS`, `MAC_ADDRESS_LOCAL`, `MALE_NAME`, `MARITAL_STATUS`, `MEDICAL_RECORD_NUMBER`, `MEDICAL_TERM`, `OAUTH_CLIENT_SECRET`, `ORGANIZATION_NAME`, `PASSPORT`, `PASSWORD`, `PERSON_NAME`, `PHONE_NUMBER`, `SSL_CERTIFICATE`, `STORAGE_SIGNED_POLICY_DOCUMENT`, `STORAGE_SIGNED_URL`, `STREET_ADDRESS`, `SWIFT_CODE`, `TIME`, `URL`, `VAT_NUMBER`, `VEHICLE_IDENTIFICATION_NUMBER`, `WEAK_PASSWORD_HASH`, `XSRF_TOKEN` |






**Examples**



<span style="color: var(--md-typeset-a-color);">1. String with email in it.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.deidentify("My email is shivam@google.co.in", "PHONE_NUMBER, EMAIL_ADDRESS")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.deidentify("My email is shivam@google.co.in", "PHONE_NUMBER, EMAIL_ADDRESS")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.deidentify("My email is shivam@google.co.in", "PHONE_NUMBER, EMAIL_ADDRESS")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------------------+
| masked_info                 |
+-----------------------------+
| My email is [EMAIL_ADDRESS] |
+-----------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. String with phone number in it.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.deidentify("My phone number is 0123456789", "PHONE_NUMBER, email_address")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.deidentify("My phone number is 0123456789", "PHONE_NUMBER, email_address")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.deidentify("My phone number is 0123456789", "PHONE_NUMBER, email_address")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------------------------+
| masked_info                       |
+-----------------------------------+
| My phone number is [PHONE_NUMBER] |
+-----------------------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">3. If `info_types` is `null` or empty, all built-in info types may be used</span>









=== "EU"

    ```sql
    select bigfunctions.eu.deidentify("My email is shivam@google.co.in", null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.deidentify("My email is shivam@google.co.in", null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.deidentify("My email is shivam@google.co.in", null)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------------------------------+
| masked_info                              |
+------------------------------------------+
| My email is [PERSON_NAME][EMAIL_ADDRESS] |
+------------------------------------------+
</code>
</pre>









