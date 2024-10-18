You have a table of customer orders, and each order contains an array of item prices. You want to calculate the total value of each order.

**Table Schema (Example):**

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.orders` AS (
  SELECT 1 AS order_id, [10.50, 25.00, 5.99] AS item_prices UNION ALL
  SELECT 2 AS order_id, [150.00, 12.75] AS item_prices UNION ALL
  SELECT 3 AS order_id, [5.00, 5.00, 5.00, 5.00] AS item_prices
);
```

**Query using `sum_values`:**

```sql
SELECT
    order_id,
    bigfunctions.us.sum_values(item_prices) AS total_order_value  -- Replace 'us' with your region
  FROM
    `your_project.your_dataset.orders`;
```

**Result:**

```
+---------+-----------------+
| order_id | total_order_value |
+---------+-----------------+
|       1 |            41.49 |
|       2 |           162.75 |
|       3 |            20.00 |
+---------+-----------------+
```


This use case demonstrates how `sum_values` simplifies the process of summing elements within an array, eliminating the need for more complex SQL involving unnest and aggregate functions.  It's a very practical application for e-commerce, inventory management, and other scenarios where you need to work with arrays of numeric values.
