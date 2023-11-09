
![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers</em>
</p>

<p align="center">
    <strong>❯ <a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a> ❮</strong>
</p>

---

<br>

## 🔍️ What is BigFunctions?

BigFunctions is:

✅ **a framework** to build a **governed catalog of powerful BigQuery functions** at YOUR company.

✅ **open-source functions to supercharge BigQuery** that you can call directly (no install) or redeploy in YOUR catalog.




<br>


## 💡 Why BigFunctions?

BigQuery, with native and remote routines, is really powerful. **BigFunctions take the most of that by offering ready-to-use functions + tooling to boost your data-teams**.

We believe no-one should be reinventing the wheel and open-source is the best way to fight against that.

Now let's Play 👇

<br>

## 👀 Call public BigFunctions without install from you GCP project

All BigFunctions represented by a 'yaml' file in *bigfunctions* folder are automatically deployed in public datasets so that you can call them directly without install from your BigQuery project.

Give it a try! Execute this SQL query from your GCP Project 👀:

```sql
select bigfunctions.eu.faker("name", "it_IT")
```


To explore all available bigfunctions and to get started, visit **<a href="https://unytics.github.io/bigfunctions/" target="_blank">BigFunctions website</a>**.

<br>


## 🚀 Deploy BigFunctions in your GCP project

You can also deploy any bigfunction in your project! To deploy *my_bigfunction* defined in *bigfunctions/my_bigfunction.yaml* file, simply call:

``` sh
bigfun deploy my_bigfunction
```

Details about `bigfun` command line are given below.

<br>


## 💥 `bigfun` CLI

`bigfun` CLI (command-line-interface) facilitates BigFunctions development, test, deployment, documentation and monitoring.

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
> 3. Get or create a `DATASET` where you have permission to edit data and where the function will be deployed.
> 4. The `DATASET` must belong to a `PROJECT` in which you have permission to run BigQuery queries.

You now can deploy `is_email_valid` function with:

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


### Deploy you first *remote* function ⚡️

*To deploy a **remote** function* (e.g. python function), there are additional requirements *in addition to the ones above*.

> 1. A *Cloud Run* service will be deployed to host the code ([as seen here](https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions)). So you must have [permissions to deploy a *Cloud Run* service](https://cloud.google.com/run/docs/deploying-source-code#permissions_required_to_deploy) in your project `PROJECT`.
> 2. `gcloud` CLI will be used directly to deploy the service (using `gcloud run deploy`). Then, make sure you are logged in with `gcloud` by calling: `gcloud auth login`. A browser window should also open, and you should be prompted to log into your Google account. WARNING: you read correctly: you have to authenticate twice. Once for bigquery python client (to deploy any function including remote as seen above.) and once now to use `gcloud` (to deploy a *Cloud Run* service).
> 3. A *BigQuery Remote Connection* will be created to link BigQuery with the *Cloud Run* service. You then should have permissions to create a remote connection. *[BigQuery Connection Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.connectionAdmin)* or *[BigQuery Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.admin)* roles have these permissions.
> 4. A service account will be automatically created by Google along with the *BigQuery Remote Connection*. BigQuery will use this service account of the remote connection to invoke the *Cloud Run* service. You then must have the permission to authorize this service account to invoke the *Cloud Run* service. This permission is provided in the role *[roles/run.admin](https://cloud.google.com/run/docs/reference/iam/roles)*


You now can deploy `faker` function with:

```sh
bigfun deploy faker
```

Test it with 👀:

```sql
select PROJECT.DATASET.faker("name", "it_IT")
```


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
