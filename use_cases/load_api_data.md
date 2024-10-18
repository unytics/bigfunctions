Let's say you want to analyze customer feedback from your Zendesk Support instance in BigQuery. You can use the `load_api_data` function to achieve this without manual data extraction and uploads.

**1. Identify the Source and Explore Configuration:**

* **Source:**  `airbyte-source-zendesk-support==2.6.10` (or a later compatible version)

**2. Generate Encrypted Secret for your Zendesk Access Token:**

* Follow the instructions in the documentation to encrypt your Zendesk access token. This ensures your credentials aren't exposed in logs. Let's assume the encrypted secret is `ENCRYPTED_SECRET(your_encrypted_token)`.

**3. Determine Available Streams:**

* Call `load_api_data` with `streams` set to `null` to see what data Zendesk makes available:

```sql
call bigfunctions.us.load_api_data('airbyte-source-zendesk-support==2.6.10', '''
  credentials:
    access_token: ENCRYPTED_SECRET(your_encrypted_token)
''', null, null);
select * from bigfunction_result;
```
* This will return a list of available streams, such as `tickets`, `users`, `organizations`, etc.

**4. Select Desired Streams and Destination:**

* Decide which streams you need (e.g., `tickets`, `users`).
* Choose your BigQuery destination dataset. For example: `your_project.your_zendesk_data`

**5. Load the Data:**

* Call `load_api_data` with the correct parameters:

```sql
call bigfunctions.us.load_api_data('airbyte-source-zendesk-support==2.6.10', '''
  credentials:
    access_token: ENCRYPTED_SECRET(your_encrypted_token)
''', 'tickets,users', 'your_project.your_zendesk_data');
select * from bigfunction_result;
```

This will:

* Create temporary tables within the `bigfunctions` project.
* Extract data from the `tickets` and `users` streams in Zendesk.
* Load the extracted data into the temporary tables.
* Move the data from the temporary tables to your specified destination dataset (`your_project.your_zendesk_data`).
* Clean up the temporary tables and resources.

**Result:**  You now have Zendesk ticket and user data in your BigQuery dataset, ready for analysis.  Subsequent calls will incrementally load new or updated data based on the state saved in the `_airbyte_states` table.


**Key Improvements over other Methods:**

* **Simplified Data Integration:** No need to build custom ETL pipelines or manage infrastructure.
* **Wide Connector Support:** Access data from 250+ sources through Airbyte.
* **Incremental Loads:**  Avoids redundant data processing by loading only new or changed data.
* **Secure Credential Handling:** Encryption protects sensitive information.
* **Serverless:**  Leverages BigQuery's serverless architecture for scalability and cost-efficiency.


This example showcases how `load_api_data` streamlines data ingestion from external APIs into BigQuery, enabling efficient data analysis and reporting.  You can adapt this approach to integrate data from various other sources supported by Airbyte connectors.
