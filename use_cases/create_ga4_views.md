## Steps to Query GA4 Data Efficiently Using BigFunctions

**1. Create a Destination Dataset**

Prepare a dataset in BigQuery where the GA4 table functions will be stored. For example:

```sql
create schema `Ga4-Project.ga4_bigquery_queries`;
```

<br>

**2. Call the GA4 View Creation Function**

Use the bigfunction to create table functions for querying GA4 data. For example:

```sql
call bigfunctions.us.create_ga4_views(

  'Ga4-Project.analytics_310989290',

  'Ga4-Project.ga4_bigquery_queries'

);
```

![image](https://github.com/user-attachments/assets/012c6c6f-d8a5-446c-bf57-515708453bcd)

<br>

**3. Wait for the function to process and create all necessary table functions.**

Once completed, all table functions (queries) are available in your destination dataset.

<br>

**4. Query GA4 Data Using Table Functions**

You can now query specific GA4 data efficiently with date ranges by calling the created table functions. For example:

```sql
select *
from `Ga4-Project.ga4_bigquery_queries`.event_scope__flatten_events('2024-11-01', '2024-12-01');
```

Replace '2024-11-01' and '2024-12-01' with your desired date range.
