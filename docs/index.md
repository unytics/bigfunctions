---
title: "BigFunctions Supercharge BigQuery"
hide:
  - navigation
  - toc
---

<style>


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

.md-content h1 a.headerlink, .md-content h2 a.headerlink {
  display: none;
}

.md-content .big-word {
  font-weight: 700!important;
  color: rgb(38, 38, 38)!important;
  font-size: 3rem!important;
  color: var(--md-default-fg-color--light);
  font-size: 2em;
  line-height: 1;
  margin-top: 0;
  margin-bottom: 0;
}

.md-content h2 {
    font-weight: 600!important;
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

.md-typeset .primary-background {
  background-color: var(--md-primary-fg-color)!important;
  padding: 20px;
}

.md-typeset .max-width-800 {
  max-width: 800px;
  margin: auto;
}

.md-typeset .max-width-800.md\:two-columns>ul>li {
  background-color: white;
  padding: 0 2rem 2rem;
  max-width: 400px;
  margin: auto;
  height: 100%;
}

.md-typeset .max-width-800.md\:two-columns>ul>li p {
  margin-block-start: 1em;
  margin-block-end: 1em;
}




.mt-neg {
  margin-top: -20px!important;
}


/*------- HERO -------*/
.hero {
  max-width: 700px;
  margin: 3rem auto;
  text-align: center;
}

.hero h1 {
  margin: 0 0 0.3em!important;
}

.hero p {
  color: rgb(92, 92, 92);
  font-weight: 400;
  font-size: 0.8rem;
  line-height: 1.6;
}


/*------- TEXT AND IMAGE -------*/
.md-typeset .lg\:two-columns, .md-typeset .md\:two-columns {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  grid-row-gap: 20px;
}

.md-typeset .lg\:two-columns>ul, .md-typeset .md\:two-columns>ul {
    display: contents;
}

.md-typeset .lg\:two-columns>ul>li, .md-typeset .md\:two-columns>ul>li {
    display: block;
    margin: 0;
    padding: .8rem;
}


/*------- FROM MEDIUM SCREEN -------*/
@media (min-width: 640px) {
  .md-content h1 {
    font-size: 3rem!important;
  }

  .md-content .big-word {
    font-size: 4.5rem!important;
  }

  .hero p {
    font-size: 1rem!important;
  }

  .hero p.small {
    font-size: 0.8rem!important;
  }

  .md-typeset .md\:two-columns {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: 2rem;
  }
}

/*------- FROM LARGE SCREEN -------*/
@media (min-width: 1024px) {

  .md-typeset .lg\:two-columns {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: 2rem;
  }

  .md-typeset .lg\:two-columns.lg\:revert-items li:nth-of-type(2) {
     order: -9999!important;
  }
}


</style>


<div class="hero" markdown>

SQL
{ .big-word }

# is all you need

Supercharge **BigQuery** with **BigFunctions**<br>
*to load, transform and activate your data.*<br><br>

[Book a Demo :octicons-arrow-right-24:](https://calendar.app.google/zu54nNMHLVw7jYWy8){ .md-button }
[Explore :octicons-arrow-right-24:](bigfunctions/){ .md-button .md-button--primary }


</div>



<!------------- TECHNOLOGIES UPON SECTION  ----------->
<div class="hero" markdown>

*Taking the most of*
{ .small }

<figure markdown="span">
  ![gcp](assets/gcp.svg){ .gray-scale .mt-neg width=200 }
</figure>

</div>

<br>

---

<!------------- POWER OF FUNCTIONS SECTION  ----------->
<div class="hero" markdown>

# The power of functions<br>with the ease of SQL

Have a data need? **There's a bigfunction for that!**<br>
*BigFunctions provides [150+ ready to use functions](bigfunctions/)</a>*

</div>


<div class="lg:two-columns lg:revert-items" markdown>

-   ## Load Data from any vendor

    Load data from Salesforce, Hubspot and hundreds of vendors with one SQL command.

    [Get Started :octicons-arrow-right-24:](bigfunctions/load_api_data/){ .md-button }

-   ![Image title](https://dummyimage.com/600x400/eee/aaa)

</div>


<div class="lg:two-columns" markdown>

-   ## Perform Anomaly Detection

    Load data from Salesforce, Hubspot and hundreds of vendors with one SQL command.

    [Get Started :octicons-arrow-right-24:](bigfunctions/load_api_data/){ .md-button }

-   ![Image title](https://dummyimage.com/600x400/eee/aaa)

</div>



<div class="hero" markdown>

*BigFunctions come with 150+ ready to use functions*

[Explore Functions :octicons-arrow-right-24:](bigfunctions/){ .md-button }

</div>

<br>

---


<div class="hero" markdown>

# The rise of <br> the SQL-Data-Stack

A data-warehouse (*bigquery*),<br>
a sql orchestrator (*dbt*)<br>
and advanced functions (*bigfunctions*)<br>
*is all you need!*

</div>


<div class="primary-background" markdown>

<div class="md:two-columns max-width-800" markdown>

-   ## Modern-Data-Stack

    ![Modern-Data-Stack is Complex](assets/modern_data_stack2.png)

    :x: **Tool Sprawl**: A multitude of tools for various tasks complicates the data workflow.

    :x: **Custom Scripting**: Reliance on custom Python scripts introduces complexity and increases maintenance overhead.

    :x: **Lack of Self-Service**: Data analysts often depend on data engineers for complex tasks, hindering agility and efficiency.


-   ## SQL-Data-Stack

    ![SQL-Data-Stack is powerfully simple](assets/sql_data_stack2.png)

    :white_check_mark: **Simplicity**: Achieve everything with SQL, thus minimizing the need for multiple tools.

    :white_check_mark: **Centralized Governance**: Control all data processes from a central data warehouse with declarative assets.

    :white_check_mark: **Self-Service**:  Empower data analysts to perform intricate tasks using SQL functions directly.

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
