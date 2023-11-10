---
title: "Explore"
description: "Catalog of open-source BigFunctions"
hide:
  - navigation
---

## 📄 Overview

BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.






**🧠 AI**


- [<code>ask_bison(question)</code>](#ask_bison): Ask Anything!

- [<code>ask_my_data(question, fully_qualified_table)</code>](#ask_my_data): Ask your data any `question` in natural language.

- [<code>generate_sql(question, fully_qualified_table)</code>](#generate_sql): Transform `question` to a SQL query.




**🛢 Get data**


- [<code>exchange_rate(base, to)</code>](#exchange_rate): Get `exchange_rate`

- [<code>get(url, headers)</code>](#get): Request `url`

- [<code>get_json(url, headers)</code>](#get_json): GET json `data` from `url`

- [<code>get_meteo(latitude, longitude, date)</code>](#get_meteo): Get `meteo`

- [<code>get_webpage_metadata(url)</code>](#get_webpage_metadata): Get webpage metadata

- [<code>get_webpage_structured_data(url)</code>](#get_webpage_structured_data): Get webpage Structured Data




**💬 Notify**


- [<code>send_google_chat_message(message, webhook_url)</code>](#send_google_chat_message): Sends `message` to google chat space

- [<code>send_mail(to, subject, content, attachment_filename, attachment_content)</code>](#send_mail): Sends an email

- [<code>send_mail_with_excel(to, subject, content, excel_filename, table_or_view_or_query)</code>](#send_mail_with_excel): Sends an email with `table_or_view_or_query` data attached as excel file

- [<code>send_slack_message(message, webhook_url)</code>](#send_slack_message): Sends `message` to a slack channel.

- [<code>send_sms(message, phone_number)</code>](#send_sms): Sends `message` via SMS to `phone_number`

- [<code>send_teams_message(message, webhook_url)</code>](#send_teams_message): Sends `message` to a Microsoft Teams channel.




**🚀 Export**


- [<code>export_to_datastore(project, namespace, kind, key, data)</code>](#export_to_datastore): Exports `data` to Datastore

- [<code>export_to_pubsub(project, topic, data, attributes)</code>](#export_to_pubsub): Exports `data` and `attributes` to Pub/Sub `topic`.

- [<code>post(url, data, headers)</code>](#post): POST `data` to `url`.

- [<code>upload_table_to_gsheet(table_or_view_or_query, max_rows, spreadsheet_url, worksheet_name, write_mode)</code>](#upload_table_to_gsheet): Upload data from `table_or_view_or_query` to Google Sheet

- [<code>upload_to_gsheet(data, spreadsheet_url, worksheet_name, write_mode)</code>](#upload_to_gsheet): Upload `data` (a json array of objects) to a Google Sheet




**1️⃣ Transform numeric**


- [<code>format_percentage(first_number, second_number, nb_decimals)</code>](#format_percentage): Return `first_number / second_number` as a formatted percentage

- [<code>quantize_into_bins(value, bin_bounds)</code>](#quantize_into_bins): Get the `bin_range` in which belongs `value`

- [<code>quantize_into_fixed_width_bins(value, min_bound, max_bound, nb_bins)</code>](#quantize_into_fixed_width_bins): Get the `bin_range` in which belongs `value`




**✨ Transform string**


- [<code>deidentify(text, info_types)</code>](#deidentify): Masks sensitive information of type `info_types` in `text`

- [<code>detect_sensitive_info(text)</code>](#detect_sensitive_info): Detect sensitive information in `text`

- [<code>faker(what, locale)</code>](#faker): Generates fake data

- [<code>is_email_valid(email)</code>](#is_email_valid): Return true if `email` is valid

- [<code>levenshtein(string1, string2)</code>](#levenshtein): Compute levenshtein distance between `string1` and `string2`

- [<code>parse_url(url)</code>](#parse_url): Return `url` parts

- [<code>parse_user_agent(user_agent_string)</code>](#parse_user_agent): Parses User Agent strings into several components

- [<code>remove_accents(str)</code>](#remove_accents): Remove accents

- [<code>remove_extra_whitespaces(str)</code>](#remove_extra_whitespaces): Remove unwanted whitespaces

- [<code>remove_strings(string, strings_to_remove)</code>](#remove_strings): Remove any string of `strings_to_remove` from `string`

- [<code>remove_words(string, words_to_remove)</code>](#remove_words): Remove any word of `words_to_remove` from `string`

- [<code>render_string(template, context)</code>](#render_string): Render template with context using nunjucks.js templating library

- [<code>replace_special_characters(string, replacement)</code>](#replace_special_characters): Replace most common special characters in a `string` with `replacement`

- [<code>translate(text, target_language)</code>](#translate): Translate `text` into `target_language`

- [<code>url_decode(url_encoded_string)</code>](#url_decode): Decode `url_encoded_string`

- [<code>xml_extract(xml, x_path)</code>](#xml_extract): Returns content extracted from XML from given XPATH








<div style="margin-top: 6rem;"></div>


## 🧠 AI

!!! note ""
    **Generative AI! **

    Query your data in Natural Language!

---



### ask_bison
<span style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://lh3.googleusercontent.com/a-/ACB-R5RDf2yxcw1p_IYLCKmiUIScreatDdhG8B83om6Ohw=s260" width="32" style=" border-radius: 50% !important">
  </a>

  <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/ask_bison.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></span>
```
ask_bison(question)
```

**Description**

Ask Anything!

Google Generative AI `bison` model will get you an answer.


**Examples**



<span style="color: var(--md-typeset-a-color);">1. Clean data</span>






=== "EU"

```sql
select bigfunctions.eu.ask_bison(
    '''
    Question: what is the country from the following user input: 'I live in frace' ?
    Answer: formatted as alpha three code
    '''
) as answer

```







