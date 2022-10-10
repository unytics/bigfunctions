
![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers</em>
</p>

---

- **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**
- **<a href="https://unytics.github.io/bigfunctions/reference/" target="_blank">Reference of public BigFunctions</a>** - callable from any BigQuery project without install
- **<a href="https://unytics.io/bigfunctions/getting_started/" target="_blank">Getting Started</a>** - call public BigFunctions from your own BigQuery project

---

<br>

## 🔍️ What is BigFunctions?

It is both:

> 1. **Open BigQuery functions giving SQL-superpowers, callable without install from any BigQuery project**
> 2. **A framework to define, test, deploy, document and monitor BigQuery Routines**

<br>


## 💡 Why BigFunctions?

- BigQuery, with native and remote routines, is really powerful.
- BigFunctions take the most of that by offering ready-to-use functions holding useful features for data-teams.
- We believe no-one should be reinventing the wheel and open-source is the best way to fight against that.
- Hey Data-People! Let's share our work, help each other and inspire from each other.
- 👉 Play and contribute to BigFunctions!

<br>

## 👀 Explore and call open BigFunctions from you own BigQuery Project

Follow the links to explore and call public BigFunctions from you own BigQuery Project:

- **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**
- **<a href="https://unytics.github.io/bigfunctions/reference/" target="_blank">Reference of public BigFunctions</a>** - callable from any BigQuery project without install
- **<a href="https://unytics.io/bigfunctions/getting_started/" target="_blank">Getting Started</a>** - call public BigFunctions from your own BigQuery project


!!! note ""


    **👀 Explore**

    - [<code>explore_column(fully_qualified_column)</code>](#explore_column): Show column statistics
    - [<code>explore_dataset(fully_qualified_dataset)</code>](#explore_dataset): Shows infos about dataset tables
    - [<code>explore_table(fully_qualified_table)</code>](#explore_table): Show table infos and column statistics


    **✨ Transform string**

    - [<code>levenshtein(string1, string2)</code>](#levenshtein): Computes levenshtein distance between `string1` and `string2`
    - [<code>render_string(template, context)</code>](#render_string): Render template with context using nunjucks.js templating library
    - [<code>sentiment_score(content)</code>](#sentiment_score): Compute sentiment score of text


    **📆 Transform date**

    - [<code>is_public_holiday(date, country_code)</code>](#is_public_holiday): Returns true if `date` corresponds to a public holiday in `country_code`


    **🌐 Graph**

    - [<code>connected_components(fully_qualified_table)</code>](#connected_components): Compute the connected components of a non-directed graph.


    **💬 Notify**

    - [<code>notify_gmail(recipients, subject, body, attachment_filename, attachment_content)</code>](#notify_gmail): Send email via gmail


    **🚀 Export**

    - [<code>export_to_gmail(table_or_view_or_query, recipients, email_subject, email_body)</code>](#export_to_gmail): Send email (via gmail) with data attached as excel file


    **🔨 Utils**

    - [<code>chart(data, chart_type, ylabel)</code>](#chart): Returns html with a chartjs chart
    - [<code>dump_to_excel(data)</code>](#dump_to_excel): Dump data to excel file returned as base64
    - [<code>get_table_columns(fully_qualified_table)</code>](#get_table_columns): Get the column information of the given table from `INFORMATION_SCHEMA.COLUMNS`



<br>

## ⚡️ BigFunctions Framework Features

> 1. 💚 **A standard to define BigQuery routines be it sql/js/remote UDF or procedures**
> 2. 💚 **`bigfun`: a CLI (Command Line Interface) to test, deploy, document and monitor these BigQuery routines in your project**

<br>


## 💥 `bigfun` CLI

This repo contains a CLI (command-line-interface) called `bigfun` to facilitate BigFunctions development, test, deployment, documentation and monitoring.

### Install `bigfun`

**Install dependencies**

`bigfun` invokes `gcloud` CLI to deploy remote functions. Furthermore, `bigfun` uses BigQuery python client using your default *gcloud app credentials*.

Thus, for `bigfun` to work, please:

- install `gcloud`
- authenticate `gcloud` by running `gcloud init`
- create your default app credentials by running `gcloud auth application-default login`.

**Install `bigfun`**

Clone the repo and from the repo directory run:

``` sh
virtualenv venv
. venv/bin/activate
pip install --editable .
```

**Get needed permissions**

[TODO]


### Use `bigfun` 🔥

``` sh
$ bigfun --help
Usage: bigfun [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  deploy  Deploy BIGFUNCTION
  doc     Generate, serve and publish documentation
  test    Test BIGFUNCTION
```

<br>

## Contribute

You are more than welcome to contribute for both:

- adding/improving BigFunctions
- improving the framework and `bigfun` CLI

See [contributing instructions](https://github.com/unytics/bigfunctions/blob/main/CONTRIBUTING.md) for more details.

**Contributors**

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>
