You have a table in BigQuery containing a column with JSON strings representing product details. Each JSON string has a flat structure (no nested objects).  You want to extract the key-value pairs from these JSON strings and analyze them.

**Example Table:**

```
products
| product_id | details                                    |
|------------|--------------------------------------------|
| 1          | '{"name": "Laptop", "price": "1200", "brand": "XYZ"}' |
| 2          | '{"name": "Mouse", "price": "25", "brand": "ABC"}'   |
| 3          | '{"name": "Keyboard", "price": "75", "brand": "XYZ"}'|
```


**Query using `json_items`:**

```sql
SELECT
    product_id,
    item.key,
    item.value
  FROM
    `your-project.your_dataset.products`,
    UNNEST(bigfunctions.your-region.json_items(details)) AS item;
```

**Result:**

```
| product_id | key    | value |
|------------|--------|-------|
| 1          | name   | Laptop|
| 1          | price  | 1200  |
| 1          | brand  | XYZ   |
| 2          | name   | Mouse |
| 2          | price  | 25    |
| 2          | brand  | ABC   |
| 3          | name   | Keyboard |
| 3          | price  | 75    |
| 3          | brand  | XYZ   |
```

This allows you to easily query and analyze individual attributes of the products, such as finding all products of a certain brand or within a specific price range.  You've effectively transformed semi-structured JSON data into a relational format for easier analysis with standard SQL.  Remember to replace `your-project`, `your_dataset`, and `your-region` with your actual values.
