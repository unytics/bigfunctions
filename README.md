
<p align="center">
  <img class="hero-image" src="https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png" alt="logo_and_name" style="width: 100%; max-width: 600px">
</p>

<p align="center">
    Supercharge <em>BigQuery</em><br>with <em>BigFunctions</em><br><br>
    <b>Upgrade your data impact</b><br>
    with 100+ ready-to-use BigQuery Functions<br>
    <i>(+ build a catalog of functions)</i><br>
</p>

<p align="center">
    <strong>❯
      <a href="https://unytics.io/bigfunctions/" target="_blank">Website</a> |
      <a href="https://github.com/unytics/bigfunctions" target="_blank">GitHub</a>
     ❮</strong>
</p>

---

<br>

## 🔍️ 1. What is BigFunctions?

BigFunctions is:

✅ **a framework** to build a **governed catalog of powerful BigQuery functions** at YOUR company.

✅ **100+ open-source functions to supercharge BigQuery** that you can call directly (no install) or redeploy in YOUR catalog.




<br>


## 💡 2. Why BigFunctions?


**As a data-analyst**<br>
You'll have new powers! *(such as loading data from any source or activating your data through reverse ETL)*.

**As an analytics-engineer**<br>
You'll feel at home with BigFunctions style which imitates the one of dbt *(with a yaml standard and a CLI)*.<br>
You'll love the idea of getting more things done through SQL.

**As a data-engineer**<br>
You'll easily build software-engineering best practices through unit testing, cicd, pull request validation, continuous deployment, etc.<br>
You will love avoiding reinventing the wheel by using functions already developed by the community.

**As a central data-team player in a large company**<br>
You'll be proud of providing a governed catalog of curated functions to your 10000+ employees with mutualized and maintainable effort.

**As a security champion**<br>
You will enjoy the ability to validate the code of functions before deployment thanks to your git validation workflow, CI Testing, binary authorization, etc.

**As an open-source lover**<br>
You'll be able to contribute so that a problem solved for you is solved for everyone.



<br>

## 👀 3. Call public BigFunctions without install from your GCP project

All BigFunctions represented by a 'yaml' file in *bigfunctions* folder of the GitHub repo are automatically deployed in public datasets so that you can call them directly without install from your BigQuery project.

Give it a try! Execute this SQL query from your GCP Project 👀:

```sql
select bigfunctions.eu.faker("name", "it_IT")
```


Explore all available bigfunctions **<a href="bigfunctions">here</a>**.

<br>


## 🚀 4. Deploy BigFunctions in your GCP project

You can also deploy any bigfunction in your project! To deploy *my_bigfunction* defined in *bigfunctions/my_bigfunction.yaml* file, simply call:

``` sh
bigfun deploy my_bigfunction
```

Details about `bigfun` command line are given below.

<br>


## 💥 5. `bigfun` CLI

`bigfun` CLI (command-line-interface) facilitates BigFunctions development, test, deployment, documentation and monitoring.

### 5.1 Install `bigfun` 🛠️

Clone the repo and from the repo directory run:

``` sh
virtualenv venv
. venv/bin/activate
pip install --editable .
```

### 5.2 Use `bigfun` 🔥

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



### 5.3 Deploy you first function 👨‍💻

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


### 5.4 Deploy you first javascript function which depends on *npm packages* 👽

*To deploy a **javascript** function* which depends on **npm packages** there are additional requirements *in addition to the ones above*.

> 1. You will need to install each *npm package* on your machine and bundle it into one file. For that, you need to [install *nodejs*](https://nodejs.org/en/download/).
> 2. The bundled js file will be uploaded into a cloud storage bucket in which you must have write access. The bucket name is asked when you run `bigfun deploy`. Users of your functions must have read access to the bucket.

You now can deploy `render_string` function with:

```sh
bigfun deploy render_string
```

Test it with 👀:

```sql
select PROJECT.DATASET.render_string("name", "it_IT")
```


<br>


### 5.5 Deploy you first *remote* function ⚡️

*To deploy a **remote** function* (e.g. python function), there are additional requirements *in addition to the ones of **Deploy you first function** section*.

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




## 👋 6. Contribute

BigFunctions is fully open-source. Any contribution is more than welcome 🤗!

- Add a ⭐ on the repo to show your support
- [Join our Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) and talk with us
- Suggest a new function [here](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&projects=&template=0_new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)
- Raise an issue [there](https://github.com/unytics/bigfunctions/issues/new/choose)
- Open a Pull-Request! (See [contributing instructions](https://github.com/unytics/bigfunctions/blob/main/CONTRIBUTING.md)).

<br>

**Contributors**

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>
