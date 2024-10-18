A company has a table of sales data with a date column. They want to create a report that displays the month name in different languages based on the user's locale.  They can use the `translated_month_name` function to achieve this.

**Example Scenario:**

The company operates in France and Spain.  They have a BigQuery table called `sales` with columns `date` and `sales_amount`.

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.sales` AS
SELECT DATE('2023-01-15') AS date, 1200 AS sales_amount UNION ALL
SELECT DATE('2023-02-20') AS date, 1500 AS sales_amount UNION ALL
SELECT DATE('2023-03-10') AS date, 1800 AS sales_amount UNION ALL
SELECT DATE('2023-04-05') AS date, 1100 AS sales_amount;
```

**Query for French Users:**

```sql
SELECT
    bigfunctions.eu.translated_month_name(date, 'fr') AS month_name_fr,
    sales_amount
FROM
    `your_project.your_dataset.sales`;
```

**Result:**

| month_name_fr | sales_amount |
|---|---|
| janvier | 1200 |
| février | 1500 |
| mars | 1800 |
| avril | 1100 |


**Query for Spanish Users:**

```sql
SELECT
    bigfunctions.eu.translated_month_name(date, 'es') AS month_name_es,
    sales_amount
FROM
    `your_project.your_dataset.sales`;
```

**Result:**

| month_name_es | sales_amount |
|---|---|
| enero | 1200 |
| febrero | 1500 |
| marzo | 1800 |
| abril | 1100 |

This allows the company to generate reports tailored to different language preferences without needing complex case statements or separate tables for each language.  The `translated_month_name` function simplifies the process of localizing date information. Remember to replace `your_project.your_dataset` and the region prefix (e.g. `eu`, `us`) as needed.
