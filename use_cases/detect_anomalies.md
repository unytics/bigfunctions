A website analytics company collects daily website visit data. They store this information in a BigQuery table called `website_visits` with columns `visit_date` and `number_of_visits`.  They want to use the `detect_anomalies` function to identify days with unusually high or low traffic.  This can help them:

* **Understand traffic spikes:**  Identify marketing campaign successes, viral content, or external events driving traffic.
* **Detect traffic drops:**  Investigate website issues, server outages, or algorithm changes impacting visibility.
* **Alert on unusual patterns:**  Detect bots, DDoS attacks, or other malicious activity.

**Example BigQuery Code (using the `us` region):**

```sql
SELECT bigfunctions.us.detect_anomalies('my_project', 'website_visits', 'visit_date', 'number_of_visits', 2.5);
```

**Explanation:**

* `my_project`: Replace with the actual project ID.
* `website_visits`: The table containing the website visit data.
* `visit_date`: The column representing the date of the visit.
* `number_of_visits`: The column representing the number of visits on that date.
* `2.5`: The threshold for the Z-score.  A value of 2.5 means any data point with a Z-score greater than 2.5 or less than -2.5 will be flagged as an anomaly.  This threshold can be adjusted based on the expected variability of the data.


**Expected Output:**

The function will return a JSON string containing an array of anomaly objects. Each object will contain the `time` (visit_date), `value` (number_of_visits), and the calculated `z_score` for the anomalous data points.

**Example Output:**

```json
'[{"time": "2024-01-01", "value": 50000, "z_score": 3.2}, {"time": "2024-01-15", "value": 10000, "z_score": -2.8}]'
```

This output indicates two anomalies: a large spike in traffic on January 1st and a significant drop in traffic on January 15th. The website analytics team can then investigate these anomalies further to understand the underlying causes.
