---
title: "Introducing SQL Data Stack"
description: |
  Tired of complex data stacks? Discover the SQL Data Stack: a new paradigm that uses SQL for data ingestion, transformation, and activation, empowering analysts and simplifying your data workflow
---


# The SQL Data Stack: A New Paradigm for Data Platforms

**By Paul Marcombes  •  2025-02-05**

Hey everyone, I'm Paul, the Head of Data at Nickel.

For six years, I've been immersed in the world of data, watching our user base on BigQuery grow from a handful to over 200. But more than just managing growth, **I've been focused on a concept close to my heart: empowering data analysts**.

Today, I want to talk about a concept that I believe is the future of data stacks: the **SQL Data Stack**. It's not just a buzzword; it's a transformative approach to how we handle data, making SQL the centerpiece of our data operations.


![paul introducing sql data stack](../../assets/blog/2025-02-05_introducing_sql_data_stack.png){ style="max-width: 400px" }
<figure markdown="span">
</figure>


## The Problem with Today’s Data Stack

Let’s face it, the modern data stack, for all its strengths, is complex. We've got this plethora of tools around data warehouses. These tools, while powerful, often don't quite fit our custom needs. And what do we do? **We end up with a myriad of custom Python scripts** for data ingestion, transformation, and actions. It becomes a complex beast to manage.

## The Vision: A Single Data Warehouse

Imagine a world where your data warehouse isn't just a storage unit but a dynamic, all-encompassing tool. A world where you don’t need a multitude of external tools or a patchwork of scripts. This is the essence of the SQL data stack. It’s about **leveraging the power of SQL within your data warehouse to do everything** — from data ingestion and transformation to activation and beyond.

## What is the SQL Data Stack?

The SQL Data Stack is a paradigm shift.

**It's about having a rich set of functions within the data warehouse** that you call in SQL and that can handle any task:

1.  **Load Data from any source** :octicons-arrow-right-24: run a SQL query
2.  **Make Advanced Transforms** :octicons-arrow-right-24: run a SQL query
3.  **Take Actions from data** :octicons-arrow-right-24: run a SQL query


## The Benefits of Embracing SQL Data Stack

Adopting this approach comes with some exciting benefits:

*   **Simplification:** Imagine replacing numerous tools and Python scripts with SQL queries calling specialized functions. That’s the simplicity we’re aiming for.
*   **Self-Served Data Analysts:** We talk a lot about self-service BI, but what about self-service for data analysts? It’s about giving them a catalog of functions to meet all their needs, right within the data warehouse.
*   **Empowerment:** At Nickel, our data analysts are fully embedded in teams. They handle everything from ingestion to actions, using tools created by our data platform engineers. This is the kind of empowerment the SQL Data Stack promises.


## Introducing BigFunctions: Making SQL Data Stack a Reality

This brings me to BigFunctions, an open-source project I created to extend the concept of self-service data analysis beyond just Nickel. BigFunctions is essentially a framework, much like dbt, but for building a catalog of functions within your data warehouse.

## How BigFunctions Works

*   **BigFunctions is first a framework:** Like dbt uses SQL and YAML files for transformations, BigFunctions uses YAML to configure functions.
*   **CLI for Testing and Deployment:** Similar to dbt, it offers a command-line interface to test and deploy these functions.
*   **Community-Driven:** It comes with a growing community of contributors, currently boasting over 120 functions that you can deploy with one command.

## A Practical Example: The Power of Three Functions

Let me illustrate with a simple example. Using BigFunctions, you can:

1.  **Load Data:** Use a function to load any file from the internet directly into your data warehouse.
2.  **Transform:** Apply advanced transformations, like forecasting using the Prophet library, all within SQL.
3.  **Activate:** Send insights or data directly to where it’s needed, like sending a Slack message with sales predictions.

## The Advantages Are Clear

*   **Separation of Responsibilities:** Data-platform engineers create the tools, and data analysts use them independently.
*   **Powered by Community:** Over 120 functions and 30 contributors, ready to use.
*   **Simplicity and Scalability:** A streamlined, reliable, and scalable approach to data management.

## Join the Movement

If you’re as excited about the SQL data stack as I am, I invite you to explore [BigFunctions](../../index.md).

Check out the [GitHub repo](https://github.com/unytics/bigfunctions), contribute, or just add a star (🙏) if you like what you see.

And if you’re keen to dive deeper or have questions, let’s connect on [LinkedIn](https://www.linkedin.com/in/paul-marcombes/). I’m always eager to discuss how we can push the boundaries of data management and empower our teams.

Together, let’s make the SQL data stack the new way!


---

## Replay on Youtube

[Watch the Replay (in French) :simple-youtube:](https://www.youtube.com/watch?v=ehB80iZjdwU)

[![Youtube Video](https://img.youtube.com/vi/ehB80iZjdwU/0.jpg)](https://www.youtube.com/watch?v=ehB80iZjdwU)
