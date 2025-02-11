# 👋 Contribute to BigFunctions

BigFunctions is fully open-source. Any contribution is more than welcome 🤗!

> - Add a ⭐ on the repo to show your support
> - [Join our Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) and talk with us
> - Suggest a new function [here](https://github.com/unytics/bigfunctions/issues/new?assignees=&labels=new-bigfunction&projects=&template=0_new_bigfunction.yaml&title=%5Bnew%5D%3A+%60function_name%28argument1%2C+argument2%29%60)
> - Raise an issue [there](https://github.com/unytics/bigfunctions/issues/new/choose)
> - Open a Pull-Request! See instructions below.


## Contributors

<a href="https://github.com/unytics/bigfunctions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=unytics/bigfunctions" />
</a>


## How to submit pull requests

To make a change to this repository:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo?tool=webui#forking-a-repository) and create your branch from `main`.
2. Clone your fork
3. Create a virtual env then install the packages (including dev packages) with `pip install -e .[dev]`
4. Make your changes.
5. Run pre-commit to follow the repo rules using `precommit run`
6. Commit and Push your changes to your fork.
7. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

(If the change is particularly small, these steps are easily accomplished directly in the GitHub UI.)


## How to create a new open-source BigFunction

Before spending a lot of time to develop a new bigfunction, don't hesitate to reach out through [bigfunctions slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) (or by email --> paul.marcombes@unytics.io).

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


## First contributor?

You can contribute by selecting one of [these issues](https://github.com/unytics/bigfunctions/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) which were tagged `good-first-issue`. If you need any help, don't hesitate to reach out through [bigfunctions slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q).


## License
By contributing to this repository, you agree that your contributions will be licensed under its MIT License.
