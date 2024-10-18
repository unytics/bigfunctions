A market research team wants to analyze user sentiment towards a specific mobile application (e.g., "Nickel App" with app ID `com.fpe.comptenickel`) across different regions. They want to understand how French users who have downloaded the app and written their review in English perceive the app.  To achieve this, they would use the `get_playstore_reviews` BigQuery function with the following parameters:

* `app_id`: `com.fpe.comptenickel`
* `country`: `fr` (France)
* `language`: `en` (English)


They would then execute a query like this (adjusting the dataset `bigfunctions.us` to match their BigQuery region):

```sql
SELECT * FROM UNNEST(JSON_EXTRACT_ARRAY(bigfunctions.us.get_playstore_reviews('com.fpe.comptenickel', 'fr', 'en'), '$.reviews')) AS review;
```

This query retrieves the reviews as a JSON array, then unnests the array so each review is a separate row.  The team can then perform further analysis on the `content`, `score`, and other fields within each review to gauge user sentiment, identify common themes in positive or negative feedback, and understand the overall user experience for this specific user segment. This information can then be used to inform product development, marketing strategies, and customer support efforts.
