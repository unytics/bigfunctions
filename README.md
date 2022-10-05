![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers, DataWarehouse in the middle</em>
</p>

---

**Documentation**: <a href="https://unytics.github.io/bigfunctions/" target="_blank">[https://unytics.github.io/bigfunctions/](https://unytics.github.io/bigfunctions/)</a>

---


## BigFunctions project is two fold


1. **Share common useful BigFunctions among the data-community.** <br>BigFunctions defined in 'bigfunctions' folder are all deployed and callable from any BigQuery project without installation. They give you new SQL-superpowers with
    - advanced transforms such as computing sentiment score of a text, or computing the latitude, longitude of an address.
    - advanced data-explorations/vizualisations from your BigQuery console, your notebooks, your IDE.
    - communication with all your SAAS to make you able to bring common logic to all your SAAS from your data-warehouse and optionnaly from dbt.
2. **Define a framework to easily develop, test and deploy routines called BigFunctions to BigQuery.**


- If you are interested in calling common BigFunctions, go [here](https://unytics.github.io/bigfunctions/).
- Otherwise if you wish to develop BigFunctions, contribute to this repo, or if you wish to deploy BigFunctions in your own GCP project, keep reading!


---


## `bigfun` CLI

This repo contains a CLI called `bigfun` to facilitate BigFunctions development, test and deployment. 


### Install


**Install and init dependencies**

As `bigfun` uses `gcloud` under the hood: 

- install `gcloud`
- authenticate `gcloud` with `gcloud init`
- authenticate `gcloud` for python by running `gcloud auth application-default login`


**Install `bigfun`**

``` sh
virtualenv venv
. venv/bin/activate
pip install --editable .
```


### Needed permissions


### Usage

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