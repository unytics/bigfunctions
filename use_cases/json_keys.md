You have a BigQuery table containing a column with JSON strings representing product information. Each JSON string has a flat structure (no nested objects) with keys like "product_name", "price", "category", etc. You want to extract all the keys present in these JSON strings.

**Example Table:**

| product_info (STRING) |
|---|---|
| `{"product_name": "Laptop", "price": 1200, "category": "electronics"}` |
| `{"product_name": "T-shirt", "category": "clothing", "color": "blue"}` |
| `{"price": 25, "product_name": "Book", "author": "Jane Doe"}` |


**Query using `json_keys`:**

```sql
SELECT bigfunctions.us.json_keys(product_info) AS keys
FROM `your_project.your_dataset.your_table`;
```

**Result:**

| keys (ARRAY<STRING>) |
|---|---|
| `["product_name", "price", "category"]` |
| `["product_name", "category", "color"]` |
| `["price", "product_name", "author"]` |


This allows you to dynamically determine the keys present in each JSON string without hardcoding them. You could then use this information for various purposes like:

* **Schema validation:** Verify that all expected keys are present in the JSON data.
* **Data transformation:**  Create new columns based on the extracted keys.
* **Dynamic querying:** Construct queries that access fields within the JSON based on the available keys.
* **Data analysis:** Analyze the frequency of different keys to understand the structure of your JSON data. 
