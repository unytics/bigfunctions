**Use Case: Finding the appropriate pricing tier**

Imagine you have a table of pricing tiers for a product, with each tier defined by a usage threshold and a corresponding price. You could use `find_greater_value` to efficiently determine the correct pricing tier for a given customer's usage.


**Example Scenario:**

A software company offers different pricing tiers based on the number of API calls made per month:

| Tier | API Calls | Price |
|---|---|---|
| Free | 0-1,000 | $0 |
| Basic | 1,001-5,000 | $25 |
| Premium | 5,001-10,000 | $50 |
| Enterprise | > 10,000 | $100 |


**BigQuery Implementation:**

```sql
WITH PricingTiers AS (
    SELECT [1000, 5000, 10000] AS api_call_thresholds,
           [0, 25, 50, 100] AS prices
),
CustomerUsage AS (
    SELECT 'customer_A' AS customer_id, 7500 AS api_calls
)
SELECT
    CustomerUsage.customer_id,
    CustomerUsage.api_calls,
    PricingTiers.prices[SAFE_OFFSET(bigfunctions.YOUR_REGION.find_greater_value(PricingTiers.api_call_thresholds, CustomerUsage.api_calls))] AS price
FROM CustomerUsage
CROSS JOIN PricingTiers;

```

**Explanation:**

1. **`PricingTiers` CTE:** This CTE stores the API call thresholds and corresponding prices as arrays.
2. **`CustomerUsage` CTE:** This CTE represents the customer's API usage.
3. **Main Query:**
   - It joins `CustomerUsage` and `PricingTiers`.
   - `find_greater_value` searches the `api_call_thresholds` array for the first value greater than or equal to the customer's `api_calls`. This returns the index (offset) of the appropriate tier.
   - `SAFE_OFFSET` handles cases where the usage exceeds all defined tiers (e.g., > 10,000), returning the last price in the array.


**Result:**

| customer_id | api_calls | price |
|---|---|---|
| customer_A | 7500 | 50 |


This example demonstrates how `find_greater_value` can be used for efficient lookups in tiered data, eliminating the need for complex `CASE` statements or joins. This approach is particularly useful when dealing with a large number of tiers or when the tiers are subject to change, as updating the arrays is much simpler than modifying numerous `CASE` conditions. You could extend this to other use cases such as tax brackets, shipping costs based on weight, or commission rates based on sales volume.  Remember to replace `YOUR_REGION` with your BigQuery region (e.g. `us`, `eu`, `us-central1`).
