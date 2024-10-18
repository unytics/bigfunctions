A company has a database of customer reviews in various languages. They want to analyze the sentiment of these reviews but their sentiment analysis tool only works on English text.  They can use the `translate` function within BigQuery to translate all reviews into English before processing them with the sentiment analysis tool.

```sql
SELECT review_id, sentiment(bigfunctions.<region>.translate(review_text, 'en')) AS sentiment_score
FROM `project.dataset.reviews`;
```

Replacing `<region>` with the appropriate BigQuery region for their dataset (e.g., `us`, `eu`, `europe-west1`).  This query translates each `review_text` into English and then calculates the sentiment score using the hypothetical `sentiment` function. This allows the company to perform sentiment analysis on all reviews regardless of the original language.
