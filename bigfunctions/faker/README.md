---
title: "faker"
description: "BigFunction faker: Generates fake data
of type `what` and localized with `locale` parameter (using [faker python library](https://faker.readthedocs.io/))

| Param  | Possible values  |
|---|---|
| `what`  | `aba`, `address`, `administrative_unit`, `am_pm`, `android_platform_token`, `ascii_company_email`, `ascii_email`, `ascii_free_email`, `ascii_safe_email`, `bank_country`, `bban`, `binary`, `boolean`, `bothify`, `bs`, `building_number`, `catch_phrase`, `century`, `chrome`, `city`, `city_prefix`, `city_suffix`, `color`, `color_name`, `company`, `company_email`, `company_suffix`, `coordinate`, `country`, `country_calling_code`, `country_code`, `credit_card_expire`, `credit_card_full`, `credit_card_number`, `credit_card_provider`, `credit_card_security_code`, `cryptocurrency`, `cryptocurrency_code`, `cryptocurrency_name`, `csv`, `currency`, `currency_code`, `currency_name`, `currency_symbol`, `current_country`, `current_country_code`, `date`, `date_between`, `date_between_dates`, `date_object`, `date_of_birth`, `date_this_century`, `date_this_decade`, `date_this_month`, `date_this_year`, `date_time`, `date_time_ad`, `date_time_between`, `date_time_between_dates`, `date_time_this_century`, `date_time_this_decade`, `date_time_this_month`, `date_time_this_year`, `day_of_month`, `day_of_week`, `dga`, `domain_name`, `domain_word`, `dsv`, `ean`, `ean13`, `ean8`, `ein`, `email`, `emoji`, `file_extension`, `file_name`, `file_path`, `firefox`, `first_name`, `first_name_female`, `first_name_male`, `first_name_nonbinary`, `fixed_width`, `free_email`, `free_email_domain`, `future_date`, `future_datetime`, `get_providers`, `hex_color`, `hexify`, `hostname`, `http_method`, `iana_id`, `iban`, `image_url`, `internet_explorer`, `invalid_ssn`, `ios_platform_token`, `ipv4`, `ipv4_network_class`, `ipv4_private`, `ipv4_public`, `ipv6`, `isbn10`, `isbn13`, `iso8601`, `items`, `itin`, `job`, `json`, `json_bytes`, `language_code`, `language_name`, `last_name`, `last_name_female`, `last_name_male`, `last_name_nonbinary`, `latitude`, `latlng`, `lexify`, `license_plate`, `linux_platform_token`, `linux_processor`, `local_latlng`, `locale`, `localized_ean`, `localized_ean13`, `localized_ean8`, `location_on_land`, `longitude`, `mac_address`, `mac_platform_token`, `mac_processor`, `md5`, `military_apo`, `military_dpo`, `military_ship`, `military_state`, `mime_type`, `month`, `month_name`, `msisdn`, `name`, `name_female`, `name_male`, `name_nonbinary`, `nic_handle`, `nic_handles`, `null_boolean`, `numerify`, `opera`, `paragraph`, `paragraphs`, `password`, `past_date`, `past_datetime`, `phone_number`, `port_number`, `postalcode`, `postalcode_in_state`, `postalcode_plus4`, `postcode`, `postcode_in_state`, `prefix`, `prefix_female`, `prefix_male`, `prefix_nonbinary`, `pricetag`, `profile`, `psv`, `pybool`, `pydecimal`, `pydict`, `pyfloat`, `pyint`, `pyiterable`, `pylist`, `pyobject`, `pyset`, `pystr`, `pystr_format`, `pystruct`, `pytimezone`, `pytuple`, `random_choices`, `random_digit`, `random_digit_not_null`, `random_digit_not_null_or_empty`, `random_digit_or_empty`, `random_element`, `random_elements`, `random_int`, `random_letter`, `random_letters`, `random_lowercase_letter`, `random_number`, `random_sample`, `random_uppercase_letter`, `randomize_nb_elements`, `rgb_color`, `rgb_css_color`, `ripe_id`, `safari`, `safe_color_name`, `safe_domain_name`, `safe_email`, `safe_hex_color`, `sbn9`, `secondary_address`, `seed_instance`, `sentence`, `sentences`, `sha1`, `sha256`, `simple_profile`, `slug`, `ssn`, `state`, `state_abbr`, `street_address`, `street_name`, `street_suffix`, `suffix`, `suffix_female`, `suffix_male`, `suffix_nonbinary`, `swift`, `swift11`, `swift8`, `tar`, `text`, `texts`, `time`, `time_delta`, `time_object`, `time_series`, `timezone`, `tld`, `tsv`, `unix_device`, `unix_partition`, `unix_time`, `upc_a`, `upc_e`, `uri`, `uri_extension`, `uri_page`, `uri_path`, `url`, `user_agent`, `user_name`, `uuid4`, `windows_platform_token`, `word`, `words`, `year`, `zip`, `zipcode`, `zipcode_in_state`, `zipcode_plus4` |
| `locale`  | `null`, `ar_AA`, `ar_AE`, `ar_BH`, `ar_EG`, `ar_JO`, `ar_PS`, `ar_SA`, `az_AZ`, `bg_BG`, `bn_BD`, `bs_BA`, `cs_CZ`, `da_DK`, `de`, `de_AT`, `de_CH`, `de_DE`, `dk_DK`, `el_CY`, `el_GR`, `en`, `en_AU`, `en_CA`, `en_GB`, `en_IE`, `en_IN`, `en_NZ`, `en_PH`, `en_TH`, `en_US`, `es`, `es_AR`, `es_CA`, `es_CL`, `es_CO`, `es_ES`, `es_MX`, `et_EE`, `fa_IR`, `fi_FI`, `fil_PH`, `fr_BE`, `fr_CA`, `fr_CH`, `fr_FR`, `fr_QC`, `ga_IE`, `he_IL`, `hi_IN`, `hr_HR`, `hu_HU`, `hy_AM`, `id_ID`, `it_CH`, `it_IT`, `ja_JP`, `ka_GE`, `ko_KR`, `la`, `lb_LU`, `lt_LT`, `lv_LV`, `mt_MT`, `ne_NP`, `nl_BE`, `nl_NL`, `no_NO`, `or_IN`, `pl_PL`, `pt_BR`, `pt_PT`, `ro_RO`, `ru_RU`, `sk_SK`, `sl_SI`, `sq_AL`, `sv_SE`, `ta_IN`, `th`, `th_TH`, `tl_PH`, `tr_TR`, `tw_GH`, `uk_UA`, `vi_VN`, `zh_CN`, `zh_TW`  |
"
---

<span style="color: gray; position: relative; top: -1rem">
  <a href=".." style="color: gray">bigfunctions </a> ＞ faker
</span>

# faker


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/shivamsingh012/" title="Author: Shivam Singh" target="_blank">
    <img src="https://media.licdn.com/dms/image/D4D03AQERv0qwECH0DA/profile-displayphoto-shrink_200_200/0/1675233460732?e=1686182400&v=beta&t=HqngiSx5zd4llZStwf3L0k2T_pE8qvnEj7NguWNJTOo" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/faker.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
faker(what, locale)
```

**Description**

Generates fake data
of type `what` and localized with `locale` parameter (using [faker python library](https://faker.readthedocs.io/))

| Param  | Possible values  |
|---|---|
| `what`  | `aba`, `address`, `administrative_unit`, `am_pm`, `android_platform_token`, `ascii_company_email`, `ascii_email`, `ascii_free_email`, `ascii_safe_email`, `bank_country`, `bban`, `binary`, `boolean`, `bothify`, `bs`, `building_number`, `catch_phrase`, `century`, `chrome`, `city`, `city_prefix`, `city_suffix`, `color`, `color_name`, `company`, `company_email`, `company_suffix`, `coordinate`, `country`, `country_calling_code`, `country_code`, `credit_card_expire`, `credit_card_full`, `credit_card_number`, `credit_card_provider`, `credit_card_security_code`, `cryptocurrency`, `cryptocurrency_code`, `cryptocurrency_name`, `csv`, `currency`, `currency_code`, `currency_name`, `currency_symbol`, `current_country`, `current_country_code`, `date`, `date_between`, `date_between_dates`, `date_object`, `date_of_birth`, `date_this_century`, `date_this_decade`, `date_this_month`, `date_this_year`, `date_time`, `date_time_ad`, `date_time_between`, `date_time_between_dates`, `date_time_this_century`, `date_time_this_decade`, `date_time_this_month`, `date_time_this_year`, `day_of_month`, `day_of_week`, `dga`, `domain_name`, `domain_word`, `dsv`, `ean`, `ean13`, `ean8`, `ein`, `email`, `emoji`, `file_extension`, `file_name`, `file_path`, `firefox`, `first_name`, `first_name_female`, `first_name_male`, `first_name_nonbinary`, `fixed_width`, `free_email`, `free_email_domain`, `future_date`, `future_datetime`, `get_providers`, `hex_color`, `hexify`, `hostname`, `http_method`, `iana_id`, `iban`, `image_url`, `internet_explorer`, `invalid_ssn`, `ios_platform_token`, `ipv4`, `ipv4_network_class`, `ipv4_private`, `ipv4_public`, `ipv6`, `isbn10`, `isbn13`, `iso8601`, `items`, `itin`, `job`, `json`, `json_bytes`, `language_code`, `language_name`, `last_name`, `last_name_female`, `last_name_male`, `last_name_nonbinary`, `latitude`, `latlng`, `lexify`, `license_plate`, `linux_platform_token`, `linux_processor`, `local_latlng`, `locale`, `localized_ean`, `localized_ean13`, `localized_ean8`, `location_on_land`, `longitude`, `mac_address`, `mac_platform_token`, `mac_processor`, `md5`, `military_apo`, `military_dpo`, `military_ship`, `military_state`, `mime_type`, `month`, `month_name`, `msisdn`, `name`, `name_female`, `name_male`, `name_nonbinary`, `nic_handle`, `nic_handles`, `null_boolean`, `numerify`, `opera`, `paragraph`, `paragraphs`, `password`, `past_date`, `past_datetime`, `phone_number`, `port_number`, `postalcode`, `postalcode_in_state`, `postalcode_plus4`, `postcode`, `postcode_in_state`, `prefix`, `prefix_female`, `prefix_male`, `prefix_nonbinary`, `pricetag`, `profile`, `psv`, `pybool`, `pydecimal`, `pydict`, `pyfloat`, `pyint`, `pyiterable`, `pylist`, `pyobject`, `pyset`, `pystr`, `pystr_format`, `pystruct`, `pytimezone`, `pytuple`, `random_choices`, `random_digit`, `random_digit_not_null`, `random_digit_not_null_or_empty`, `random_digit_or_empty`, `random_element`, `random_elements`, `random_int`, `random_letter`, `random_letters`, `random_lowercase_letter`, `random_number`, `random_sample`, `random_uppercase_letter`, `randomize_nb_elements`, `rgb_color`, `rgb_css_color`, `ripe_id`, `safari`, `safe_color_name`, `safe_domain_name`, `safe_email`, `safe_hex_color`, `sbn9`, `secondary_address`, `seed_instance`, `sentence`, `sentences`, `sha1`, `sha256`, `simple_profile`, `slug`, `ssn`, `state`, `state_abbr`, `street_address`, `street_name`, `street_suffix`, `suffix`, `suffix_female`, `suffix_male`, `suffix_nonbinary`, `swift`, `swift11`, `swift8`, `tar`, `text`, `texts`, `time`, `time_delta`, `time_object`, `time_series`, `timezone`, `tld`, `tsv`, `unix_device`, `unix_partition`, `unix_time`, `upc_a`, `upc_e`, `uri`, `uri_extension`, `uri_page`, `uri_path`, `url`, `user_agent`, `user_name`, `uuid4`, `windows_platform_token`, `word`, `words`, `year`, `zip`, `zipcode`, `zipcode_in_state`, `zipcode_plus4` |
| `locale`  | `null`, `ar_AA`, `ar_AE`, `ar_BH`, `ar_EG`, `ar_JO`, `ar_PS`, `ar_SA`, `az_AZ`, `bg_BG`, `bn_BD`, `bs_BA`, `cs_CZ`, `da_DK`, `de`, `de_AT`, `de_CH`, `de_DE`, `dk_DK`, `el_CY`, `el_GR`, `en`, `en_AU`, `en_CA`, `en_GB`, `en_IE`, `en_IN`, `en_NZ`, `en_PH`, `en_TH`, `en_US`, `es`, `es_AR`, `es_CA`, `es_CL`, `es_CO`, `es_ES`, `es_MX`, `et_EE`, `fa_IR`, `fi_FI`, `fil_PH`, `fr_BE`, `fr_CA`, `fr_CH`, `fr_FR`, `fr_QC`, `ga_IE`, `he_IL`, `hi_IN`, `hr_HR`, `hu_HU`, `hy_AM`, `id_ID`, `it_CH`, `it_IT`, `ja_JP`, `ka_GE`, `ko_KR`, `la`, `lb_LU`, `lt_LT`, `lv_LV`, `mt_MT`, `ne_NP`, `nl_BE`, `nl_NL`, `no_NO`, `or_IN`, `pl_PL`, `pt_BR`, `pt_PT`, `ro_RO`, `ru_RU`, `sk_SK`, `sl_SI`, `sq_AL`, `sv_SE`, `ta_IN`, `th`, `th_TH`, `tl_PH`, `tr_TR`, `tw_GH`, `uk_UA`, `vi_VN`, `zh_CN`, `zh_TW`  |






**Examples**



<span style="color: var(--md-typeset-a-color);">1. Generate fake italian name</span>









=== "EU"

    ```sql
    select bigfunctions.eu.faker("name", "it_IT")
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.faker("name", "it_IT")
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.faker("name", "it_IT")
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| fake_data        |
+------------------+
| Michela Beccaria |
+------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. Generate fake IPv4 address (without specifying locale)</span>









=== "EU"

    ```sql
    select bigfunctions.eu.faker("ipv4_private", null)
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.faker("ipv4_private", null)
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.faker("ipv4_private", null)
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+---------------+
| fake_data     |
+---------------+
| 10.52.207.187 |
+---------------+
</code>
</pre>









