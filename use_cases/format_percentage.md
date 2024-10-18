You're an analyst for an e-commerce company and you need to calculate and display the conversion rate for different marketing campaigns.  You have a table with the number of clicks and the number of resulting purchases for each campaign.

```sql
WITH campaign_data AS (
    SELECT
        'Campaign A' AS campaign_name,
        1000 AS clicks,
        50 AS purchases
    UNION ALL
    SELECT
        'Campaign B' AS campaign_name,
        500 AS clicks,
        20 AS purchases
    UNION ALL
    SELECT
        'Campaign C' AS campaign_name,
        2000 AS clicks,
        150 AS purchases

)

SELECT
    campaign_name,
    bigfunctions.us.format_percentage(purchases, clicks, 2) AS conversion_rate
FROM campaign_data;
```

This query uses the `format_percentage` function to calculate the conversion rate (purchases / clicks) for each campaign and format it as a percentage with two decimal places.  The result would be a table like this:

```
+---------------+----------------+
| campaign_name | conversion_rate |
+---------------+----------------+
| Campaign A    | 5.00 %         |
| Campaign B    | 4.00 %         |
| Campaign C    | 7.50 %         |
+---------------+----------------+
```

This makes it easy to compare the effectiveness of different campaigns in a human-readable format.  You could also use this function to calculate and display other percentages, such as sales growth rates, discount percentages, or return rates.
