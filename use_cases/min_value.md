You have a table of products, and each product has an array of prices representing its price history. You want to find the lowest price ever recorded for each product.

```sql
WITH Products AS (
    SELECT
        'Product A' AS product_name,
        [10, 12, 8, 15, 9] AS prices
    UNION ALL
    SELECT
        'Product B' AS product_name,
        [20, 18, 18, 19, 21] AS prices
    UNION ALL
    SELECT
        'Product C' AS product_name,
        [5, 7, 5, 6, 4] AS prices
)
SELECT
    product_name,
    bigfunctions.us.min_value(prices) AS min_price
FROM Products;
```

This query would utilize the `min_value` function to efficiently determine the minimum value within the `prices` array for each product, effectively identifying the historical lowest price.  You would replace `bigfunctions.us` with the appropriate dataset for your region.
