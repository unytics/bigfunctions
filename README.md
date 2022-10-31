
![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers</em>
</p>

---

- **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**
- **<a href="https://unytics.github.io/bigfunctions/reference/" target="_blank">Reference of public BigFunctions</a>** - callable from any BigQuery project without install
- **<a href="https://unytics.io/bigfunctions/getting_started/" target="_blank">Getting Started</a>** - call public BigFunctions from your BigQuery project

---

<br>

## 🔍️ What is BigFunctions?

BigFunctions is both:

> 1. **Some Open-Source BigQuery functions giving SQL-superpowers, callable without install from any GCP project**
> 2. **A framework to define, test, deploy, document and monitor your BigQuery functions in addition to the BigFunctions available in this repo**. BigFunctions Framework Features:
>     1. 💚 **A standard to define BigQuery routines be it sql/js/remote UDF or procedures**
>     2. 💚 **`bigfun`: a CLI (Command Line Interface) to test, deploy, document and monitor these BigQuery routines in your project**


<br>


## 💡 Why BigFunctions?

- BigQuery, with native and remote routines, is really powerful.
- BigFunctions take the most of that by offering ready-to-use functions holding useful features for data-teams.
- We believe no-one should be reinventing the wheel and open-source is the best way to fight against that.
- Hey Data-People! Let's share our work, help each other and inspire from each other.
- 👉 Play and contribute to BigFunctions!

<br>

## 👀 Call public BigFunctions without install from you GCP project

All BigFunctions represented by a 'yaml' file in 'bigfunctions' folder are automatically deployed in public datasets so that you can call them directly without install from your BigQuery project. 

To explore available bigfunctions and get started to call them, visit **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**.

<br>


## 🚀 Deploy BigFunctions in your GCP project

To deploy a bigfunction named 'my_bigfunction' defined as a yaml file located in 'bigfunctions' folder simply call:

``` sh
bigfun deploy my_bigfunction
```

Details about `bigfun` command line are given below.

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
