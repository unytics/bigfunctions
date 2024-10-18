Let's illustrate the `upsert` function with a concrete use case: managing a product catalog in BigQuery.

**Scenario:** You have a BigQuery table called `product_catalog` that stores information about your products.  You receive regular updates about product information from various sources, and you need to efficiently update your `product_catalog` table with these changes.

**Table Schema (product_catalog):**

* `product_id` (STRING): Unique identifier for each product (primary key)
* `name` (STRING): Product name
* `price` (NUMERIC): Product price
* `description` (STRING): Product description
* `last_updated` (TIMESTAMP): Timestamp indicating the last update time

**Update Data:** You receive a new batch of product updates in another table or as the result of a query. This data may contain new products, updates to existing products, or even information about products that need to be removed.

**Use Case Examples:**

**1. Delta Update (Insert and Update):**

You want to insert new products and update existing ones based on the latest information.  You use the `delta` insertion mode and the `last_updated` field to determine the most recent record.

```sql
CALL bigfunctions.<your-region>.upsert(
    'dataset_id.product_updates',  -- Source table with updates
    'dataset_id.product_catalog', -- Destination table
    'delta',                      -- Insertion mode
    ['product_id'],              -- Primary key
    'last_updated'               -- Recency field
);
```

This will:

* **Insert:**  Any new products (based on `product_id`) found in `product_updates` that are not present in `product_catalog`.
* **Update:** For products with matching `product_id` in both tables, the values in `product_catalog` will be updated with the values from `product_updates` if the `last_updated` timestamp in `product_updates` is more recent.

**2. Full Merge (Insert, Update, and Delete):**

You want to perform a complete synchronization of your product catalog. This means inserting new products, updating existing ones, and *deleting* products that are no longer present in the source data. You use the `full` insertion mode.

```sql
CALL bigfunctions.<your-region>.upsert(
    -- Query that selects active products from a larger dataset
    'SELECT * FROM dataset_id.all_products WHERE active = TRUE',
    'dataset_id.product_catalog', -- Destination table
    'full',                      -- Insertion mode
    ['product_id'],              -- Primary key
    'last_updated'               -- Recency field
);
```

This will:

* **Insert:** New products.
* **Update:** Existing products with more recent data.
* **Delete:** Products present in `product_catalog` but not returned by the source query (meaning they are no longer active).


**3. Insert Only:**

If you only want to insert new products without updating existing ones:

```sql
CALL bigfunctions.<your-region>.upsert(
    'dataset_id.new_products',    -- Source table with new products
    'dataset_id.product_catalog', -- Destination table
    'insert_only',                -- Insertion mode
    ['product_id'],              -- Primary key
    NULL                         -- No recency field needed for insert only
);
```


These examples demonstrate how the `upsert` function simplifies the process of merging data into a BigQuery table, handling various update scenarios with a single function call.  Remember to replace `<your-region>` with the appropriate BigQuery region (e.g., `us`, `eu`, `us-central1`).
