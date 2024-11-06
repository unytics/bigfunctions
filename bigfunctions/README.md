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






## 🧠 AI

- [<code>ask_ai(prompt, model)</code>](ask_ai.md): Ask Anything!
- [<code>ask_appstore_reviews(prompt, app_url_in_appstore)</code>](ask_appstore_reviews.md): Ask AI what your app users think.
- [<code>ask_my_data(question, fully_qualified_table)</code>](ask_my_data.md): Ask your data any `question` in natural language.
- [<code>categorize(items)</code>](categorize.md): Categorize `items` in categories and subcategories.
- [<code>classify_text(text, candidate_labels)</code>](classify_text.md): Classify `text` among `candidate_labels`
- [<code>generate_categories(items)</code>](generate_categories.md): Return `categories` of `items`.
- [<code>generate_face_embedding(image_url)</code>](generate_face_embedding.md): Detect Face on image and Generate its Embedding
- [<code>generate_sql(question, fully_qualified_table)</code>](generate_sql.md): Transform `question` to a SQL query.


## 💬 Notify

- [<code>send_google_chat_message(message, webhook_url)</code>](send_google_chat_message.md): Sends `message` to google chat space
- [<code>send_mail(to, subject, content, attachment_filename, attachment_content)</code>](send_mail.md): Sends an email
- [<code>send_mail_with_excel(to, subject, content, excel_filename, table_or_view_or_query)</code>](send_mail_with_excel.md): Sends an email with `table_or_view_or_query` data attached as excel file
- [<code>send_slack_message(message, webhook_url)</code>](send_slack_message.md): Sends `message` to a slack channel.
- [<code>send_sms(message, phone_number)</code>](send_sms.md): Sends `message` via SMS to `phone_number`
- [<code>send_teams_message(message, webhook_url)</code>](send_teams_message.md): Sends `message` to a Microsoft Teams channel.


## 🛢 Get data

