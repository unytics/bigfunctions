---
title: "BigFunctions Framework helps you build a catalog of BigQuery functions"
description: |
  BigFunctions is a framework to build
  a catalog of functions in BigQuery
  Like dbt, it comes with a yaml standard and
  a Command-Line-Interface to test, deploy
  and generate a documentation website
hide:
  - navigation
---


<div class="hero" markdown>

# BigFunctions Framework

Build a catalog of BigQuery functions<br>
using BigFunctions Framework<br>

[Discover the framework :octicons-arrow-right-24:](#discover-the-framework){ .md-button .md-button--primary }

</div>

<br>

---

<br>


## Discover the framework

<div class="lg:two-columns lg:revert-items" markdown>

-   ### A YAML Standard

    Each function is defined in a **yaml file** *(with its author, description, arguments, examples, code, etc)*


    Yaml files are used to **test & deploy the functions** and **generate a documentation website** (such as this website).

-   ![function yaml](assets/yaml.png)

</div>


<div class="lg:two-columns" markdown>

-   ### A Command Line Interface

    `bigfun` CLI is installable with one `pip install` and enables you to:

    - get the yaml file of a public function
    - test the function
    - deploy it
    - generate a documentation website (such as this website)



-   ![bigfun command line interface](assets/bigfun.png)

</div>


<div class="lg:two-columns lg:revert-items" markdown>

-   ### A Documentation Website

    The command line interface generates your catalog of the available functions in your company with use cases and examples.

    **Foster self-service for your data-people!**

-   ![website screenshot](assets/catalog.png){ .primary-border }

</div>


## Get Started!

`bigfun` CLI (command-line-interface) facilitates BigFunctions development, test, deployment, documentation and monitoring.

### 1. Install `bigfun` 🛠️


``` sh
pip install bigfunctions
```

### 2. Use `bigfun` 🔥

``` sh
$ bigfun --help
Usage: bigfun [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  deploy      Deploy BIGFUNCTION
  docs        Generate, serve and publish documentation
  get         Download BIGFUNCTION yaml file from unytics/bigfunctions...
  test        Test BIGFUNCTION
```


### 3. Create you first function 👷

Functions are defined as yaml files under `bigfunctions` folder. To create your first function locally, the easiest is to download an existing yaml file of unytics/bigfunctions Github repo.

For instance to download `is_email_valid.yaml` into bigfunctions folder, do:

```sh
bigfun get is_email_valid
```

You can then update the file to suit your needs.




### 4. Deploy you first function 👨‍💻

> 1. Make sure the `gcloud` command is [installed on your computer](https://cloud.google.com/sdk/docs/install)
> 2. Activate the application-default account with `gcloud auth application-default login`. A browser window should open, and you should be prompted to log into your Google account. Once you've done that, `bigfun` will use your oauth'd credentials to connect to BigQuery through BigQuery python client!
> 3. Get or create a `DATASET` where you have permission to edit data and where the function will be deployed.
> 4. The `DATASET` must belong to a `PROJECT` in which you have permission to run BigQuery queries.

You now can deploy the function `is_email_valid` defined in `bigfunctions/is_email_valid.yaml` yaml file by running:

```sh
bigfun deploy is_email_valid
```

> The first time you run this command it will ask for `PROJECT` and `DATASET`.
>
> Your inputs will be written to `config.yaml` file in current directory so that you won't be asked again (unless you delete the entries in `config.yaml`). You can also override this config at deploy time: `bigfun deploy is_email_valid --project=PROJECT --dataset=DATASET`.


Test it with 👀:

```sql
select PROJECT.DATASET.is_email_valid('paul.marcombes@unytics.io')
```

<br>


### 5. Deploy you first javascript function which depends on *npm packages* 👽

*To deploy a **javascript** function* which depends on **npm packages** there are additional requirements *in addition to the ones above*.

> 1. You will need to install each *npm package* on your machine and bundle it into one file. For that, you need to [install *nodejs*](https://nodejs.org/en/download/).
> 2. The bundled js file will be uploaded into a cloud storage bucket in which you must have write access. The bucket name must be provided in `config.yaml` file in a variable named `bucket_js_dependencies`. Users of your functions must have read access to the bucket.

You now can deploy the function `render_template` defined in `bigfunctions/render_template.yaml` yaml file by running:

```sh
bigfun deploy render_template
```

Test it with 👀:

```sql
select PROJECT.DATASET.render_template('Hello {{ user }}', json '{"user": "James"}')
```


<br>


### 6. Deploy you first *remote* function ⚡️

*To deploy a **remote** function* (e.g. python function), there are additional requirements *in addition to the ones of **Deploy you first function** section*.

> 1. A *Cloud Run* service will be deployed to host the code ([as seen here](https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions)). So you must have [permissions to deploy a *Cloud Run* service](https://cloud.google.com/run/docs/deploying-source-code#permissions_required_to_deploy) in your project `PROJECT`.
> 2. `gcloud` CLI will be used directly to deploy the service (using `gcloud run deploy`). Then, make sure you are logged in with `gcloud` by calling: `gcloud auth login`. A browser window should also open, and you should be prompted to log into your Google account. WARNING: you read correctly: you have to authenticate twice. Once for bigquery python client (to deploy any function including remote as seen above.) and once now to use `gcloud` (to deploy a *Cloud Run* service).
> 3. A *BigQuery Remote Connection* will be created to link BigQuery with the *Cloud Run* service. You then should have permissions to create a remote connection. *[BigQuery Connection Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.connectionAdmin)* or *[BigQuery Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.admin)* roles have these permissions.
> 4. A service account will be automatically created by Google along with the *BigQuery Remote Connection*. BigQuery will use this service account of the remote connection to invoke the *Cloud Run* service. You then must have the permission to authorize this service account to invoke the *Cloud Run* service. This permission is provided in the role *[roles/run.admin](https://cloud.google.com/run/docs/reference/iam/roles)*


You now can deploy the function `faker` defined in `bigfunctions/faker.yaml` yaml file by running:

```sh
bigfun deploy faker
```

Test it with 👀:

```sql
select PROJECT.DATASET.faker("name", "it_IT")
```


<br>


## ❓ FAQ

<details>
  <summary><strong>How to define specific parameters for cloud run of python functions?</strong></summary>

  In yaml files you can add a `cloud_run` field with cloud run parameters. Any argument of <a href="https://cloud.google.com/sdk/gcloud/reference/run/deploy">'cloud run deploy' command</a> can be put under `cloud_run` field.

  You can see an example <a href="https://github.com/unytics/bigfunctions/blob/main/bigfunctions/get_data/load_api_data_into_temp_dataset.yaml#L339">here</a>.

  You can also put the same config in your `config.yaml` file to define default values (useful for defining a default service account for functions). The arguments defined in `config.yaml` will be overriden by the arguments (if defined) defined in the function yaml files.
</details>
<details>
  <summary><strong>How to change the cloud run service account for python functions?</strong></summary>

  By default, your default compute service account is used when deploying cloud run. To change that, see the previous FAQ item which show how to define specific parameters for cloud run.
</details>
<details>
  <summary><strong>How to correctly highlight <code>sql</code>, <code>python</code> and <code>javascript</code> code in yaml files?</strong></summary>

  In yaml files multiline string are by default highlighted as strings. That makes reading <code>code</code> field hard to read (with all code in the same string color). To correctly highlight the code regarding its python / javascript / sql syntax, you can install <a href="https://marketplace.visualstudio.com/items?itemName=harrydowning.yaml-embedded-languages">YAML Embedded Languages</a> VSCode extension.
</details>
