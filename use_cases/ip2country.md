You have a table of website access logs, and each record includes the IP address of the visitor. You want to analyze website traffic by country.  The `ip2country` function can be used to determine the country code associated with each IP address, allowing you to aggregate and analyze traffic patterns based on visitor location.

```sql
SELECT
    bigfunctions.us.ip2country(client_ip) AS country_code,
    COUNT(*) AS visit_count
FROM
    `your_project.your_dataset.website_logs`
GROUP BY
    country_code
ORDER BY
    visit_count DESC;
```

This query uses the `ip2country` function to add a `country_code` column to the `website_logs` table. Then, it groups the data by `country_code` and counts the number of visits from each country, providing a summary of website traffic by country of origin. Remember to replace `your_project.your_dataset.website_logs` with the actual path to your website logs table and choose the correct BigFunctions dataset according to your region (e.g., `bigfunctions.eu`, `bigfunctions.asia_northeast1`).
