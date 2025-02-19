
<p align="center">
  <img class="hero-image" src="https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png" alt="logo_and_name" style="width: 100%; max-width: 600px">
</p>

<p align="center">
    <em>Supercharge BigQuery with BigFunctions</em><br><br>
</p>

---

<br>

## 🔍️ 1. Supercharge BigQuery with BigFunctions

1. BigFunctions is **a framework** to build a **governed catalog of BigQuery functions to supercharge BigQuery**.
2. It also comes with **150+ functions** built by the community that you can call directly (no install) or redeploy in YOUR catalog.
3. You can now perform any advanced data task, be it load, transform or take actions by running SQL commands in BigQuery.


[Learn more >](https://unytics.io/bigfunctions/)



<br>

## 👀 2. Call public BigFunctions without install from your GCP project

**All BigFunctions represented by a 'yaml' file in *bigfunctions* folder are deployed in public datasets**. You can then call them directly without install from your BigQuery project.

Give it a try! Execute this SQL query from your GCP Project 👀:

```sql
select bigfunctions.eu.faker("name", "it_IT")
```


[Explore open BigFunctions >](https://unytics.io/bigfunctions/bigfunctions/)

<br>


## 🚀 3. Deploy BigFunctions in your GCP project

You can also deploy any bigfunction in your project! To deploy *my_bigfunction* defined in *bigfunctions/my_bigfunction.yaml* file, simply call:

``` sh
bigfun deploy my_bigfunction
```

[Discover the framework >](https://unytics.io/bigfunctions/framework/)

<br>


## 👋 4. Contribute

BigFunctions is fully open-source. Any contribution is more than welcome 🤗!

- Add a ⭐ on the repo to show your support
- [Join our Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) and talk with us
- Suggest a new function [here](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&projects=&template=0_new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)
- Raise an issue [there](https://github.com/unytics/bigfunctions/issues/new/choose)
- Open a Pull-Request! (See [contributing instructions](https://unytics.io/bigfunctions/community/)).


<br>

**Contributors**

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>
