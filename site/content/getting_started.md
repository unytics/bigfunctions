---
title: "BigFunctions"
ogtitle: "BigFunctions supercharge BigQuery"
description: "BigFunctions are open-source BigQuery routines that give you SQL-superpowers. BigFunctions can show data-visualizations inside BigQuery console, compute advanced transforms such as sentiment score of a text, or send data to any of your favorite SAAS tool. BigFunctions is dbt's best friend."
image: "https://unytics.io/bigfunctions/assets/logo_and_name.png"
image_alt: "Supercharge BigQuery with BigFunctions"
image_width: "2500"
image_height: "541"
hide:
  - navigation
---

# Getting Started

!!! note ""

    BigFunctions are open-source BigQuery routines that give you **SQL-superpowers** in BigQuery 💪.

    There are **6 must know** to use them:

    1. Location is important
    2. Be patient
    3. Beware of BigQuery costs
    4. We log executions
    5. BigFunctions are open
    6. Please help us & make suggestions --> contact@unytics.io


## 🌍 Location is important

BigQuery routines must be located at the same location as your data. Otherwise the BigFunction OR your data will not be found by BigQuery. To explore your table `your-project.your_dataset.your_table` use one of the following commands regarding the location of `your_dataset`:


=== "`your_dataset` is in EU"

    ```sql
    call bigfunctions.eu.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in US"

    ```sql
    call bigfunctions.us.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-east1"

    ```sql
    call bigfunctions.asia_east1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-east2"

    ```sql
    call bigfunctions.asia_east2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-northeast1"

    ```sql
    call bigfunctions.asia_northeast1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-northeast2"

    ```sql
    call bigfunctions.asia_northeast2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-northeast3"

    ```sql
    call bigfunctions.asia_northeast3.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-south1"

    ```sql
    call bigfunctions.asia_south1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-south2"

    ```sql
    call bigfunctions.asia_south2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-southeast1"

    ```sql
    call bigfunctions.asia_southeast1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in asia-southeast2"

    ```sql
    call bigfunctions.asia_southeast2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in australia-southeast1"

    ```sql
    call bigfunctions.australia_southeast1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in australia-southeast2"

    ```sql
    call bigfunctions.australia_southeast2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-central2"

    ```sql
    call bigfunctions.europe_central2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-north1"

    ```sql
    call bigfunctions.europe_north1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-west1"

    ```sql
    call bigfunctions.europe_west1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-west2"

    ```sql
    call bigfunctions.europe_west2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-west3"

    ```sql
    call bigfunctions.europe_west3.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-west4"

    ```sql
    call bigfunctions.europe_west4.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in europe-west6"

    ```sql
    call bigfunctions.europe_west6.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in northamerica-northeast1"

    ```sql
    call bigfunctions.northamerica_northeast1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in northamerica-northeast2"

    ```sql
    call bigfunctions.northamerica_northeast2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in southamerica-east1"

    ```sql
    call bigfunctions.southamerica_east1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in southamerica-west1"

    ```sql
    call bigfunctions.southamerica_west1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-central1"

    ```sql
    call bigfunctions.us_central1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-east1"

    ```sql
    call bigfunctions.us_east1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-east4"

    ```sql
    call bigfunctions.us_east4.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-west1"

    ```sql
    call bigfunctions.us_west1.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-west2"

    ```sql
    call bigfunctions.us_west2.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-west3"

    ```sql
    call bigfunctions.us_west3.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```

=== "`your_dataset` is in us-west4"

    ```sql
    call bigfunctions.us_west4.explore_table("your-project.your_dataset.your_table");
    select html from bigfunction_result;
    ```



---




## ⌛ Be patient

For instance `explore_table` can take several minutes to compute the statistics of the table. The reason is that it computes multiple queries for each column.


## 💰 Beware of BigQuery costs

BigFunctions make BigQuery queries from your project so incur costs like any BigQuery query. For instance, `explore_table` function incurs a full-scan of your table. Consider creating smaller tables by sampling large ones if needed to use them with BigFunctions.


## 📝 We log executions

We log executions of remote functions to manage quotas and costs. Collected data include: timestamp of execution, name of executed BigFunction and the user email who executed them. We will never share these emails to anyone. We don't log function arguments data. If this seems unfair to you please contact contact@unytics.io.


## 😮 BigFunctions are open

You can inspect the source code of any deployed SQL and js function at any time by pinning the `bigfunctions` project in BigQuery console and exploring routines. What's more you will find the github link to each BigFunction configuration file in the documentation.
