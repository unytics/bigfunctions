You have a table of products, and each product has a list of prices at different stores.  You want to find the highest price for each product.

```sql
WITH Products AS (
    SELECT
        'Product A' AS product_name,
        [10.99, 12.50, 11.75] AS prices
    UNION ALL SELECT
        'Product B' AS product_name,
        [5.00, 5.50, 4.99] AS prices
    UNION ALL SELECT
        'Product C' AS product_name,
        [20.00, 19.50, 21.25] AS prices
)
SELECT
    product_name,
    bigfunctions.us.max_value(prices) AS max_price
FROM Products;
```

This query uses the `max_value` function to find the highest price within the `prices` array for each product. The result will be:

```
+-------------+-----------+
| product_name | max_price |
+-------------+-----------+
| Product A    | 12.5      |
| Product B    | 5.5       |
| Product C    | 21.25     |
+-------------+-----------+
```

This shows how `max_value` can be practically used to extract the maximum value from an array of numbers within a larger dataset.  This could be useful for things like pricing analysis, finding peak values in time series data (if stored as arrays), or determining the maximum score in a game played multiple times.
