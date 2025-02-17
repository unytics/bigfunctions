# Introducing BigFunctions: open-source superpowers for BigQuery

Hey r/dataengineering!

I'm excited to introduce [BigFunctions](https://github.com/unytics/bigfunctions), an open-source project designed to supercharge your BigQuery data-warehouse and empower your data analysts! 

After 2 years building it, we just wrote our first [article](https://medium.com/google-cloud/sql-is-all-you-need-77554fea90c0) to announce it. 


## What is BigFunctions?

Inspired by the growing **"SQL Data Stack"** movement, BigFunctions is a framework that lets you:

- **Build a Governed Catalog of Functions**: Think dbt, but for creating and managing reusable functions directly within BigQuery.
- **Empower Data Analysts**: Give them a self-service catalog of functions to handle everything from data loading to complex transformations and action taking-- *all from SQL*!
- **Simplify Your Data Stack**: Replace messy Python scripts and a multitude of tools with clean, scalable SQL queries.


## The Problem We're Solving

The modern data stack can get complicated. Lots of tools, lots of custom scripts...it's a management headache. We believe the future is a simplified stack where SQL (and BigQuery) does it all. 

Here are some benefits:

- **Simplify the stack** by replacing a multitude of custom tools to one.
- **Enable data-analysts to do more**, directly from SQL.


## How it Works

- **YAML-Based Configuration**: Define your functions using simple YAML, just like dbt uses for transformations.
- **CLI for Testing & Deployment**: Test and deploy your functions with ease using our command-line interface.
- **Community-Driven Function Library**: Access a growing library of over 120 functions contributed by the community. 

Deploy them with a single command!


## Example:

Imagine this:

1. **Load Data**: Use a BigFunction to ingest data from any URL directly into BigQuery.
2. **Transform**: Run time series forecasting with a Prophet BigFunction.
3. **Activate**: Automatically send sales predictions to a Slack channel using a BigFunction that integrates with the Slack API.

All in SQL. No more jumping between different tools and languages.


## Why We Built This

As Head of Data at Nickel, I saw the need for a better way to empower our 25 data analysts. 

Thanks to SQL and configuration, our data-analysts at Nickel send 100M+ communications to customers every year, personalize content on mobile app based on customer behavior and call internal APIs to take actions based on machine learning scoring.  

I built BigFunctions 2 years ago as an open-source project to benefit the entire community. So that any team can empower its SQL users.

Today, I think it has been used in production long enough to announce it publicly. Hence this first [article on medium](https://medium.com/google-cloud/sql-is-all-you-need-77554fea90c0). 

The road is not finished; we still have a lot to do. Stay tuned for the journey.

Stay connected and follow us on [GitHub](https://github.com/unytics/bigfunctions), [Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) or [Linkedin](https://www.linkedin.com/company/unytics/).