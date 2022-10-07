
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

BigQuery is very powerful as you can:
- create native SQL and javascript routines,
- deploy any remote function as a *cloud function* / *cloud run* in your favorite language and with your favorite dependencies/executables.

Yet, to build solutions using these features needs time and experience and we believe data-teams should *NOT* waste effort working on challenges already solved by other data-teams. Let's share our solutions.

> 👉 **We believe open-source is the way to go for data-people to share their work, help each other, inspire from each other and avoid reinventing the wheel. That's why we created BigFunctions.**

<br>

## 👀 Explore and call open BigFunctions from you own BigQuery Project

Public and shared BigFunctions give you **SQL-superpowers** such as:

- advanced transforms such as computing sentiment score of a text, or computing the latitude, longitude of an address, run graph algorithms, etc
- advanced data-explorations/vizualisations from your BigQuery console, your notebooks, your IDE.
- communication with all your SAAS to bring a common logic orchestrated from your data-warehouse and optionnaly from dbt.

Follow the links to explore and call public BigFunctions from you own BigQuery Project:

- **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**
- **<a href="https://unytics.github.io/bigfunctions/reference/" target="_blank">Reference of public BigFunctions</a>** - callable from any BigQuery project without install
- **<a href="https://unytics.io/bigfunctions/getting_started/" target="_blank">Getting Started</a>** - call public BigFunctions from your own BigQuery project


<br>

## ⚡️ BigFunctions Framework Features

> 1. 💚**create a unique standard to define BigQuery routines be it sql/js/remote UDF or procedures**
> 2. 💚 **Provide `bigfun` a CLI (Command Line Interface) to test, deploy, document and monitor these BigQuery routines in your project**

<br>


## 💥 `bigfun` CLI

This repo contains a CLI (command-line-interface) called `bigfun` to facilitate BigFunctions development, test, deployment, documentation and monitoring.

### Install `bigfun`

**Install dependencies**

`bigfun` invokes `gcloud` CLI to deploy remote functions. Furthermore, `bigfun` uses BigQuery python client authenticated by default *gcloud app credentials*.

Thus, for `bigfun` to work, please:

- install `gcloud`
- authenticate `gcloud` by running `gcloud init`
- authenticate to create default app credentials by running `gcloud auth application-default login`.

**Install `bigfun`**

Clone the repo and from the repo directory run:

``` sh
virtualenv venv
. venv/bin/activate
pip install --editable .
```


### Get needed permissions


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

You are more than welcome to contribute both for:

- adding/improving BigFunctions
- improving the framework and `bigfun` CLI

**Contributors**

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>
