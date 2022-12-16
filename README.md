
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

> 1. **Some Open-Source BigQuery functions (💪 hello SQL-superpowers) callable without install from any GCP project**
> 2. **A framework to define, test, deploy, document and monitor your own BigQuery functions** (in addition to the ones available in this repo). 👉 BigFunctions Framework Features:
>     1. 💚 **A standard to define BigQuery routines as yaml files be it sql/js/remote UDF or procedures**
>     2. 💚 **`bigfun`: a CLI (Command Line Interface) to test, deploy, document and monitor these BigQuery routines in your project**


<br>


## 💡 Why BigFunctions?

BigQuery, with native and remote routines, is really powerful. **BigFunctions take the most of that by offering ready-to-use functions holding useful features for data-teams**.

We believe no-one should be reinventing the wheel and open-source is the best way to fight against that. Hey Data-People! Let's share our work, help each other and inspire from each other. 👉 Play and contribute to BigFunctions!

<br>

## 👀 Call public BigFunctions without install from you GCP project

All BigFunctions represented by a 'yaml' file in 'bigfunctions' folder are automatically deployed in public datasets so that you can call them directly without install from your BigQuery project.

To explore available bigfunctions and to get started, visit **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**.

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

### Install `bigfun` 🛠️

Clone the repo and from the repo directory run:

``` sh
virtualenv venv
. venv/bin/activate
pip install --editable .
```

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



### Deploy you first function 👨‍💻

> 1. Make sure the `gcloud` command is [installed on your computer](https://cloud.google.com/sdk/docs/install)
> 2. Activate the application-default account with `gcloud auth application-default login`. A browser window should open, and you should be prompted to log into your Google account. Once you've done that, `bigfun` will use your oauth'd credentials to connect to BigQuery through BigQuery python client!
> 3. Get permissions to edit a dataset `DATASET` in a project `PROJECT` and to run BigQuery queries in that project.


You should then be able to deploy the function `is_email_valid` by simply running

```
bigfun deploy PROJECT.DATASET.is_email_valid
```

Test it with ➡ `select PROJECT.DATASET.is_email_valid('paul.marcombes@unytics.io')` !

<br>


### Deploy you first *remote* function ⚡️

*To deploy a **remote** function* (e.g. python function), there are additional requirements *in addition to the ones above*.

> 1. A *Cloud Run* service will be deployed to host the code ([as seen here](https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions)). So you must have permissions to deploy a *Cloud Run* service in your project `PROJECT`.
> 2. `gcloud` CLI will be used directly to deploy the service (using `gcloud run deploy`). Then, make sure you are logged in with `gcloud` by calling: `gcloud auth login`. A browser window should also open, and you should be prompted to log into your Google account. WARNING: you read correctly: you have to authenticate twice. Once for bigquery python client (to deploy any function including remote as seen above.) and once now to use `gcloud` (to deploy a *Cloud Run* service).
> 3. A *BigQuery Remote Connection* will be created to link BigQuery with the *Cloud Run* service. You then should have permissions to create a remote connection. *[BigQuery Connection Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.connectionAdmin)* or *[BigQuery Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.admin)* roles have these permissions.
> 4. A service account will be automatically created by Google along with the *BigQuery Remote Connection*. BigQuery will use this service account of the remote connection to invoke the *Cloud Run* service. You then must have the permission to authorize this service account to invoke the *Cloud Run* service. This permission is provided in the role *[roles/run.admin](https://cloud.google.com/run/docs/reference/iam/roles)*


You now should be able to deploy `sentiment_score` function by running

```
bigfun deploy PROJECT.DATASET.sentiment_score
```

To make this specific function work, you first must [enable Google Cloud NLP API](https://cloud.google.com/natural-language/docs/setup#api) in your project `PROJECT`. You can then test it with ➡ `select PROJECT.DATASET.sentiment_score('This is awesome!')` !


<br>



## Contribute

You are more than welcome to contribute by:

- adding a ⭐ on this repo 😁
- reporting an issue [here](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=bug-bigfun-CLI&template=3_bug_bigfun_cli.yaml&title=%5Bbug%5D%3A+it+does+not+work).
- suggesting new functions [here](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&template=new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)
- adding/improving BigFunctions
- improving the framework and `bigfun` CLI

See [contributing instructions](https://github.com/unytics/bigfunctions/blob/main/CONTRIBUTING.md) for more details.

**Contributors**

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>
