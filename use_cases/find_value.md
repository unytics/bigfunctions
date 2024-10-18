You have a table of customer orders, and each order has an array of product IDs.  You want to find the position of a specific product ID within each order's product array.

**Table Schema:**

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.orders` (
  order_id INT64,
  product_ids ARRAY<INT64>
);

INSERT INTO `your_project.your_dataset.orders` (order_id, product_ids) VALUES
(1, [101, 102, 103, 104]),
(2, [102, 105, 106]),
(3, [101, 103, 107, 102]);
```

**Use Case: Finding the position of product ID 102:**

```sql
SELECT
    order_id,
    bigfunctions.your_region.find_value(product_ids, 102) AS product_102_position
  FROM
    `your_project.your_dataset.orders`;
```

**Result:**

```
+---------+----------------------+
| order_id | product_102_position |
+---------+----------------------+
|       1 |                    1 |
|       2 |                    0 |
|       3 |                    3 |
+---------+----------------------+
```

**Explanation:**

* The `find_value` function searches the `product_ids` array for the value `102`.
* It returns the zero-based index (position) of the first occurrence of `102`.
* For `order_id = 1`, `102` is at index 1.
* For `order_id = 2`, `102` is at index 0.
* For `order_id = 3`, `102` is at index 3.


**Other Potential Use Cases:**

* **Inventory Management:**  Find the location of a specific item within a warehouse represented as an array.
* **Log Analysis:** Find the first occurrence of a specific error code within a log entry containing an array of codes.
* **User Behavior Analysis:**  Determine the position of a specific action within a user's sequence of actions on a website.


Remember to replace `your_project`, `your_dataset`, and `your_region` with your actual values.  For example, if your dataset is in the `us-central1` region, you would use `bigfunctions.us_central1`.
