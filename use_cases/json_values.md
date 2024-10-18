You have a table in BigQuery that stores JSON strings representing user activity.  Each JSON string contains key-value pairs where the keys represent activity types and the values represent timestamps or user IDs.  You want to extract all the values from these JSON strings to analyze the different types of activities performed without needing to know the specific keys.

**Example Table:**

| UserID | ActivityJSON |
|---|---|
| 1 | `{"login": "2023-10-26 10:00:00", "purchase": "item123"}` |
| 2 | `{"logout": "2023-10-26 10:15:00", "view_product": "item456"}` |
| 3 | `{"login": "2023-10-26 10:30:00", "add_to_cart": "item789"}` |


**Query using `json_values`:**

```sql
SELECT
    UserID,
    bigfunctions.us.json_values(ActivityJSON) AS ActivityValues
FROM
    `your_project.your_dataset.your_table`;
```

**Result:**

| UserID | ActivityValues |
|---|---|
| 1 | `['2023-10-26 10:00:00', 'item123']` |
| 2 | `['2023-10-26 10:15:00', 'item456']` |
| 3 | `['2023-10-26 10:30:00', 'item789']` |

Now you have an array of values for each user, which you can further process. For instance, you could unnest the array to analyze the frequency of different activity values or join it with another table based on these values.  The key benefit here is that you've extracted the relevant data without needing to explicitly parse the JSON based on individual keys.  This is particularly useful when the keys in the JSON strings can vary across different rows but the values themselves hold the information you're interested in.
