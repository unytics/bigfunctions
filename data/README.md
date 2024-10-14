---
title: "Tables"
description: "Catalog of open-source Tables"
---

!!! note ""

    **✅ The following public tables** are

    - deployed in `bigfunctions` GCP project in 39 datasets for all of the 39 BigQuery regions.
    - They are public, so they can be read by anyone under the eventual license given in the description of the table.
    - For any question or difficulties, please read [Getting Started](../).
    - If you prefer to create the tables in your own project, read [Getting Started](../).
    - Found a bug? Please raise an issue [here](https://github.com/unytics/bigfunctions/issues/new/choose)

??? info "All BigFunctions Datasets >"

    | Region | Dataset |
    |--------|---------|
    | `EU` | `bigfunctions.eu` |
    | `US` | `bigfunctions.us` |
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
    | `europe-west1` | `bigfunctions.europe_west1` |
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






---



### holidays
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/holidays.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Contains national public holidays for every country.

Dates were issued from [holidays python package](https://pypi.org/project/holidays/) with:

```python
import holidays
countries = holidays.utils.list_supported_countries()
for country in countries:
    dates = holidays.country_holidays(country, years=range(1975, 2077))
    dates = sorted([str(date) for date in dates.keys()])
    print('\\n'.join(f'{country},{date}' for date in dates))
```



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| country | string | country code |
| date | date | public holiday local date |


---



### natality
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/natality.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Copy of bigquery-public-data.samples.natality public table.

The table was created with:

```SQL
CREATE TABLE `bigfunctions.us.natality`
(
  source_year INT64 NOT NULL OPTIONS(description="Four-digit year of the birth. Example: 1975."),
  year INT64 OPTIONS(description="Four-digit year of the birth. Example: 1975."),
  month INT64 OPTIONS(description="Month index of the date of birth, where 1=January."),
  day INT64 OPTIONS(description="Day of birth, starting from 1."),
  wday INT64 OPTIONS(description="Day of the week, where 1 is Sunday and 7 is Saturday."),
  state STRING OPTIONS(description="The two character postal code for the state. Entries after 2004 do not include this value."),
  is_male BOOL NOT NULL OPTIONS(description="TRUE if the child is male, FALSE if female."),
  child_race INT64 OPTIONS(description="The race of the child. One of the following numbers:\n\n1 - White\n2 - Black\n3 - American Indian\n4 - Chinese\n5 - Japanese\n6 - Hawaiian\n7 - Filipino\n9 - Unknown/Other\n18 - Asian Indian\n28 - Korean\n39 - Samoan\n48 - Vietnamese"),
  weight_pounds FLOAT64 OPTIONS(description="Weight of the child, in pounds."),
  plurality INT64 OPTIONS(description="How many children were born as a result of this pregnancy. twins=2, triplets=3, and so on."),
  apgar_1min INT64 OPTIONS(description="Apgar scores measure the health of a newborn child on a scale from 0-10. Value after 1 minute. Available from 1978-2002."),
  apgar_5min INT64 OPTIONS(description="Apgar scores measure the health of a newborn child on a scale from 0-10. Value after 5 minutes. Available from 1978-2002."),
  mother_residence_state STRING OPTIONS(description="The two-letter postal code of the mother's state of residence when the child was born."),
  mother_race INT64 OPTIONS(description="Race of the mother. Same values as child_race."),
  mother_age INT64 OPTIONS(description="Reported age of the mother when giving birth."),
  gestation_weeks INT64 OPTIONS(description="The number of weeks of the pregnancy."),
  lmp STRING OPTIONS(description="Date of the last menstrual period in the format MMDDYYYY. Unknown values are recorded as \"99\" or \"9999\"."),
  mother_married BOOL OPTIONS(description="True if the mother was married when she gave birth."),
  mother_birth_state STRING OPTIONS(description="The two-letter postal code of the mother's birth state."),
  cigarette_use BOOL OPTIONS(description="True if the mother smoked cigarettes. Available starting 2003."),
  cigarettes_per_day INT64 OPTIONS(description="Number of cigarettes smoked by the mother per day. Available starting 2003."),
  alcohol_use BOOL OPTIONS(description="True if the mother used alcohol. Available starting 1989."),
  drinks_per_week INT64 OPTIONS(description="Number of drinks per week consumed by the mother. Available starting 1989."),
  weight_gain_pounds INT64 OPTIONS(description="Number of pounds gained by the mother during pregnancy."),
  born_alive_alive INT64 OPTIONS(description="Number of children previously born to the mother who are now living."),
  born_alive_dead INT64 OPTIONS(description="Number of children previously born to the mother who are now dead."),
  born_dead INT64 OPTIONS(description="Number of children who were born dead (i.e. miscarriages)"),
  ever_born INT64 OPTIONS(description="Total number of children to whom the woman has ever given birth (includes the current birth)."),
  father_race INT64 OPTIONS(description="Race of the father. Same values as child_race."),
  father_age INT64 OPTIONS(description="Age of the father when the child was born."),
  record_weight INT64 OPTIONS(description="1 or 2, where 1 is a row from a full-reporting area, and 2 is a row from a 50% sample area.")
)
as
select * from `bigquery-public-data.samples.natality` tablesample system (10 percent)
```



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| source_year | INT64 | Four-digit year of the birth. Example: 1975. |
| year | INT64 | Four-digit year of the birth. Example: 1975. |
| month | INT64 | Month index of the date of birth, where 1=January. |
| day | INT64 | Day of birth, starting from 1. |
| wday | INT64 | Day of the week, where 1 is Sunday and 7 is Saturday. |
| state | STRING | The two character postal code for the state. Entries after 2004 do not include this value. |
| is_male | BOOL | TRUE if the child is male, FALSE if female. |
| child_race | INT64 | The race of the child. One of the following numbers:<br><br>1 - White<br>2 - Black<br>3 - American Indian<br>4 - Chinese<br>5 - Japanese<br>6 - Hawaiian<br>7 - Filipino<br>9 - Unknown/Other<br>18 - Asian Indian<br>28 - Korean<br>39 - Samoan<br>48 - Vietnamese |
| weight_pounds | FLOAT64 | Weight of the child, in pounds. |
| plurality | INT64 | How many children were born as a result of this pregnancy. twins=2, triplets=3, and so on. |
| apgar_1min | INT64 | Apgar scores measure the health of a newborn child on a scale from 0-10. Value after 1 minute. Available from 1978-2002. |
| apgar_5min | INT64 | Apgar scores measure the health of a newborn child on a scale from 0-10. Value after 5 minutes. Available from 1978-2002. |
| mother_residence_state | STRING | The two-letter postal code of the mother's state of residence when the child was born. |
| mother_race | INT64 | Race of the mother. Same values as child_race. |
| mother_age | INT64 | Reported age of the mother when giving birth. |
| gestation_weeks | INT64 | The number of weeks of the pregnancy. |
| lmp | STRING | Date of the last menstrual period in the format MMDDYYYY. Unknown values are recorded as "99" or "9999". |
| mother_married | BOOL | True if the mother was married when she gave birth. |
| mother_birth_state | STRING | The two-letter postal code of the mother's birth state. |
| cigarette_use | BOOL | True if the mother smoked cigarettes. Available starting 2003. |
| cigarettes_per_day | INT64 | Number of cigarettes smoked by the mother per day. Available starting 2003. |
| alcohol_use | BOOL | True if the mother used alcohol. Available starting 1989. |
| drinks_per_week | INT64 | Number of drinks per week consumed by the mother. Available starting 1989. |
| weight_gain_pounds | INT64 | Number of pounds gained by the mother during pregnancy. |
| born_alive_alive | INT64 | Number of children previously born to the mother who are now living. |
| born_alive_dead | INT64 | Number of children previously born to the mother who are now dead. |
| born_dead | INT64 | Number of children who were born dead (i.e. miscarriages) |
| ever_born | INT64 | Total number of children to whom the woman has ever given birth (includes the current birth). |
| father_race | INT64 | Race of the father. Same values as child_race. |
| father_age | INT64 | Age of the father when the child was born. |
| record_weight | INT64 | 1 or 2, where 1 is a row from a full-reporting area, and 2 is a row from a 50% sample area. |


---



### sales
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/sales.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Sales



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| product_id | int64 | Product Identifier |
| price | float64 | Unit Price of product |
| quantity | int64 | Quantity of this product sold |
| sale_date | date | Sale date |


---



### sample_graph
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/sample_graph.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Example of a graph represented as a list of edges between pair of nodes



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| node1 | int64 | node id connected to node2 |
| node2 | int64 | node id connected to node1 |


---



### translated_days
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/translated_days.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Days translations for each locale

This csv was generated by:
```python
import datetime
import locale
languages = [locale for locale in locale.locale_alias if '.' not in locale and '@' not in locale]
dates = [datetime.datetime(2023, 1, day) for day in range(1, 8)]
with open('data/translated_days.csv', 'w', encoding='utf-8') as out:
    for language in languages:
        try:
            locale.setlocale(locale.LC_TIME, language)
            for k, date in enumerate(dates):
                name = date.strftime("%A")
                out.write(f'{language},{k + 1},{name}\n')
        except:
            pass
```



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| locale | string | Locale such as 'en' or 'en_en' |
| day_nb | int64 | Day as integer from 1 to 7 with Sunday as 1 |
| translated_day | string | Translated day name for locale |


---



### translated_months
<div style="position: relative; top: -2rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">

  <a href="https://github.com/unytics/bigfunctions/blob/main/data/translated_months.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a></div>

**Description**

Months translations for each locale

This csv was generated by:
```python
import datetime
import locale
languages = [locale for locale in locale.locale_alias if '.' not in locale and '@' not in locale]
with open('translated_months.csv', 'w', encoding='utf-8') as out:
    for language in languages:
        try:
            locale.setlocale(locale.LC_TIME, language)
            for month in range(0, 12):
                month = month + 1
                date = datetime.datetime(2023, month, 1)
                name = date.strftime("%B")
                out.write(f'{language},{month},{name}\n')
        except:
            pass
```



**Schema**

| Column  | Type | Description  |
|---------|------|--------------|
| locale | string | Locale such as 'en' or 'en_en' |
| month_nb | int64 | Month as integer from 1 to 12 |
| translated_month | string | Translated month name for locale |


---
