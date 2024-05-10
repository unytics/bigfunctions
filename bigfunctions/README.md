---
description: "Catalog of open-source BigFunctions"
search:
  exclude: true
---

# BigFunctions


BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.





!!! note ""

    **✅ You can call ANY of the following public BigFunctions from your Google Cloud Project** (*no install*).

    - The functions are deployed in `bigfunctions` GCP project in 39 datasets for all of the 39 BigQuery regions.
    - They are public, so they can be called by anyone.
    - For any question or difficulties, please read [Getting Started](../README.md).
    - If you prefer to deploy the BigFunction in your own project, read [Getting Started](../README.md).
    - Found a bug? Please raise an issue [here](https://github.com/unytics/bigfunctions/issues/new/choose)

??? info "All BigFunctions Datasets >"

    | Region | Dataset |
    |--------|---------|
    | `eu` | `bigfunctions.eu` |
    | `us` | `bigfunctions.us` |
    | `europe-west1` | `bigfunctions.europe_west1` |
    | `asia-east1` | `bigfunctions.asia_east1` |
    | `asia-east2` | `bigfunctions.asia_east2` |
    | `asia-northeast1` | `bigfunctions.asia_northeast1` |
    | `asia-northeast2` | `bigfunctions.asia_northeast2` |
    | `asia-northeast3` | `bigfunctions.asia_northeast3` |
    | `asia-south1` | `bigfunctions.asia_south1` |
    | `asia-south2` | `bigfunctions.asia_south2` |
    | `asia-southeast1` | `bigfunctions.asia_southeast1` |
    | `asia-southeast2` | `bigfunctions.asia_southeast2` |
    | `australia-southeast1` | `bigfunctions.australia_southeast1` |
    | `australia-southeast2` | `bigfunctions.australia_southeast2` |
    | `europe-central2` | `bigfunctions.europe_central2` |
    | `europe-north1` | `bigfunctions.europe_north1` |
    | `europe-southwest1` | `bigfunctions.europe_southwest1` |
    | `europe-west2` | `bigfunctions.europe_west2` |
    | `europe-west3` | `bigfunctions.europe_west3` |
    | `europe-west4` | `bigfunctions.europe_west4` |
    | `europe-west6` | `bigfunctions.europe_west6` |
    | `europe-west8` | `bigfunctions.europe_west8` |
    | `europe-west9` | `bigfunctions.europe_west9` |
    | `europe-west12` | `bigfunctions.europe_west12` |
    | `me-central1` | `bigfunctions.me_central1` |
    | `me-west1` | `bigfunctions.me_west1` |
    | `northamerica-northeast1` | `bigfunctions.northamerica_northeast1` |
    | `northamerica-northeast2` | `bigfunctions.northamerica_northeast2` |
    | `southamerica-east1` | `bigfunctions.southamerica_east1` |
    | `southamerica-west1` | `bigfunctions.southamerica_west1` |
    | `us-central1` | `bigfunctions.us_central1` |
    | `us-east1` | `bigfunctions.us_east1` |
    | `us-east4` | `bigfunctions.us_east4` |
    | `us-east5` | `bigfunctions.us_east5` |
    | `us-south1` | `bigfunctions.us_south1` |
    | `us-west1` | `bigfunctions.us_west1` |
    | `us-west2` | `bigfunctions.us_west2` |
    | `us-west3` | `bigfunctions.us_west3` |
    | `us-west4` | `bigfunctions.us_west4` |
    





## 👀 Explore

- [<code>explore_table(fully_qualified_table)</code>](explore_table.md): Show table infos and column statistics
- [<code>sankey_chart(data)</code>](sankey_chart.md): Return html with a Sankey Google chart
- [<code>explore_dataset(fully_qualified_dataset)</code>](explore_dataset.md): Show infos about dataset tables
- [<code>chart(data, chart_type, options)</code>](chart.md): Return html with a chartjs chart
- [<code>explore_column(fully_qualified_column)</code>](explore_column.md): Show column statistics


## 🧠 AI

- [<code>ask_appstore_reviews(prompt, app_url_in_appstore)</code>](ask_appstore_reviews.md): Ask AI what your app users think.
- [<code>generate_sql(question, fully_qualified_table)</code>](generate_sql.md): Transform `question` to a SQL query.
- [<code>ask_my_data(question, fully_qualified_table)</code>](ask_my_data.md): Ask your data any `question` in natural language.
- [<code>ask_ai(prompt, model)</code>](ask_ai.md): Ask Anything!


## 🛢 Get data

- [<code>get_webpage_metadata(url)</code>](get_webpage_metadata.md): Get webpage metadata
- [<code>get_appstore_reviews(url)</code>](get_appstore_reviews.md): GET Apple App Store Reviews of an app 
- [<code>get_meteo(latitude, longitude, date)</code>](get_meteo.md): Get `meteo`
- [<code>get_webpage_structured_data(url)</code>](get_webpage_structured_data.md): Get webpage Structured Data
- [<code>get_json(url, headers)</code>](get_json.md): GET json `data` from `url`
- [<code>exchange_rate(base, to)</code>](exchange_rate.md): Get `exchange_rate`
- [<code>get(url, headers)</code>](get.md): Request `url`


## 💬 Notify

- [<code>send_mail_with_excel(to, subject, content, excel_filename, table_or_view_or_query)</code>](send_mail_with_excel.md): Sends an email with `table_or_view_or_query` data attached as excel file
- [<code>send_sms(message, phone_number)</code>](send_sms.md): Sends `message` via SMS to `phone_number`
- [<code>send_teams_message(message, webhook_url)</code>](send_teams_message.md): Sends `message` to a Microsoft Teams channel.
- [<code>send_slack_message(message, webhook_url)</code>](send_slack_message.md): Sends `message` to a slack channel.
- [<code>send_google_chat_message(message, webhook_url)</code>](send_google_chat_message.md): Sends `message` to google chat space
- [<code>send_mail(to, subject, content, attachment_filename, attachment_content)</code>](send_mail.md): Sends an email


## 🚀 Export

- [<code>upload_table_to_gsheet(table_or_view_or_query, max_rows, spreadsheet_url, worksheet_name, write_mode)</code>](upload_table_to_gsheet.md): Upload data from `table_or_view_or_query` to Google Sheet
- [<code>post(url, data, headers)</code>](post.md): POST `data` to `url`.
- [<code>export_to_pubsub(project, topic, data, attributes)</code>](export_to_pubsub.md): Exports `data` and `attributes` to Pub/Sub `topic`.
- [<code>export_to_datastore(project, namespace, kind, key, data)</code>](export_to_datastore.md): Exports `data` to Datastore
- [<code>upload_to_gsheet(data, spreadsheet_url, worksheet_name, write_mode)</code>](upload_to_gsheet.md): Upload `data` (a json array of objects) to a Google Sheet


## 1️⃣ Transform numeric

- [<code>format_percentage(first_number, second_number, nb_decimals)</code>](format_percentage.md): Return `first_number / second_number` as a formatted percentage
- [<code>quantize_into_fixed_width_bins(value, min_bound, max_bound, nb_bins)</code>](quantize_into_fixed_width_bins.md): Get the `bin_range` in which belongs `value`
- [<code>quantize_into_bins(value, bin_bounds)</code>](quantize_into_bins.md): Get the `bin_range` in which belongs `value`
- [<code>weighted_average(element, weight)</code>](weighted_average.md): Returns the weigthed average elements.


## ✨ Transform string

- [<code>phone_number_info(phone_number, options)</code>](phone_number_info.md): Get `phone_number` info
- [<code>remove_strings(string, strings_to_remove)</code>](remove_strings.md): Remove any string of `strings_to_remove` from `string`
- [<code>translate(text, target_language)</code>](translate.md): Translate `text` into `target_language`
- [<code>deidentify(text, info_types)</code>](deidentify.md): Masks sensitive information of type `info_types` in `text`
- [<code>parse_url(url)</code>](parse_url.md): Return `url` parts
- [<code>levenshtein(string1, string2)</code>](levenshtein.md): Compute levenshtein distance between `string1` and `string2`
- [<code>convert_non_ascii_characters_to_unicode_escape_sequences(text)</code>](convert_non_ascii_characters_to_unicode_escape_sequences.md): Replace all non ASCII characters with escape unicode
- [<code>faker(what, locale)</code>](faker.md): Generates fake data
- [<code>remove_words(string, words_to_remove)</code>](remove_words.md): Remove any word of `words_to_remove` from `string`
- [<code>is_phone_number_valid(phone_number, options)</code>](is_phone_number_valid.md): Return if `phone_number` is valid
- [<code>ip2country_name(ip)</code>](ip2country_name.md): Get `country_name` of `ip`
- [<code>xml_extract(xml, x_path)</code>](xml_extract.md): Returns content extracted from XML from given XPATH
- [<code>render_template(template, context)</code>](render_template.md): Render template with context using nunjucks.js templating library
- [<code>replace_special_characters(string, replacement)</code>](replace_special_characters.md): Replace most common special characters in a `string` with `replacement`
- [<code>remove_accents(str)</code>](remove_accents.md): Remove accents
- [<code>parse_user_agent(user_agent_string)</code>](parse_user_agent.md): Parses User Agent strings into several components
- [<code>ip_range2ip_networks(first_ip, last_ip)</code>](ip_range2ip_networks.md): Convert an IP range into a json list of IP networks in CIDR notation
- [<code>url_decode(url_encoded_string)</code>](url_decode.md): Decode `url_encoded_string`
- [<code>detect_sensitive_info(text)</code>](detect_sensitive_info.md): Detect sensitive information in `text`
- [<code>ip2asn(ip)</code>](ip2asn.md): Get `asn` of `ip`
- [<code>is_email_valid(email)</code>](is_email_valid.md): Return true if `email` is valid
- [<code>ip2continent_name(ip)</code>](ip2continent_name.md): Get `continent` of `ip`
- [<code>ip2country(ip)</code>](ip2country.md): Get `country_code` of `ip`
- [<code>render_string(template, context)</code>](render_string.md): Render template with context using nunjucks.js templating library
- [<code>ip2continent(ip)</code>](ip2continent.md): Get `continent_code` of `ip`
- [<code>remove_extra_whitespaces(str)</code>](remove_extra_whitespaces.md): Remove unwanted whitespaces


## 🌐 Transform geo data

- [<code>validate_address(address)</code>](validate_address.md): Validate `address` using Google Maps
- [<code>reverse_geocode(latitude, longitude)</code>](reverse_geocode.md): Get address details at `latitude`, `longitude`
- [<code>h3(function_name, arguments)</code>](h3.md): Wrapper around [Uber H3](https://github.com/uber/h3-js)
- [<code>geocode(address)</code>](geocode.md): Get `address` details from Google Maps


## 📆 Transform date

- [<code>gregorian2hijri(gregorian_date)</code>](gregorian2hijri.md): Convert Gregorian Date to Hijri Date (taken from [here](https://stackoverflow.com/questions/78072960/convert-dates-gregorian-to-hijri-bigquery#answer-78079872))
- [<code>is_public_holiday(date, country_code)</code>](is_public_holiday.md): Return true if `date` corresponds to a public holiday in `country_code`
- [<code>date_sub_isoyear(date, years)</code>](date_sub_isoyear.md): Returns same day `years` before
- [<code>translated_weekday_name(date, language)</code>](translated_weekday_name.md): Get `translated_weekday_name`
- [<code>translated_month_name(date, language)</code>](translated_month_name.md): Get `translated_month_name`
- [<code>generate_dates(start_date, end_date)</code>](generate_dates.md): Generate a table of dates
- [<code>parse_date(date_string)</code>](parse_date.md): Parse date with automatic format detection


## <span style="color: var(--md-primary-fg-color);">{...}</span> Transform json

- [<code>items2json(key_value_items)</code>](items2json.md): Returns `json` object from array of `key_value_items`
- [<code>json_values(json_string)</code>](json_values.md): Extract `values` from `json_string`
- [<code>json_schema(json_string)</code>](json_schema.md): Return the schema of a json string as `[{path, type}]`
- [<code>json_keys(json_string)</code>](json_keys.md): Extract `keys` from `json_string`
- [<code>json_query(json_string, query)</code>](json_query.md): Extract data from `json_string` using advanced json querying
- [<code>json_merge(json_string1, json_string2)</code>](json_merge.md): Merge `json_string1` and `json_string2`
- [<code>json_items(json_string)</code>](json_items.md): Extract `key_value_items` from `json_string`


## <span style="color: var(--md-primary-fg-color);">[...]</span> Transform array

- [<code>remove_value(arr, value)</code>](remove_value.md): Return an array with all values except `value`.
- [<code>distinct_values(arr)</code>](distinct_values.md): Return distinct values
- [<code>median_value(arr)</code>](median_value.md): Return median value of array
- [<code>percentile_value(arr, percentile)</code>](percentile_value.md): Returns percentile of an array with percentile a float in range [0, 1].
- [<code>sort_values_desc(arr)</code>](sort_values_desc.md): Return sorted array (descending)
- [<code>last_value(arr)</code>](last_value.md): Return last value of array
- [<code>find_value(arr, value)</code>](find_value.md): Return the first `offset` (zero-based index) of `value` in array `arr`
- [<code>find_lower_value(arr, x)</code>](find_lower_value.md): Return the `offset` (zero-based index) of the first `value` in `arr` where `value <= x`
- [<code>get_value(key_value_items, search_key)</code>](get_value.md): Return the first `value` with a key `search_key` from `key_value_items`
- [<code>min_value(arr)</code>](min_value.md): Return min value of array
- [<code>array_intersect(array1, array2)</code>](array_intersect.md): Returns the intersection of two arrays.
- [<code>sum_values(arr)</code>](sum_values.md): Return the sum of array values
- [<code>array_union(array1, array2)</code>](array_union.md): Returns the union of two arrays.
- [<code>find_greater_value(arr, x)</code>](find_greater_value.md): Return the `offset` (zero-based index) of the first `value` in `arr` where `value >= x`
- [<code>sort_values(arr)</code>](sort_values.md): Return sorted array (ascending)
- [<code>max_value(arr)</code>](max_value.md): Return max value of array
- [<code>are_arrays_equal(array1, array2)</code>](are_arrays_equal.md): Return true if `array1` = `array2`


## 🧠 Machine learning

- [<code>roc_auc(predictions)</code>](roc_auc.md): Returns the Area Under the Receiver Operating Characteristic Curve (a.k.a. ROC AUC)
- [<code>precision_recall_auc(predictions)</code>](precision_recall_auc.md): Returns the Area Under the Precision Recall Curve (a.k.a. AUC PR)
- [<code>prophet(records, periods, kwargs)</code>](prophet.md): Forecast time-series using prophet
- [<code>roc_curve(predictions)</code>](roc_curve.md): Returns the Receiver Operating Characteristic Curve (a.k.a. ROC Curve)
- [<code>sentiment_score(content)</code>](sentiment_score.md): Compute sentiment score of `content`
- [<code>precision_recall_curve(predictions)</code>](precision_recall_curve.md): Returns the Precision-Recall Curve


## 🌐 Graph

- [<code>connected_components(fully_qualified_table)</code>](connected_components.md): Compute the connected components of a non-directed graph.


## 🔨 Convert data format

- [<code>json2excel(data)</code>](json2excel.md): Dump data to excel file
- [<code>json2xml(json)</code>](json2xml.md): Returns XML for given JSON string
- [<code>html2pdf(html)</code>](html2pdf.md): Convert `html` to `pdf`
- [<code>xml2json(xml)</code>](xml2json.md): Returns JSON as a string for given XML string


## 🔨 Utils

- [<code>deduplicate_rows(query_or_table_or_view)</code>](deduplicate_rows.md): Returns the deduplicated rows of `query_or_table_or_view`
- [<code>get_table_columns(fully_qualified_table)</code>](get_table_columns.md): Get the column information of the given table from `INFORMATION_SCHEMA.COLUMNS`
- [<code>get_view_history(fully_qualified_view)</code>](get_view_history.md): Get BigQuery View history
- [<code>sleep(seconds)</code>](sleep.md): Sleep during `seconds` seconds
- [<code>get_latest_partition_timestamp(fully_qualified_table)</code>](get_latest_partition_timestamp.md): Return the maximum of the partition column of `fully_qualified_table`
- [<code>upsert(query_or_table_or_view, destination_table, insertion_mode, primary_keys, recency_field)</code>](upsert.md): Merges `query_or_table_or_view` into the `destination_table`.
- [<code>run_python(python_code, requirements, kwargs)</code>](run_python.md): Run any `python_code`.
- [<code>timestamp_to_unix_date_time(timestamp_expression, date_time_part)</code>](timestamp_to_unix_date_time.md): Returns the number of `date_time_part` since `1970-01-01 00:00:00 UTC`.
- [<code>timestamp_from_unix_date_time(unix_date_time, date_time_part)</code>](timestamp_from_unix_date_time.md): Interprets `unix_date_time` as the number of `date_time_part` since `1970-01-01 00:00:00 UTC`.



