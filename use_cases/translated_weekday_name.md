A company has a database of customer orders with timestamps. They want to generate reports based on the day of the week, but need the reports to be localized for different regions.

For example, they might want to generate a report showing the total sales for each day of the week in French for their French-speaking customers, and a separate report in Spanish for their Spanish-speaking customers.

Using the `translated_weekday_name` function, they can achieve this easily. They can query their order data, extract the weekday from the timestamp, and then use the function to translate the weekday name into the desired language.  A simplified example in BigQuery SQL (assuming the dataset is in the EU region) would be:

```sql
SELECT
    bigfunctions.eu.translated_weekday_name(EXTRACT(DATE from order_timestamp), 'fr') AS french_weekday,
    SUM(order_total) AS total_sales
  FROM
    `your_project.your_dataset.your_orders_table`
  GROUP BY 1
  ORDER BY 1
```

This would output a table showing the total sales for each day of the week, with the weekday name translated into French. They could then repeat the query with a different language code (e.g., 'es' for Spanish) to generate a localized report for a different region.
