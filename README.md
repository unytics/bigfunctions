
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

Public and shared BigFunctions give you **SQL-superpowers** such as:

- advanced transforms such as computing sentiment score of a text, computing the latitude / longitude of an address, run graph algorithms, etc
- advanced data-explorations / vizualisations from your BigQuery console, your notebooks, your IDE.
- communication with all your SAAS to bring a common logic orchestrated from your data-warehouse and optionnaly from dbt.

Follow the links to explore and call public BigFunctions from you own BigQuery Project:

- **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**
- **<a href="https://unytics.github.io/bigfunctions/reference/" target="_blank">Reference of public BigFunctions</a>** - callable from any BigQuery project without install
- **<a href="https://unytics.io/bigfunctions/getting_started/" target="_blank">Getting Started</a>** - call public BigFunctions from your own BigQuery project


<br>

## ⚡️ BigFunctions Framework Features

> 1. 💚 **A standard to define BigQuery routines be it sql/js/remote UDF or procedures**
> 2. 💚 **`bigfun`: a CLI (Command Line Interface) to test, deploy, document and monitor these BigQuery routines in your project**

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
