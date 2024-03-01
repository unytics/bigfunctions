---
title: "send_mail_with_excel"
description: "BigFunction send_mail_with_excel: Sends an email with `table_or_view_or_query` data attached as excel file
(only the first 1000 rows will be copied to the excel file)

> This function calls `json2excel` and `send_mail` functions.

| Param      | Possible values  |
|------------|------------------|
| `to     `  | One or multiple comma separated emails.<br>For instance `contact@unytics.io` or `contact@unytics.io, paul.marcombes@unytics.io`   |
| `subject`  | Email subject |
| `content`  | Can be plain text, html or **markdown**   |
| `attachment_filename`  | filename with extension such as `report.xlsx`  |
| `table_or_view_or_query`  | A fully qualified table or view you have permission to read or a sql query starting with `select`  |
"
---

<a style="color: gray; position: relative; top: -1rem" href="..">BigFunctions </a> / 

# send_mail_with_excel


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://lh3.googleusercontent.com/a-/ACB-R5RDf2yxcw1p_IYLCKmiUIScreatDdhG8B83om6Ohw=s260" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="send_mail_with_excel.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
send_mail_with_excel(to, subject, content, excel_filename, table_or_view_or_query)
```

**Description**

Sends an email with `table_or_view_or_query` data attached as excel file
(only the first 1000 rows will be copied to the excel file)

> This function calls `json2excel` and `send_mail` functions.

| Param      | Possible values  |
|------------|------------------|
| `to     `  | One or multiple comma separated emails.<br>For instance `contact@unytics.io` or `contact@unytics.io, paul.marcombes@unytics.io`   |
| `subject`  | Email subject |
| `content`  | Can be plain text, html or **markdown**   |
| `attachment_filename`  | filename with extension such as `report.xlsx`  |
| `table_or_view_or_query`  | A fully qualified table or view you have permission to read or a sql query starting with `select`  |






**Examples**













=== "EU"

    ```sql
    call bigfunctions.eu.send_mail_with_excel(
      'contact@unytics.io', 
      'Financial Report', 
      '''
      # Monthly Report from BigQuery
      
      ## KPIs
      
      - **MRR**: 32,343 USD
      - **Churn**: 4.2 %
      - **Subscriptions**: +3452
      ''', 
      'report.xlsx', 
      'eu.sales');
    
    ```




=== "US"

    ```sql
    call bigfunctions.us.send_mail_with_excel(
      'contact@unytics.io', 
      'Financial Report', 
      '''
      # Monthly Report from BigQuery
      
      ## KPIs
      
      - **MRR**: 32,343 USD
      - **Churn**: 4.2 %
      - **Subscriptions**: +3452
      ''', 
      'report.xlsx', 
      'us.sales');
    
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.send_mail_with_excel(
      'contact@unytics.io', 
      'Financial Report', 
      '''
      # Monthly Report from BigQuery
      
      ## KPIs
      
      - **MRR**: 32,343 USD
      - **Churn**: 4.2 %
      - **Subscriptions**: +3452
      ''', 
      'report.xlsx', 
      'europe_west1.sales');
    
    ```












<a href="send_mail_with_excel.png"><img alt="screenshot" src="send_mail_with_excel.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>


