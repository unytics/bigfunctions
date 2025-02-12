---
title: "Join the Community"
description: "The power of BigFunctions come from its community of contributors who build functions for every data need"
search:
  exclude: true
hide:
  - navigation
---


<div class="hero" markdown>

# Powered by the Community

40+ contributors make BigFunctions shine

*More Contributors :octicons-arrow-right-24: More Functions*
{ .small }

[Join the Community :octicons-arrow-right-24:](#join-the-community){ .md-button .md-button--primary }


</div>

<br>

---

<br>

## Join the Community

!!! note ""

    BigFunctions is fully open-source. Any contribution is more than welcome :hugging:!


<div class="grid cards  " markdown>

-   [**Get Help on Slack :simple-slack:**](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q)

    ---

    Join 200+ slack members. Get help or help others.

    [Join Slack :octicons-arrow-right-24:](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q)


-   [**Attract Contributors :star:**](https://github.com/unytics/bigfunctions/)

    ---

    Add a star to bigfunctions GitHub :simple-github: to make it more visible and attract contributors.

    [Add a star on Github :octicons-arrow-right-24:](https://github.com/unytics/bigfunctions/)



-   [**Suggest a Function :bulb:**](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&projects=&template=0_new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)

    ---

    Suggesting an idea is already a great contribution. Developers may develop it faster than you think.

    [Suggest a function :octicons-arrow-right-24:](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&projects=&template=0_new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)


-   [**Report a bug :red_circle:**](https://github.com/unytics/bigfunctions/issues/new/choose)

    ---

    Found a bug? Don't let it hidden! Report it!

    [Raise an issue :octicons-arrow-right-24:](https://github.com/unytics/bigfunctions/issues/new/choose)


-   [**Get your hands-on :hugging:**](#contribute)

    ---

    Open a Pull-Request to create a new function or improve the framework.

    [See contribution guidelines :octicons-arrow-right-24:](#contribute)


-   [**Get Premium Support :magic_wand:**](https://calendar.app.google/zu54nNMHLVw7jYWy8)

    ---

    Need professional support? Need we develop a custom function for you?

    [Book a call with BigFunctions creator :octicons-arrow-right-24:](https://calendar.app.google/zu54nNMHLVw7jYWy8)

</div>



<br>



## Contributors

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>


<br>

## Contribute

!!! note ""

    BigFunctions is fully open-source. Any contribution is more than welcome 🤗!

    **Before spending a lot of time to develop**, [share your idea on slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q).


### How to submit pull requests

To make a change to this repository:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo?tool=webui#forking-a-repository) and create your branch from `main`.
2. Clone your fork
3. Create a virtual env then install the packages (including dev packages) with `pip install -e .[dev]`
4. Make your changes.
5. Run pre-commit to follow the repo rules using `precommit run`
6. Commit and Push your changes to your fork.
7. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

(If the change is particularly small, these steps are easily accomplished directly in the GitHub UI.)


### How to create a new open-source BigFunction

To start, the best is to duplicate an existing yaml file in 'bigfunctions' folder. Make sure to duplicate a file with the same type (function_sql, aggregate_function_sql, function_js, function_py, procedure) as the one you target.

Before submitting a Pull-Request, make sure:

- your BigFunction is really useful. If it takes more time to call it than to write its own code, there may be something wrong. For instance, it does not seem appropriate to create a bigfunction that we would call by `bigfunctions.eu.is_date_in_range(my_date, start_date, end_date)` rather than to write directly `my_date between start_date and end_date`.
- bigfunction name is explicit. If the function returns a boolean, it should start with `is_` or `has_`. It the function create a vizualisation in BigQuery console it should start with `explore_`.
- all arguments/output names are explicit.
- descriptions are concise.
- you provide enough examples (edge cases must be provided) but not too much (you should not provide a second example that does not provide more understanding about the function than the first one).
- you deployed sucessfully your bigfunction by calling `bigfun deploy your_bigfunction`
- you tested the bigfunction for all the examples you provided and you each time got the expected output. (we plan to create a test command line soon).
- sql keywords must me lowercased (such as `select`)


### First contributor?

You can contribute by selecting one of [these issues](https://github.com/unytics/bigfunctions/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) which were tagged `good-first-issue`. If you need any help, don't hesitate to reach out through [bigfunctions slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q).


### License
By contributing to this repository, you agree that your contributions will be licensed under its MIT License.
