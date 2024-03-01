---
title: "send_mail"
description: "BigFunction send_mail: Sends an email
to `to` email with `subject`, `content` and possible attachment (defined by `attachment_filename` and `attachment_content`).

| Param      | Possible values  |
|------------|------------------|
| `to     `  | One or multiple comma separated emails.<br>For instance `contact@unytics.io` or `contact@unytics.io, paul.marcombes@unytics.io`   |
| `subject`  | Email subject |
| `content`  | Can be plain text, html or **markdown**   |
| `attachment_filename`  | `null` or filename with extension such as `report.xlsx`  |
| `attachment_content`  | `null` or can be plain text or base64 encoded content (useful to send excel files, pdf or images)  |

> This function uses [SendGrid](https://sendgrid.com/) to send the emails and [Lee Munroe HTML template](https://github.com/leemunroe/responsive-html-email-template) for styling emails.
"
---

<a style="color: gray; position: relative; top: -1rem" href="..">BigFunctions </a> / 

# send_mail


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/guillaume-pivette/" title="Author: Guillaume Pivette from Neoxia" target="_blank">
    <img src="https://cdn-images-1.medium.com/v2/resize:fit:92/1*jHdQzX82eU5lyjBYp63NqQ@2x.png" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="send_mail.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
send_mail(to, subject, content, attachment_filename, attachment_content)
```

**Description**

Sends an email
to `to` email with `subject`, `content` and possible attachment (defined by `attachment_filename` and `attachment_content`).

| Param      | Possible values  |
|------------|------------------|
| `to     `  | One or multiple comma separated emails.<br>For instance `contact@unytics.io` or `contact@unytics.io, paul.marcombes@unytics.io`   |
| `subject`  | Email subject |
| `content`  | Can be plain text, html or **markdown**   |
| `attachment_filename`  | `null` or filename with extension such as `report.xlsx`  |
| `attachment_content`  | `null` or can be plain text or base64 encoded content (useful to send excel files, pdf or images)  |

> This function uses [SendGrid](https://sendgrid.com/) to send the emails and [Lee Munroe HTML template](https://github.com/leemunroe/responsive-html-email-template) for styling emails.






**Examples**



<span style="color: var(--md-typeset-a-color);">1. Send email without file attached</span>









=== "EU"

    ```sql
    select bigfunctions.eu.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', null, null)
    
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
    select bigfunctions.eu.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.csv', 'col1,col2\nval1,val2\nval3,val4')
    
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
    select bigfunctions.eu.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select eu.json2excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]')))
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select us.json2excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]')))
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.send_mail('contact@unytics.io', 'I love BigFunctions', 'Hey Paul, could you deploy more BigFunctions 🙏?', 'report.xlsx', (select europe_west1.json2excel('[{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]')))
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------+
| success |
+---------+
| true    |
+---------+
</code>
</pre>









