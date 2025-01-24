---
title: "BigFunctions Supercharge BigQuery"
hide:
  - navigation
  - toc
---

<style>


/* Get started button */
.md-typeset .md-button--primary:hover {
  color: var(--md-primary-fg-color);
  background-color: var(--md-primary-bg-color);
  border-color: var(--md-primary-fg-color);
}
.md-typeset .md-button--primary {
  color: var(--md-primary-bg-color);
  background-color: var(--md-primary-fg-color);
  border-color: var(--md-primary-bg-color);
}

.hero {
  max-width: 700px;
  display: flex;
  padding: .4rem;
  margin: 0 auto;
  text-align: center;
}

.hero p {
  color: rgb(92, 92, 92);
  font-weight: 400;
  font-size: 0.8rem!important;
  line-height: 1.6!important;
}
.hero__image {
  max-width: 1000px;
  /*min-width: 600px;*/
  width: 100%;
  height: auto;
  margin: 0 auto;
  display: flex;
  align-items: stretch;
}

.hero__image img {
  width: 100%;
  height: 100%;
  min-width: 0;
}

.md-button--center {
    text-align: center;
}

.md-content h1, .md-content h2 {
  background-image: linear-gradient(60deg, #495ccdff, #232c60ff);
  background-clip: text;
  color: #0000!important;
}

.md-content h1 {
  font-weight: 700!important;
  font-size: 2rem!important;
  line-height: 1.1 !important;
  margin: 0 0 0.6em!important;
}

.md-content .h1-bigger {
  color: rgb(38, 38, 38)!important;
  font-size: 3rem!important;
}

@media (min-width: 640px) {
  .md-content h1 {
    font-size: 3rem!important;
  }

  .md-content .h1-bigger {
    font-size: 4.5rem!important;
  }

  .hero p {
    font-size: 1rem!important;
  }
  .hero p.small {
    font-size: 0.8rem!important;
  }


  .grid-2 {
    grid-template-columns: 47.5% 47.5%!important;
    grid-column-gap: 5%!important;
    grid-row-gap: 40px!important;
  }
}


h2 {
    font-weight: 600!important;
}

.grid-container {
    background-color: var(--md-primary-fg-color)!important;
    padding: 20px;
}

.grid-container h2 {
    color: var(--md-primary-fg-color) !important;
}

.grid-container li {
    margin: 10px 0!important;
}

.cards li {
    background-color: white;
    color: rgb(92, 92, 92);
}

.centered-big-message {
    color: rgb(92, 92, 92);
    font-size: 1.2em;
    margin-top: -0.5em;
}

.quote {
    text-align: center;
    font-style: italic;
    /* font-weight: 600!important; */
    font-size: 1.2em!important;
    color: rgb(250, 250, 250)!important;
    /* color: rgb(92, 92, 92)!important; */
    background-color: var(--md-primary-fg-color)!important;
}

img.gray-scale {
  filter: grayscale(100%); /* Standard */
  -webkit-filter: grayscale(100%); /* Webkit */
  vertical-align: middle;
}


.primary-background {
  background-color: var(--md-primary-fg-color)!important;
  padding: 20px;
}

.grid-2 {
  display: grid;
  grid-template-columns: 100%;
  grid-column-gap: 0;
  grid-row-gap: 20px;
  max-width: 900px;
  margin: auto;
}
.grid-2 > div {
  background-color: white;
  padding: 2rem;
  max-width: 400px;
  margin: auto;
  height: 100%;
}

.grid-2 h2 {
  margin: 0 0 0.64em!important;
}



.md-typeset .text-and-image {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

.md-typeset .text-and-image>ul {
    display: contents;
}

.md-typeset .text-and-image>ul>li {
    display: block;
    margin: 0;
    padding: .8rem;
}


@media (min-width: 1024px) {

  .md-typeset .text-and-image {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: 2rem;
  }

  .md-typeset .text-and-image.image-on-left li:nth-of-type(2) {
     order: -9999!important;
  }
}


</style>


<div class="md-container hero">
  <div>
    <h1><span class="h1-bigger">SQL</span><br>is all you need</h1>
    <p>Supercharge <b>BigQuery</b> with <b>BigFunctions</b><br><i>to load, transform and activate your data.</i></p>
    <a href="https://calendar.app.google/zu54nNMHLVw7jYWy8" class="md-button">
      Book a Demo
      <svg width="11" height="10" viewBox="0 0 11 10" fill="none" style="margin-left:2px"><path d="M1 5.16772H9.5M9.5 5.16772L6.5 1.66772M9.5 5.16772L6.5 8.66772" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    </a>
    <a href="bigfunctions/" class="md-button md-button--primary">
      Explore
      <svg width="11" height="10" viewBox="0 0 11 10" fill="none" style="margin-left:2px"><path d="M1 5.16772H9.5M9.5 5.16772L6.5 1.66772M9.5 5.16772L6.5 8.66772" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    </a>
  </div>
</div>

<br>
<div class="md-container hero">
  <p class="small" style="margin-bottom: -20px"><i>Taking the most of</i></p>
  <figure><img class="gray-scale" src="assets/gcp.svg" width=200></figure>
</div>

<br>
<br>
---
<br>

<div class="md-container hero">
  <div>
    <h1>The power of functions<br>with the ease of SQL</h1>
    <p>
      Have a data need? <strong>There's a bigfunction for that!</strong><br>
      <i>BigFunctions provides <a href="bigfunctions/">150+ ready to use functions</a></i>
    </p>
  </div>
</div>



<div class="text-and-image image-on-left" markdown>

-   ## Load Data from any vendor

    Load data from Salesforce, Hubspot and hundreds of vendors with one SQL command.

    [Get Started :octicons-arrow-right-24:](bigfunctions/load_api_data/){ .md-button }

-   ![Image title](https://dummyimage.com/600x400/eee/aaa)

</div>


<div class="text-and-image image-on-right" markdown>

-   ## Perform Anomaly Detection

    Load data from Salesforce, Hubspot and hundreds of vendors with one SQL command.

    [Get Started :octicons-arrow-right-24:](bigfunctions/load_api_data/){ .md-button }

-   ![Image title](https://dummyimage.com/600x400/eee/aaa)

</div>







<div class="md-container hero">
  <div>
    <p>BigFunctions come with 150+ ready to use functions</p>
    <a href="bigfunctions/" class="md-button md-button--primary">
      Explore Functions
      <svg width="11" height="10" viewBox="0 0 11 10" fill="none" style="margin-left:2px"><path d="M1 5.16772H9.5M9.5 5.16772L6.5 1.66772M9.5 5.16772L6.5 8.66772" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    </a>
  </div>
</div>





---


<div class="md-container primary-background">

<h2 style="color: white!important; text-align: center; margin: 1.4em 0 0 0 !important;">The rise of the SQL-Data-Stack</h2>
<p class="quote">
  The data-warehouse,<br>
  supercharged with advanced functions,<br>
  can perform any advanced data job<br>
  (all callable with SQL).<br>
</p>

<div class="grid-2">
  <div>
    <h2>Modern-Data-Stack</h2>
    <img src="assets/modern_data_stack2.png" style="width: 90%">
    <p><img alt="❌" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/274c.svg" title=":x:"> <strong>Tool Sprawl</strong>: A multitude of tools for various tasks complicates the data workflow.</p>
    <p><img alt="❌" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/274c.svg" title=":x:"> <strong>Custom Scripting</strong>: Reliance on custom Python scripts introduces complexity and increases maintenance overhead.</p>
    <p><img alt="❌" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/274c.svg" title=":x:"> <strong>Lack of Self-Service</strong>: Data analysts often depend on data engineers for complex tasks, hindering agility and efficiency.</p>
  </div>
  <div>
    <h2>SQL-Data-Stack</h2>
    <img src="assets/sql_data_stack2.png" style="width: 90%">
    <p><img alt="✅" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/2705.svg" title=":white_check_mark:">  <strong>Simplicity</strong>: Achieve everything with SQL, thus minimizing the need for multiple tools.</p>
    <p><img alt="✅" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/2705.svg" title=":white_check_mark:">  <strong>Centralized Governance</strong>: Control all data processes from a central data warehouse with declarative assets.</p>
    <p><img alt="✅" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/2705.svg" title=":white_check_mark:">  <strong>Self-Service</strong>:  Empower data analysts to perform intricate tasks using SQL functions directly.</p>
  </div>
</div>
</div>

---





<br>
<br>
<br>




## BigFunctions: the key enabler of the SQL Data Stack

!!! note ""


    **BigFunctions** is a framework and a collection of open-source functions that make the SQL data stack a reality. It allows you to build a governed catalog of powerful BigQuery functions within your company.

    *   **Governed Catalog**: A framework to build a governed catalog of powerful BigQuery functions.
    *   **100+ Ready-to-Use Functions**: Provides more than 100 open-source functions for direct use in BigQuery.
    *   **Comprehensive Functionality**: Includes functions for loading, transforming, and activating data.
    *   **Community-Driven**: Leverages community-developed functions, and allows contributions.
    *   **Familiar Workflow**:  Uses a YAML standard and CLI similar to dbt, making it intuitive for dbt users.

    ### Benefits for Different Users:

    *   **Data Analysts**: Gain new capabilities for loading data from diverse sources or activating data via reverse ETL and leverage a catalog of self-service functions.
    *   **Analytics Engineers**: The framework's design is familiar to those who use dbt.
    *   **Data Engineers**: Implement software engineering best practices and leverage community-developed functions, preventing the need to reinvent the wheel.
    *   **Central Data Teams**: Provide a governed catalog of curated functions to large organizations with maintainable effort.

    ### Functionality Examples:

    *   **Loading Data**: Load data from any file on the internet using SQL.
    *   **Transforming Data**: Perform complex data transformations using functions such as the time series forecasting function `prophet`.
    *   **Activating Data**: Send emails to target audiences directly from SQL queries and send data to your CRM using activation functions.
    Explore all available BigFunctions.


## Get Started with BigFunctions

!!! note ""

    <div class="grid cards" markdown>

    -   :material-clock-fast:{ .lg .middle } __Call Public BigFunctions__

        ---

        You can call public functions directly from your BigQuery project without installation. For example:
        ```sql
        SELECT bigfunctions.eu.faker("name", "it_IT")
        ```

        [Explore Public BigFunctions :octicons-arrow-right-24:](bigfunctions){ .md-button .md-input--stretch .md-button--center }


    -   :material-rocket-launch:{ .lg .middle } __Deploy BigFunctions__

        ---

        You can also deploy functions in your GCP project.

        - Install the bigfun CLI: pip install bigfunctions.
        - Deploy a function: bigfun deploy my_bigfunction.
        - Functions are defined using YAML files.

        [Discover the Framework :octicons-arrow-right-24:](framework){ .md-button .md-input--stretch .md-button--center }


    -   :fontawesome-solid-people-group:{ .lg .middle } __Join the Community__

        ---

        Benefit from BigFunctions community to get support or help others.

        [Join Slack :octicons-arrow-right-24:](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q){ .md-button .md-input--stretch .md-button--center }


    -   :fontawesome-solid-person-walking:{ .lg .middle } __Contribute to BigFunctions__

        ---

        BigFunctions is fully open-source, and any contribution is welcome.

        [See Contribution Instructions :octicons-arrow-right-24:](CONTRIBUTING){ .md-button .md-input--stretch .md-button--center }

    </div>
