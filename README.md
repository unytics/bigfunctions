![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers, DataWarehouse in the middle</em>
</p>

---

**Documentation**: <a href="https://unytics.github.io/bigfunctions/" target="_blank">[https://unytics.github.io/bigfunctions/](https://unytics.github.io/bigfunctions/)</a>

---

BigFunctions are open BigQuery routines that give you new *SQL powers* in BigQuery 💪.


### Deploy

```sh
# Deploy `render_string` BigFunction in dataset `eu` of project `bigfunctions`
bfun deploy bigfunctions.eu.render_string

# Deploy `render_string` BigFunction in all datasets defined in environment variable `BIGFUNCTIONS_DATASETS`

```

```sh
export BIGFUNCTIONS_DATASETS=bigfunctions.eu,bigfunctions.us,bigfunctions.asia_east1,bigfunctions.asia_east2,bigfunctions.asia_northeast1,bigfunctions.asia_northeast2,bigfunctions.asia_northeast3,bigfunctions.asia_south1,bigfunctions.asia_southeast1,bigfunctions.australia_southeast1,bigfunctions.europe_north1,bigfunctions.europe_west1,bigfunctions.europe_west2,bigfunctions.europe_west3,bigfunctions.europe_west4,bigfunctions.europe_west6,bigfunctions.northamerica_northeast1,bigfunctions.southamerica_east1,bigfunctions.us_central1,bigfunctions.us_east1,bigfunctions.us_east4,bigfunctions.us_west1,bigfunctions.us_west2

```