# Generate Static Dashboards using Mozaic

**Select an Example**


<style>
.loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid var(--md-primary-fg-color); /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

select#examples {
    padding: 1em;
    border-color: var(--md-primary-fg-color);
}
</style>

<select id="examples">
    <option value="aeromagnetic-survey">Aeromagnetic Survey</option>
    <option value="airline-travelers">Airline Travelers</option>
    <option value="athletes">Athletes</option>
    <option value="athlete-birth-waffle">Athlete Birth Waffle</option>
    <option value="athlete-height">Athlete Height Intervals</option>
    <option value="axes">Axes &amp; Gridlines</option>
    <option value="bias">Bias Parameter</option>
    <option value="contours">Contours</option>
    <option value="crossfilter">Crossfilter</option>
    <option value="density-groups">Density Groups</option>
    <option value="density1d">Density 1D</option>
    <option value="density2d">Density 2D</option>
    <option value="driving-shifts">Driving Shifts into Reverse</option>
    <option value="earthquakes-feed">Earthquakes Feed</option>
    <option value="earthquakes-globe">Earthquakes Globe</option>
    <option value="facet-interval">Facet Interval</option>
    <option value="flights-200k">Flights 200k</option>
    <option value="flights-10m">Flights 10M</option>
    <option value="flights-density">Flights Density</option>
    <option value="flights-hexbin">Flights Hexbin</option>
    <option value="gaia">Gaia Star Catalog</option>
    <option value="line-density">Line Density</option>
    <option value="line">Line</option>
    <option value="line-multi-series">Line Multi-Series</option>
    <option value="linear-regression">Linear Regression</option>
    <option value="linear-regression-10m">Linear Regression 10M</option>
    <option value="legends">Legends</option>
    <option value="mark-types">Mark Types</option>
    <option value="moving-average">Moving Average</option>
    <option value="normalize">Normalize Stocks</option>
    <option value="nyc-taxi-rides">NYC Taxi Rides</option>
    <option value="observable-latency">Observable Latency</option>
    <option value="overview-detail">Overview + Detail</option>
    <option value="pan-zoom">Pan + Zoom</option>
    <option value="population-arrows">Population Arrows</option>
    <option value="presidential-opinion">Presidential Opinion</option>
    <option value="protein-design">Protein Design</option>
    <option value="region-tests">Region Tests</option>
    <option value="seattle-temp">Seattle Temperatures</option>
    <option value="sorted-bars" selected>Sorted Bars</option>
    <option value="splom">Scatter Plot Matrix</option>
    <option value="symbols">Symbols</option>
    <option value="table">Table</option>
    <option value="unemployment">Unemployment</option>
    <option value="us-county-map">U.S. County Map</option>
    <option value="us-state-map">U.S. State Map</option>
    <option value="voronoi">Voronoi</option>
    <option value="walmart-openings">Walmart Openings</option>
    <option value="weather">Seattle Weather</option>
    <option value="wind-map">Wind Map</option>
    <option value="wnba-shots">WNBA Shot Chart</option>
</select>

!!! note ""

    💡 Mozaic Dashboards are generated on the fly from a yaml configuration file using Mosaic Javascript Library. They are interactive and based on parquet files. Know more [below](#more-on-mozaic) on Mozaic.


<br>

=== "Generated Dashboard"

    <div id="view"></div>

=== "YAML Configuration"

    <div id="yaml" style="white-space: pre-wrap;"></div>


---

<br>

## More on Mozaic

!!! note ""

    [Mosaic javascript library](https://idl.uw.edu/mosaic/) can generate a dashboard:

    - from a simple yaml configuration which defines
        - the parquet files to use
        - the interactive elements (inputs and dropdowns)
        - the plots
    - with interactivity thanks to duckdb
    - with ultra-fast cross-filtering

    Above, you can select some yaml files examples provided on Mosaic Website.
    At selection, it will:

    - initialize a duckdb wasm database in browser
    - create tables in the database by loading the parquet files
    - generate the html of the inputs and plots.

    The generated dashboard is interactive by changing the inputs or selecting areas in the plot.
    Under the hood, duckdb queries are made on the fly before rendering the changes.




<script type="module">
  import { load } from '../assets/mosaic.js';

  const view = document.querySelector('#view');
  const yaml = document.querySelector('#yaml');
  const exampleMenu = document.querySelector('#examples');

  const baseURL = 'https://idl.uw.edu/mosaic/';

  async function loadDashboard() {
    const specURL = `${baseURL}specs/yaml/${exampleMenu.value}.yaml`;
    await load(specURL, baseURL, view, yaml);
  }

  exampleMenu.addEventListener('change', loadDashboard);

  loadDashboard();

</script>
