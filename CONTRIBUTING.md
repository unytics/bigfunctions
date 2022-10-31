# Contributing to 🤗 BigFunctions
Thanks for your interest in helping out! Feel free to comment, open issues, and create pull requests if there's something you want to share. It also helps us if you spread the word! Reference the repo in blog posts, shout out on Twitter every time it has helped you, or simply ⭐️ the repository to say thank you!



## Submitting pull requests
To make a change to this repository, the best way is to use pull requests:

1. Fork the repository and create your branch from `main`.
2. Make your changes.
6. Create a pull request.

(If the change is particularly small, these steps are easily accomplished directly in the GitHub UI.)

## Creating a new BigFunction

Before spending a lot of time to develop a new bigfunction, don't hesitate to reach out through [bigfunctions slack](https://join.slack.com/t/bigfunctions/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q) (or by email --> paul.marcombes@unytics.io).

To start, the best is to duplicate an existing yaml file in 'bigfunctions' folder. Make sure to duplicate a file with the same type (function_sql, function_js, function_py, procedure) as the one you target.

Before submitting a PR, make sure:

- your BigFunction is really useful. If it takes more time to call it than to write its own code, there may be something wrong. For instance, it does not seem appropriate to create a bigfunction that we would call by `bigfunctions.eu.is_date_in_range(my_date, start_date, end_date)` rather than to write directly `my_date between start_date and end_date`.
- bigfunction name is explicit. If the function returns a boolean, it should start with `is_` or `has_`. It the function create a vizualisation in BigQuery console it should start with `explore_`. 
- all arguments/output names are explicit. 
- descriptions are concise.
- you provide enough examples (edge cases must be provided) but not too much (you should not provide a second example that does not provide more understanding about the function than the first one).
- you deployed sucessfully your bigfunction by calling `bigfun deploy your_bigfunction`
- you tested the bigfunction for all the examples you provided and you each time got the expected output. (we plan to create a test command line soon).

## Report bugs using Github's issues
We use GitHub issues to track bugs. Report a bug or start a conversation by opening a new issue.

## License
By contributing to this repository, you agree that your contributions will be licensed under its MIT License.

## References
This document was adapted from the GitHub Gist of [briandk](https://gist.github.com/briandk/3d2e8b3ec8daf5a27a62) and used some of Hugging Face one.
