You have a table storing Unix timestamps (integers representing seconds since 1970-01-01 00:00:00 UTC). You want to convert these timestamps into BigQuery TIMESTAMP format, but at different levels of granularity.  Here are a few use cases:

* **Analyzing data by year:** You have event data with Unix timestamps and you want to analyze trends year by year.  You can use `timestamp_from_unix_date_time(unix_timestamp, 'YEAR')` to truncate the timestamps to the beginning of each year, then group your data by this truncated timestamp.

```sql
SELECT
  bigfunctions.us.timestamp_from_unix_date_time(event_timestamp, 'YEAR') AS event_year,
  COUNT(*) AS event_count
FROM
  `your_project.your_dataset.your_table`
GROUP BY
  event_year
ORDER BY
  event_year;
```


* **Generating reports by month:**  You want to create monthly reports based on user activity. You have user activity timestamps stored as Unix timestamps. Use `timestamp_from_unix_date_time(unix_timestamp, 'MONTH')`  to get the beginning of the month for each activity, and then aggregate data accordingly.

```sql
SELECT
  bigfunctions.us.timestamp_from_unix_date_time(activity_timestamp, 'MONTH') AS activity_month,
  COUNT(DISTINCT user_id) AS active_users
FROM
  `your_project.your_dataset.user_activity`
GROUP BY
  activity_month
ORDER BY
  activity_month;
```


* **Data bucketing/aggregation:** You want to group events into hourly buckets. You can use `timestamp_from_unix_date_time(unix_timestamp, 'HOUR')` to truncate timestamps to the beginning of each hour, enabling easy grouping and aggregation.


```sql
SELECT
  bigfunctions.us.timestamp_from_unix_date_time(event_timestamp, 'HOUR') AS event_hour,
  SUM(event_value) AS total_value
FROM
  `your_project.your_dataset.events`
GROUP BY
  event_hour
ORDER BY
  event_hour;

```

* **Simplifying date comparisons:**  Sometimes, you only care about the date part of a timestamp.  Using `timestamp_from_unix_date_time(unix_timestamp, 'DAY')` effectively converts the Unix timestamp to a date, allowing for straightforward date comparisons without dealing with the time component.


```sql
SELECT *
FROM `your_project.your_dataset.events`
WHERE bigfunctions.us.timestamp_from_unix_date_time(event_timestamp, 'DAY') = '2024-03-15';
```

These examples demonstrate the flexibility of the function to handle different levels of time granularity based on the `date_time_part` argument, enabling a variety of time-based analysis and reporting tasks. Remember to replace  `your_project.your_dataset.your_table` with your actual table information and the correct regional dataset for `bigfunctions`.
