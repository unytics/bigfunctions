A data analyst wants to analyze the activity on the `dbt-labs/dbt-core` GitHub repository.  They are particularly interested in tracking the number of stargazers over time, identifying key contributors through commits, and understanding the release history.  They can use the `get_github_data` BigQuery function to import this data directly into BigQuery for analysis.

Here's how they would use the function:

1. **Prepare the destination dataset:**

```sql
-- Create the dataset
CREATE SCHEMA `my_project.github_data`;

-- Grant access to the BigFunctions service account
GRANT `roles/bigquery.dataEditor`
ON SCHEMA `my_project.github_data`
TO 'serviceAccount:bigfunction@bigfunctions.iam.gserviceaccount.com';
```

2. **Import the data using the function:**

```sql
SELECT bigfunctions.us.get_github_data('dbt-labs/dbt-core', 'my_project.github_data', 'stargazers, commits, releases');
```

This call will import data for the specified streams (`stargazers`, `commits`, and `releases`) into tables within the `my_project.github_data` dataset.  For instance, the stargazer data will likely be in a table named `my_project.github_data.stargazers`.

3. **Analyze the data in BigQuery:**

Now the analyst can use standard SQL queries to analyze the imported data.  For example:

```sql
-- Track stargazer growth over time
SELECT DATE(starred_at) AS star_date, COUNT(*) AS num_stars
FROM `my_project.github_data.stargazers`
GROUP BY star_date
ORDER BY star_date;

-- Identify top contributors
SELECT author.login, COUNT(*) AS num_commits
FROM `my_project.github_data.commits`
GROUP BY author.login
ORDER BY num_commits DESC;

-- Explore release history
SELECT name, tag_name, published_at
FROM `my_project.github_data.releases`
ORDER BY published_at DESC;
```

This use case demonstrates how the `get_github_data` function simplifies the process of importing and analyzing GitHub repository data within BigQuery, enabling data-driven insights into project activity and community engagement.
