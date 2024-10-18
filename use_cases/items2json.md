Let's say you have a BigQuery table that stores product information, including a set of custom attributes for each product.  These attributes are stored as key-value pairs in an array.  You want to transform this array of key-value pairs into a JSON object for easier processing or export.

**Example Table:**

```
CREATE OR REPLACE TABLE `your_project.your_dataset.products` (
  product_id INT64,
  product_name STRING,
  attributes ARRAY<STRUCT<key STRING, value STRING>>
);

INSERT INTO `your_project.your_dataset.products` (product_id, product_name, attributes) VALUES
(1, 'Product A', [('color', 'red'), ('size', 'large'), ('material', 'cotton')]),
(2, 'Product B', [('color', 'blue'), ('weight', '10kg')]);
```

**Using `items2json`:**

You can use the `items2json` function to convert the `attributes` array into a JSON object:

```sql
SELECT
  product_id,
  product_name,
  bigfunctions.your_region.items2json(attributes) AS attributes_json
FROM
  `your_project.your_dataset.products`;
```

**Result:**

```
+------------+--------------+---------------------------------------------------+
| product_id | product_name | attributes_json                                   |
+------------+--------------+---------------------------------------------------+
|          1 | Product A    | {"color": "red", "size": "large", "material": "cotton"} |
|          2 | Product B    | {"color": "blue", "weight": "10kg"}                |
+------------+--------------+---------------------------------------------------+
```

Now, the `attributes_json` column contains a JSON representation of the product attributes, making it easier to work with in downstream processes.  For instance, you could easily extract individual attribute values using JSON functions or export the data in a JSON format.


Another use case could be dynamically constructing JSON payloads for API calls based on data stored in key-value pairs in BigQuery.  Or you might use it to simplify the representation of complex data structures within BigQuery for analysis or reporting purposes.
