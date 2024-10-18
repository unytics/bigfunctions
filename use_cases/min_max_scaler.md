Let's say you have a table of product prices and you want to compare their relative affordability. The prices range from $10 to $1000, but you need them on a normalized scale between 0 and 1 for a machine learning model or visualization.  Here's how `min_max_scaler` can be used:

```sql
WITH ProductPrices AS (
    SELECT 'Product A' AS product, 10 AS price
    UNION ALL SELECT 'Product B' AS product, 50 AS price
    UNION ALL SELECT 'Product C' AS product, 200 AS price
    UNION ALL SELECT 'Product D' AS product, 1000 AS price
),
MinMaxScaledPrices AS (
  SELECT
      product,
      bigfunctions.us.min_max_scaler(ARRAY_AGG(price) OVER ()) AS scaled_prices
  FROM ProductPrices
)
SELECT
    product,
    scaled_price
FROM MinMaxScaledPrices, UNARRAY(scaled_prices) AS scaled_price;

```

This query first collects all prices into an array using `ARRAY_AGG`.  Then, `min_max_scaler` normalizes these prices within the array.  Finally, the `UNARRAY` function expands the resulting array so you get each product and its scaled price on separate rows.

This results in a table like this (the exact values might vary slightly due to floating-point precision):

| product    | scaled_price |
|------------|--------------|
| Product A  | 0            |
| Product B  | 0.04         |
| Product C  | 0.19         |
| Product D  | 1            |

Now "Product A", with the lowest price, has a scaled price of 0, and "Product D", with the highest price, has a scaled price of 1.  The other products have scaled prices in between, reflecting their relative affordability.


Another use case would be normalizing features in a machine learning preprocessing step directly within BigQuery before exporting the data for training.  This can simplify your data pipeline.
