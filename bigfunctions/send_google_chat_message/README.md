---
title: "send_google_chat_message"
description: "BigFunction send_google_chat_message: Sends `message` to google chat space
using incoming webhook.


> To get the incoming `webhook_url`:
>
> - In a web browser, open Google Chat.
> - Go to the space to which you want to add a webhook.
> - At the top, next to space title, click Down Arrow arrow_drop_down > Apps & integrations.
> - Click Manage webhooks.
> - If this space already has other webhooks, click Add another. Otherwise, skip this step.
> - For Name, enter "Quickstart Webhook".
> - For Avatar URL, enter https://developers.google.com/chat/images/chat-product-icon.png.
> - Click SAVE.
> - To copy the full webhook URL, click Copy.
"
---

<span style="color: gray; position: relative; top: -1rem">
  <a href=".." style="color: gray">bigfunctions </a> ＞ send_google_chat_message
</span>

# send_google_chat_message


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/send_google_chat_message.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
send_google_chat_message(message, webhook_url)
```

**Description**

Sends `message` to google chat space
using incoming webhook.


> To get the incoming `webhook_url`:
>
> - In a web browser, open Google Chat.
> - Go to the space to which you want to add a webhook.
> - At the top, next to space title, click Down Arrow arrow_drop_down > Apps & integrations.
> - Click Manage webhooks.
> - If this space already has other webhooks, click Add another. Otherwise, skip this step.
> - For Name, enter "Quickstart Webhook".
> - For Avatar URL, enter https://developers.google.com/chat/images/chat-product-icon.png.
> - Click SAVE.
> - To copy the full webhook URL, click Copy.






**Examples**













=== "EU"

    ```sql
    select bigfunctions.eu.send_google_chat_message("Hello 👋 from bigfunctions!", "YOUR_WEBHOOK_URL")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.send_google_chat_message("Hello 👋 from bigfunctions!", "YOUR_WEBHOOK_URL")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.send_google_chat_message("Hello 👋 from bigfunctions!", "YOUR_WEBHOOK_URL")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+--------------------------------------------------------------------------------------------------+
| response                                                                                         |
+--------------------------------------------------------------------------------------------------+
| {
  &#34;name&#34;: ...,
  &#34;sender&#34;: ...,
  &#34;createTime&#34;: ...,
  &#34;text&#34;: &#34;Hello 👋 from bigfunctions!&#34;
}
 |
+--------------------------------------------------------------------------------------------------+
</code>
</pre>









