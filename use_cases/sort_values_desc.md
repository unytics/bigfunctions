You have a table of product sales with columns like `product_id` and `sales_amount`.  You want to find the top 3 products by sales in descending order. You can use `sort_values_desc` within an aggregation to achieve this:

```sql
SELECT product_id
FROM `your_project.your_dataset.your_sales_table`
GROUP BY product_id
ORDER BY bigfunctions.YOUR_REGION.sort_values_desc(ARRAY_AGG(sales_amount)) DESC
LIMIT 3
```

**Explanation:**

1. **`ARRAY_AGG(sales_amount)`**:  For each `product_id`, this gathers all the `sales_amount` values into an array.
2. **`sort_values_desc(...)`**: This sorts the array of sales amounts in descending order.  The highest sales amount will now be the first element in each array.
3. **`ORDER BY ... DESC`**: This orders the `product_id` groups based on the sorted sales amount arrays in descending order. Since the largest sales amount is the first element of each array after sorting, ordering by the array itself (descending) effectively orders by the highest sales amount.
4. **`LIMIT 3`**: This returns only the top 3 `product_id`s based on the ordering.

**Another Use Case (Data Cleaning):**

Imagine you have a table with a column containing lists of dates (perhaps representing important events related to a customer). These date lists might be in any order. You want to consistently store these dates in descending chronological order.  You could use `sort_values_desc`:

```sql
SELECT
    customer_id,
    bigfunctions.YOUR_REGION.sort_values_desc(dates_array) AS sorted_dates
FROM
    `your_project.your_dataset.your_customer_table`
```

This would update or create a new column `sorted_dates` with the dates arranged from most recent to oldest.


Remember to replace `YOUR_REGION` with the appropriate BigQuery region (e.g., `us`, `eu`, `asia-northeast1`, etc.) that corresponds to your dataset's location.