- [<code>exchange_rate(base, to)</code>](exchange_rate.md): Get `exchange_rate`
- [<code>faker(what, locale)</code>](faker.md): Generates fake data
- [<code>get(url, headers)</code>](get.md): Request `url`
- [<code>get_appstore_reviews(url)</code>](get_appstore_reviews.md): GET Apple App Store Reviews of an app
- [<code>get_github_data(public_repo, destination_dataset, streams)</code>](get_github_data.md): Get data from `public_repo` into `destination_dataset`
- [<code>get_json(url, headers)</code>](get_json.md): GET json `data` from `url`
- [<code>get_meteo(latitude, longitude, date)</code>](get_meteo.md): Get `meteo`
- [<code>get_playstore_reviews(app_id, country, language)</code>](get_playstore_reviews.md): GET Google Play Store Reviews of an app
- [<code>get_transport_emissions(distance_km)</code>](get_transport_emissions.md): Get the transport CO2 emissions given the `distance_km`
- [<code>get_webpage_data(prompt, url)</code>](get_webpage_data.md): Extract `data` from `url` using `prompt`
- [<code>get_webpage_metadata(url)</code>](get_webpage_metadata.md): Get webpage metadata
- [<code>get_webpage_structured_data(url)</code>](get_webpage_structured_data.md): Get webpage Structured Data
- [<code>list_public_datasets()</code>](list_public_datasets.md): Returns list of BigQuery `public_datasets`
- [<code>load_api_data(source, source_config, streams, destination_dataset)</code>](load_api_data.md): Load data from 250+ sources using [Airbyte Python Connectors](https://docs.airbyte.com/using-airbyte/pyairbyte/getting-started#available-connectors)
- [<code>load_api_data_into_temp_dataset(source, source_config, streams, state)</code>](load_api_data_into_temp_dataset.md): Load data from 250+ sources using [Airbyte Python Connectors](https://docs.airbyte.com/using-airbyte/pyairbyte/getting-started#available-connectors)
- [<code>load_file(url, file_type, destination_table, options)</code>](load_file.md): Download web file into `destination_table`
- [<code>load_file_into_temp_dataset(url, file_type, options)</code>](load_file_into_temp_dataset.md): Download web file into a temp dataset


## 🚀 Export

- [<code>export_to_datastore(project, namespace, kind, key, data)</code>](export_to_datastore.md): Exports `data` to Datastore
- [<code>export_to_pubsub(project, topic, data, attributes)</code>](export_to_pubsub.md): Exports `data` and `attributes` to Pub/Sub `topic`.
- [<code>post(url, data, headers)</code>](post.md): POST `data` to `url`.
- [<code>refresh_powerbi(dataset_id, workspace_id, tenant_id, app_id, token_secret, custom_refresh_param)</code>](refresh_powerbi.md): Refresh a Power BI dataset (semantic model)
- [<code>refresh_tableau(workbook_or_datasource_title, site, server, token_name, token_secret)</code>](refresh_tableau.md): Refresh a tableau datasource or workbook
- [<code>upload_table_to_gsheet(table_or_view_or_query, max_rows, spreadsheet_url, worksheet_name, write_mode)</code>](upload_table_to_gsheet.md): Upload data from `table_or_view_or_query` to Google Sheet
- [<code>upload_to_gsheet(data, spreadsheet_url, worksheet_name, write_mode)</code>](upload_to_gsheet.md): Upload `data` (a json array of objects) to a Google Sheet


## 1️⃣ Transform numeric

- [<code>format_percentage(first_number, second_number, nb_decimals)</code>](format_percentage.md): Return `first_number / second_number` as a formatted percentage
- [<code>quantize_into_bins(value, bin_bounds)</code>](quantize_into_bins.md): Get the `bin_range` in which belongs `value`
- [<code>quantize_into_bins_with_labels(value, bin_bounds, labels)</code>](quantize_into_bins_with_labels.md): Get the `label` of the bin in which belongs `value`
- [<code>quantize_into_fixed_width_bins(value, min_bound, max_bound, nb_bins)</code>](quantize_into_fixed_width_bins.md): Get the `bin_range` in which belongs `value`
- [<code>weighted_average(element, weight)</code>](weighted_average.md): Returns the weigthed average elements.


## ✨ Transform string

- [<code>camel2snake(camelCaseString)</code>](camel2snake.md): Convert `string` from camelCase to snake_case
- [<code>convert_non_ascii_characters_to_unicode_escape_sequences(text)</code>](convert_non_ascii_characters_to_unicode_escape_sequences.md): Replace all non ASCII characters with escape unicode
- [<code>deidentify(text, info_types)</code>](deidentify.md): Masks sensitive information of type `info_types` in `text`
- [<code>detect_sensitive_info(text)</code>](detect_sensitive_info.md): Detect sensitive information in `text`
- [<code>ip2asn(ip)</code>](ip2asn.md): Get `asn` of `ip`
- [<code>ip2continent(ip)</code>](ip2continent.md): Get `continent_code` of `ip`
- [<code>ip2continent_name(ip)</code>](ip2continent_name.md): Get `continent` of `ip`
- [<code>ip2country(ip)</code>](ip2country.md): Get `country_code` of `ip`
- [<code>ip2country_name(ip)</code>](ip2country_name.md): Get `country_name` of `ip`
- [<code>ip_range2ip_networks(first_ip, last_ip)</code>](ip_range2ip_networks.md): Convert an IP range into a json list of IP networks in CIDR notation
- [<code>is_email_valid(email)</code>](is_email_valid.md): Return true if `email` is valid
- [<code>is_phone_number_valid(phone_number, options)</code>](is_phone_number_valid.md): Return if `phone_number` is valid
- [<code>levenshtein(string1, string2)</code>](levenshtein.md): Compute levenshtein distance between `string1` and `string2`
- [<code>markdown2html(markdown)</code>](markdown2html.md): Convert `markdown` to `html`
- [<code>ngram_frequency_similarity(string1, string2, n)</code>](ngram_frequency_similarity.md): Calculates n-gram similarity between two strings
- [<code>parse_url(url)</code>](parse_url.md): Return `url` parts
- [<code>parse_user_agent(user_agent_string)</code>](parse_user_agent.md): Parses User Agent strings into several components
- [<code>phone_number_info(phone_number, options)</code>](phone_number_info.md): Get `phone_number` info
- [<code>remove_accents(str)</code>](remove_accents.md): Remove accents
- [<code>remove_extra_whitespaces(str)</code>](remove_extra_whitespaces.md): Remove unwanted whitespaces
- [<code>remove_strings(string, strings_to_remove)</code>](remove_strings.md): Remove any string of `strings_to_remove` from `string`
- [<code>remove_words(string, words_to_remove)</code>](remove_words.md): Remove any word of `words_to_remove` from `string`
- [<code>render_handlebars_template(template, context)</code>](render_handlebars_template.md): Render template with context using handlebars.js templating library
- [<code>render_template(template, context)</code>](render_template.md): Render template with context using nunjucks.js templating library
- [<code>replace_special_characters(string, replacement)</code>](replace_special_characters.md): Replace most common special characters in a `string` with `replacement`
- [<code>translate(text, target_language)</code>](translate.md): Translate `text` into `target_language`
- [<code>url_decode(url_encoded_string)</code>](url_decode.md): Decode `url_encoded_string`
- [<code>xml_extract(xml, x_path)</code>](xml_extract.md): Returns content extracted from XML from given XPATH


## 🌐 Transform geo data

- [<code>geocode(address)</code>](geocode.md): Get `address` details from Google Maps
- [<code>h3(function_name, arguments)</code>](h3.md): Wrapper around [Uber H3](https://github.com/uber/h3-js)
- [<code>reverse_geocode(latitude, longitude)</code>](reverse_geocode.md): Get address details at `latitude`, `longitude`
- [<code>validate_address(address)</code>](validate_address.md): Validate `address` using Google Maps


## 📆 Transform date

- [<code>date_sub_isoyear(date, years)</code>](date_sub_isoyear.md): Returns same day `years` before
- [<code>generate_dates(start_date, end_date)</code>](generate_dates.md): Generate a table of dates
- [<code>gregorian2hijri(gregorian_date)</code>](gregorian2hijri.md): Convert Gregorian Date to Hijri Date (taken from [here](https://stackoverflow.com/questions/78072960/convert-dates-gregorian-to-hijri-bigquery#answer-78079872))
- [<code>is_public_holiday(date, country_code)</code>](is_public_holiday.md): Return true if `date` corresponds to a public holiday in `country_code`
- [<code>parse_date(date_string)</code>](parse_date.md): Parse date with automatic format detection
- [<code>translated_month_name(date, language)</code>](translated_month_name.md): Get `translated_month_name`
- [<code>translated_weekday_name(date, language)</code>](translated_weekday_name.md): Get `translated_weekday_name`


## <span style="color: var(--md-primary-fg-color);">{...}</span> Transform json

- [<code>create_materialized_view_w_flattened_json_column(fully_qualified_table, fully_qualified_materialized_view, json_column)</code>](create_materialized_view_w_flattened_json_column.md): Create a Materialized view of a table with `json_column` flattened
- [<code>items2json(key_value_items)</code>](items2json.md): Returns `json` object from array of `key_value_items`
- [<code>json_column_schema(data)</code>](json_column_schema.md): Returns the schema of a json column
- [<code>json_items(json_string)</code>](json_items.md): Extract `key_value_items` from `json_string`
- [<code>json_keys(json_string)</code>](json_keys.md): Extract `keys` from `json_string`
- [<code>json_merge(json_string1, json_string2)</code>](json_merge.md): Merge `json_string1` and `json_string2`
- [<code>json_query(json_string, query)</code>](json_query.md): Extract data from `json_string` using advanced json querying
- [<code>json_schema(data)</code>](json_schema.md): Returns the schema of `data`
- [<code>json_values(json_string)</code>](json_values.md): Extract `values` from `json_string`
- [<code>sql_to_flatten_json_column(data, fully_qualified_column)</code>](sql_to_flatten_json_column.md): Generate the SQL to flatten a json `column`


## <span style="color: var(--md-primary-fg-color);">[...]</span> Transform array

- [<code>are_arrays_equal(array1, array2)</code>](are_arrays_equal.md): Return true if `array1` = `array2`
- [<code>array_intersect(array1, array2)</code>](array_intersect.md): Returns the intersection of two arrays.
- [<code>array_union(array1, array2)</code>](array_union.md): Returns the union of two arrays.
- [<code>benford_distance(values)</code>](benford_distance.md): Calculate the distance from Benford's Law for given `values`.
- [<code>distinct_values(arr)</code>](distinct_values.md): Return distinct values
- [<code>find_greater_value(arr, x)</code>](find_greater_value.md): Return the `offset` (zero-based index) of the first `value` in `arr` where `value >= x`
- [<code>find_lower_value(arr, x)</code>](find_lower_value.md): Return the `offset` (zero-based index) of the first `value` in `arr` where `value <= x`
- [<code>find_value(arr, value)</code>](find_value.md): Return the first `offset` (zero-based index) of `value` in array `arr`
- [<code>frequent_values(values, frequency_threshold)</code>](frequent_values.md): Returns `frequent_values` among array of `values`
- [<code>get_value(key_value_items, search_key)</code>](get_value.md): Return the first `value` with a key `search_key` from `key_value_items`
- [<code>last_value(arr)</code>](last_value.md): Return last value of array
- [<code>max_value(arr)</code>](max_value.md): Return max value of array
- [<code>median_value(arr)</code>](median_value.md): Return median value of array
- [<code>min_max_scaler(arr)</code>](min_max_scaler.md): Performs min-max scaling on an array.
- [<code>min_value(arr)</code>](min_value.md): Return min value of array
- [<code>percentile_value(arr, percentile)</code>](percentile_value.md): Returns percentile of an array with percentile a float in range [0, 1].
- [<code>rare_values(values, frequency_threshold)</code>](rare_values.md): Returns `rare_values` among array of `values`
- [<code>remove_value(arr, value)</code>](remove_value.md): Return an array with all values except `value`.
- [<code>sort_values(arr)</code>](sort_values.md): Return sorted array (ascending)
- [<code>sort_values_desc(arr)</code>](sort_values_desc.md): Return sorted array (descending)
- [<code>sum_values(arr)</code>](sum_values.md): Return the sum of array values
- [<code>z_scores(arr)</code>](z_scores.md): Compute `z_scores`


## 🧠 Machine learning

- [<code>precision_recall_auc(predictions)</code>](precision_recall_auc.md): Returns the Area Under the Precision Recall Curve (a.k.a. AUC PR)
- [<code>precision_recall_curve(predictions)</code>](precision_recall_curve.md): Returns the Precision-Recall Curve
- [<code>prophet(records, periods, kwargs)</code>](prophet.md): Forecast time-series using prophet
- [<code>roc_auc(predictions)</code>](roc_auc.md): Returns the Area Under the Receiver Operating Characteristic Curve (a.k.a. ROC AUC)
- [<code>roc_curve(predictions)</code>](roc_curve.md): Returns the Receiver Operating Characteristic Curve (a.k.a. ROC Curve)
- [<code>sentiment_score(content)</code>](sentiment_score.md): Compute sentiment score of `content`


## 🌐 Graph

- [<code>connected_components(fully_qualified_table)</code>](connected_components.md): Compute the connected components of a non-directed graph.


## 🔨 Convert data format

- [<code>html2pdf(html)</code>](html2pdf.md): Convert `html` to `pdf`
- [<code>json2excel(data)</code>](json2excel.md): Dump data to excel file
- [<code>json2xml(json)</code>](json2xml.md): Returns XML for given JSON string
- [<code>xml2json(xml)</code>](xml2json.md): Returns JSON as a string for given XML string


## 👀 Explore

- [<code>chart(data, chart_type, ylabel)</code>](chart.md): Return html with a chartjs chart
- [<code>explore_column(fully_qualified_column)</code>](explore_column.md): Show column statistics
- [<code>explore_dataset(fully_qualified_dataset)</code>](explore_dataset.md): Show infos about dataset tables
- [<code>explore_table(fully_qualified_table)</code>](explore_table.md): Show table infos and column statistics
- [<code>list_dataset_tables(fully_qualified_dataset)</code>](list_dataset_tables.md): List tables of `fully_qualified_dataset`
- [<code>sankey_chart(data)</code>](sankey_chart.md): Return html with a Sankey Google chart


## 🔨 Utils

- [<code>deduplicate_rows(query_or_table_or_view)</code>](deduplicate_rows.md): Returns the deduplicated rows of `query_or_table_or_view`
- [<code>get_latest_partition_timestamp(fully_qualified_table)</code>](get_latest_partition_timestamp.md): Return the maximum of the partition column of `fully_qualified_table`
- [<code>get_table_columns(fully_qualified_table)</code>](get_table_columns.md): Get the column information of the given table from `INFORMATION_SCHEMA.COLUMNS`
- [<code>get_view_history(fully_qualified_view)</code>](get_view_history.md): Get BigQuery View history
- [<code>list_scheduled_queries(project)</code>](list_scheduled_queries.md): Returns`scheduled_queries` of project `project`.
- [<code>run_python(python_code, requirements, kwargs)</code>](run_python.md): Run any `python_code`.
- [<code>sleep(seconds)</code>](sleep.md): Sleep during `seconds` seconds
- [<code>timestamp_from_unix_date_time(unix_date_time, date_time_part)</code>](timestamp_from_unix_date_time.md): Interprets `unix_date_time` as the number of `date_time_part` since `1970-01-01 00:00:00 UTC`.
- [<code>timestamp_to_unix_date_time(timestamp_expression, date_time_part)</code>](timestamp_to_unix_date_time.md): Returns the number of `date_time_part` since `1970-01-01 00:00:00 UTC`.
- [<code>upsert(query_or_table_or_view, destination_table, insertion_mode, primary_keys, recency_field)</code>](upsert.md): Merges `query_or_table_or_view` into the `destination_table`.
