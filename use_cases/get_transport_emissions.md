A logistics company uses BigQuery to store data about its deliveries.  Each record in the `deliveries` table includes the `distance_km` for each delivery.  The company wants to calculate the estimated CO2 emissions for each delivery, broken down by different transportation modes (e.g., truck, train, plane) to understand its environmental impact and explore potential optimizations.

They can use the `get_transport_emissions` function within a query like this:

```sql
SELECT
    delivery_id,
    distance_km,
    bigfunctions.eu.get_transport_emissions(distance_km) AS co2_emissions
  FROM
    `project.dataset.deliveries`;

```

This query adds a new column, `co2_emissions`, to the results.  This column contains an array of structs, where each struct represents a transportation mode and its associated CO2 emission for the given distance. The company can then further process this data:

* **Aggregate emissions by transport mode:**  Unnest the `co2_emissions` array and aggregate the total emissions for each transport mode across all deliveries.  This allows them to see which modes contribute most to their carbon footprint.

```sql
SELECT
    transport.name,
    SUM(transport.value) AS total_emissions
  FROM
    `project.dataset.deliveries`,
    UNNEST(bigfunctions.eu.get_transport_emissions(distance_km)) AS transport
  GROUP BY 1
  ORDER BY
    total_emissions DESC

```


* **Compare emissions for different delivery routes:** If they have multiple potential routes for a delivery, they can use this function to estimate the emissions for each route and choose the most environmentally friendly option.

* **Scenario planning:** The company could use this function to model the impact of switching to different transport modes for a portion of their deliveries.  For example, what would be the CO2 reduction if 20% of truck deliveries were switched to rail?

* **Reporting and dashboards:** Integrate the emission data into reports and dashboards to monitor progress towards sustainability goals.


By using the `get_transport_emissions` function directly within their BigQuery workflows, the logistics company can efficiently analyze their emissions data without needing to manage external APIs or data transfers.  This enables them to make data-driven decisions to optimize their operations for lower environmental impact.
