A marketing team wants to analyze the performance of their recent social media campaigns. They have the campaign data stored in a BigQuery table. To share this data with non-technical stakeholders who primarily use Google Sheets, they can utilize the `upload_to_gsheet` function.


Here's a breakdown of the use case:

1. **Data Preparation in BigQuery:** The marketing team creates a BigQuery query to aggregate the relevant campaign data, such as campaign name, impressions, clicks, conversions, and cost.  Let's assume the query results in a table named `campaign_performance`.

2. **Converting to JSON:**  They use BigQuery's `TO_JSON_STRING` function to convert the results of the `campaign_performance` table into a JSON array of objects, where each object represents a row of campaign data.

   ```sql
   SELECT TO_JSON_STRING(t)
   FROM `project.dataset.campaign_performance` AS t;
   ```

3. **Uploading to Google Sheets:** They use the `upload_to_gsheet` function within BigQuery to upload this JSON data directly to a designated Google Sheet.

   ```sql
   SELECT bigfunctions.us.upload_to_gsheet(
       (
           SELECT TO_JSON_STRING(t)
           FROM `project.dataset.campaign_performance` AS t
       ), 
       'https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID', 
       'Campaign Performance', 
       'write_truncate'
   );
   ```
   This code snippet does the following:
    * Calls the `upload_to_gsheet` function from the appropriate regional dataset (e.g., `bigfunctions.us`).
    * Passes the JSON string generated in the subquery as the `data` argument.
    * Provides the URL of the target Google Sheet, replacing `YOUR_SPREADSHEET_ID` with the actual ID.
    * Specifies the worksheet name as 'Campaign Performance'.
    * Uses the `write_truncate` mode to overwrite the sheet if it already exists, ensuring they always have the latest data.  Alternatively, they could use `write_append` to add new data to the existing sheet.

4. **Sharing and Analysis in Google Sheets:** The Google Sheet is then shared with the non-technical stakeholders, who can easily access, visualize, and analyze the campaign performance data within their familiar spreadsheet environment.  They can create charts, pivot tables, and use other Google Sheets features to gain insights.


This process automates the data transfer from BigQuery to Google Sheets, ensuring that stakeholders have up-to-date campaign performance data readily available for analysis and decision-making. It bridges the gap between technical data storage and non-technical data consumption, enabling broader access to critical business information.
