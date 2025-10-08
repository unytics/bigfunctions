---
title: "BigFunctions Supercharge BigQuery"
description: |
  SQL is all you need!
  BigFunctions supercharge BigQuery
  so that you can perform any task with SQL
hide:
  - navigation
  - toc
---


<!------------- POWER OF FUNCTIONS HEADER  ----------->
<div class="hero" markdown>

# Powerful Functions to Supercharge BigQuery

**150+ Ready-to-Go Functions** from the community *(no install needed)*

[Discover the Functions :octicons-arrow-right-24:](bigfunctions/README.md){ .md-button }


</div>


<figure markdown="span">
  ![functions examples](assets/functions.png)
  <figcaption>BigQuery can now perform any task with SQL</figcaption>
</figure>


<br>



---






<!------------- FRAMEWORK  ----------->

<div class="hero" markdown>

# A Framework for BigQuery functions

Build your own catalog of advanced functions.

[Discover the Framework :octicons-arrow-right-24:](framework.md){ .md-button }

![bigfun command line interface](assets/bigfun.png){ style="max-width: 400px; width: 100%" }


</div>


<br>

---


<!------------- THE RISE OF SQL DATA STACK  ----------->

<div class="hero" markdown>

# Keep it Simple<br>with SQL-Data-Stack

**BigQuery**, **BigFunctions** and **dataform**<br>
is all you need

[Discover the SQL Data Stack :octicons-arrow-right-24:](https://medium.com/google-cloud/sql-is-all-you-need-77554fea90c0){ .md-button target="_blank" }

</div>

<div class="grid cards text-center" markdown>

-   **BigQuery** runs SQL

    ![bigquery logo](assets/bigquery.png){ style="max-height: 50px" }

-   **BigFunctions** supercharges SQL

    ![bigfunctions logo](assets/logo_and_name.png){ style="max-height: 50px" }


-   **dataform** orchestrates SQL

    ![dataform logo](assets/dataform.jpeg.jpg){ style="max-height: 50px" }

</div>


<div class="hero" markdown>

**dataform can be replaced by any sql orchestrator (dbt, sqlmesh, scheduled queries, etc)*
{ .small }

</div>


## Want to get an email from BigQuery with your KPIs of the day? 
### It's as easy as a copy & paste!

To send you an email with your KPIs of the day, simply copy the following code and run it in BigQuery. 
One Click & you got your email. No install needed!

``` sql
with 

# Compute the KPIs of the day
kpis_of_the_day as (
  select 
    1584  as total_users,
    74863.35 as total_revenue
),

# Set email recipients (you in this case)
recipients as (
  select 
    session_user() as email,
    initcap(replace(split(session_user(), '@')[offset(0)], '.', ' ')) as username,
)


# Send an Email to recipients (you) with the KPIs of the day
select bigfunctions.eu.send_mail(

  email,                    # Recipient

  "Daily Metrics Summary",  # Email Subject

  format(                   # Email Body in markdown format
    """
    ## Hi %s

    *Here is your Daily Metrics Summary*
    
    - **Total users**: %d
    - **Total revenue**: %.2f $

    Enjoy your day!    
    """,
    username,
    total_users,
    total_revenue
  ),
  null,                   # Optional Attached file name
  null                    # Optional Attached file content
)

from kpis_of_the_day, recipients
```


<!------------- TECHNOLOGIES UPON SECTION  ----------->
<div class="hero" markdown>

*Taking the most of*
{ .small }

<figure markdown="span">
  ![gcp](assets/gcp.svg){ .gray-scale .mt-neg width=200 }
</figure>

</div>

<br>
<br>
