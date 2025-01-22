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


h1 {
  font-weight: 700!important;
  font-size: 2rem!important;
  line-height: 1.1 !important;
  background-image: linear-gradient(60deg, #495ccdff, #2a3576ff);
  background-clip: text;
  color: #0000!important;
  margin: 0 0 0.6em!important;
}

.h1-bigger {
  color: rgb(38, 38, 38)!important;
  font-size: 3rem!important;
}

@media (min-width: 640px) {
  h1 {
    font-size: 3rem!important;
  }

  .h1-bigger {
    font-size: 4.5rem!important;
  }

  .hero p {
    font-size: 1rem!important;
  }
}


h2 {
    font-weight: 600!important;
    color: rgb(38, 38, 38)!important;
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

</style>

<div class="md-container hero">
  <div>
    <h1><span class="h1-bigger">SQL</span><br>is all you need</h1>
    <p>Supercharge <b>BigQuery</b> with <b>BigFunctions</b><br>to load, transform and activate data.</p>
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

<!-- <div class="md-container">
  <div class="hero__image">
    <img
      src="{{config.site_url}}assets/images/bigfunctions_intro.gif"
      alt=""
      draggable="false"
      style="border: black solid 1rem; width: 100%; margin-top: 5rem;"
    >
  </div>
</div> -->

<!-- <hr style="margin: 16em 1em 1.5em 1em;  border-bottom: 0.05rem solid var(--md-default-fg-color--lightest); display: flow-root;"> -->

<br>
<br>
<br>

<div class="grid-container" markdown>

<div class="grid cards" markdown>


-   ## From Modern Data Stack

    <figure markdown="span">
        ![Image title](assets/modern_data_stack2.png){ width="600" }
        <figcaption>The Modern Data Stack is Complex!</figcaption>
    </figure>

    :x: **Tool Sprawl**: A multitude of tools for various tasks complicates the data workflow.

    :x: **Custom Scripting**: Reliance on custom Python scripts introduces complexity and increases maintenance overhead.

    :x: **Lack of Self-Service**: Data analysts often depend on data engineers for complex tasks, hindering agility and efficiency.



-   ## :octicons-arrow-right-24: to SQL Data Stack

    <figure markdown="span">
        ![Image title](assets/sql_data_stack2.png){ width="600" }
        <figcaption>Supercharged Data-Warehouse is All You Need!</figcaption>
    </figure>

    :white_check_mark:  **Simplicity**: Achieve everything with SQL, thus minimizing the need for multiple tools.

    :white_check_mark:  **Centralized Governance**: Control all data processes from a central data warehouse with declarative assets.

    :white_check_mark:  **Self-Service**:  Empower data analysts to perform intricate tasks using SQL functions directly.


</div>

</div>




## BigFunctions brings the SQL Data Stack


!!! quote ""

    BigFunctions makes the **SQL data stack** a reality


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



## Supercharge Your SQL with BigFunctions

BigFunctions offers a variety of functions to manage the data lifecycle, including data ingestion, transformation, and activation.

### Functionality Examples:

*   **Loading Data**: Load data from any file on the internet using SQL.
*   **Transforming Data**: Perform complex data transformations using functions such as the time series forecasting function `prophet`.
*   **Activating Data**: Send emails to target audiences directly from SQL queries and send data to your CRM using activation functions.

Explore all available BigFunctions.



## Get Started with BigFunctions


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



---

> The modern data stack is characterized by a collection of tools for data ingestion, transformation, and activation + additional python scripts to address custom needs.
>
> :octicons-arrow-right-24: The Data Workflow is **fragmented** and **hard to manage**.
>
> The future of the data stack is a* **declarative SQL data stack** *where the data warehouse is equipped to handle all data needs using SQL and advanced functions.
>
> :octicons-arrow-right-24: The Data Workflow is* **Simple**.
>
