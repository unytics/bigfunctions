---
title: "{{ name }}"
description: "BigFunction {{ name }} is a BigQuery function which {{ description.split('\n')[0] }}"
{% if hide_in_doc %}
search:
  exclude: true
{% endif %}
---

<div class="breadcrumb" markdown>

{% set path_parts = filename.split('/')[:-1] %}

{% for part in path_parts -%}
- [{{ part }}](../{{ path_parts[:loop.index] | join('/') }}/README.md){% if not loop.last %}<span style="margin: 0 20px">❯</span>{% endif %}
{% endfor -%}


</div>


# {{ name }}


<div style="position: relative; top: -4rem; margin-bottom:  -4rem; text-align: right; z-index: 9999;">
  {% if author %}
  <a href="{{ author.url }}" title="{% if not author.name.startswith('Credits') %}Author: {% endif %}{{ author.name }}" target="_blank">
    <img src="{{ author.avatar_url }}" alt="author photo" width="32" style=" border-radius: 50% !important">
  </a>
  {% endif %}
  <a href="{REPO_URL}/tree/main/{{ filename }}" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>


```
{{ signature }}
```


## Description


{{ description }}



## Usage


{% if project == 'bigfunctions' %}


??? note "Call or Deploy `{{ name }}` ?"


    ??? success "Call `{{ name }}` directly"

        **The easiest way to use bigfunctions**

        - `{{ name }}` function is deployed in 39 public datasets for all of the 39 BigQuery regions.
        - It can be called by anyone. Just copy / paste examples below in your BigQuery console. It just works!
        - *(You need to use the dataset in the same region as your datasets otherwise you may have a function not found error)*

        **Public BigFunctions Datasets**

        | Region | Dataset |
        |--------|---------|
        {% for dataset in dataset.split(',') -%}
        | `{{ dataset.replace('_', '-') }}` | `{{ project }}.{{ dataset }}` |
        {% endfor -%}
        |  ...   |   ...   |


    ??? success "Deploy `{{ name }}` in your project"

        **Why deploy?**

        - You may prefer to deploy `{{ name }}` in your own project to build and manage your own catalog of functions.
        - This is particularly useful if you want to create private functions (for example calling your internal APIs).
        - Get started by reading [the framework page ](../framework.md)

        **Deployment**

        `{{ name }}` function can be deployed with:

        ```bash
        pip install bigfunctions
        bigfun get {{ name }}
        bigfun deploy {{ name }}
        ```

        {% if secrets is defined -%}
        **Requirements**

        `{{ name }}` uses the following secrets. Get them by reading the documentation link and store them in [Google Secret Manager](https://console.cloud.google.com/security/secret-manager){ target="_blank" } in the project where you deploy the function (and give Accessor role to the service account of the function):

        | name | description | documentation to get the secret |
        |------|-------------|-----|
        {% for secret in secrets -%}
        | `{{ secret.name }}` | {{ secret.description }} | [doc]({{ secret.documentation_link }}){ target="_blank" } |
        {% endfor %}
        {% endif %}


{% endif %}



{% set arguments_containing_secrets = arguments|selectattr('contains_secret')|map(attribute='name')|list %}

{% if arguments_containing_secrets %}


??? warning "Keep the secrets safe!"

    **Do NOT write secrets in plain text in your SQL queries!**

    Otherwise, anyone with access to your BigQuery logs can read and use them.

    Instead, **generate an encrypted version** that you can safely share:

    <div>
      <input id="secret-to-encrypt" type="text" class="md-input" placeholder="secret">
      <input id="authorized-users" type="text" class="md-input" placeholder="you@example.com">
      <button class="md-button md-button--primary" onclick="encrypt();">Encrypt Secret</button>
    </div>

    1. Enter a secret value below along with the emails of the users who are authorized to use it (separated by commas).
    2. Click on `Encrypt Secret`.
    3. The browser (no server is called) will generate an encrypted version and copy it in the clipboard
    4. Paste the encrypted secret into the arguments of your function exactly like if you passed the plain text version.
    5. The bigfunction will decrypt it and check that the calling user is authorized.



    ??? quote "More on secret encryption"

        Technically, this encryption system uses the same encryption mechanism used to transfer data over the internet.
        It uses a pair of a public and private keys.

        The public key (contained in this web page) is used to encrypt a text.
        The corresponding private key is the only one who is able to decrypt the text.
        The private key is stored in a secret manager and is only accessible to this function.
        Thus, this function (and this function only) can decrypt it.

        Moreover, the function will check that the caller of the function belong to the list of `authorized users`
        that you gave at encryption time.

        Thanks to this:

        - Nobody but this function will be able to decrypt it.
        - Nobody but `authorized users` can use the encrypted version in a function.
        - No function but the function `{{ name }}` can decrypt it.


{% endif %}





## Examples




{% for example in examples %}

{% if example.description %}
{% set description_parts = example.description.split('\n', 1) %}
**{% if examples|length > 1 %}{{ loop.index }}. {% endif %}{{ description_parts[0] }}**
{% if description_parts|length > 1 %}{{ description_parts[1] }}{% endif %}
{% endif %}

{% set datasets = dataset.split(',') %}
{% set nb_datasets = [(datasets|length), 3] | min %}


{% for dataset in datasets[:nb_datasets] %}


{% if datasets|length > 1 %}
=== "{% if dataset|length <=2 %}{{ dataset | upper | replace('_', '-') }}{% else %}{{ dataset | replace('_', '-') }}{% endif %}"
{% endif %}

{% filter indent(width=4 if datasets|length > 1 else 0) %}

```sql
{% if example.with_clause is defined %}
with sample_data as (

  {{ example.with_clause | indent(6) }}
)
{% endif %}
{% if example.temp_table is defined %}
create temp table sample_data as (

  {{ example.temp_table | indent(6) }}
);
{% endif %}
{% if type == 'procedure' %}call{% elif type == 'table_function' %}select * from{% else %}select{% endif %} {{ project }}.{{ dataset }}.{{ name }}({% for argument in example.arguments %}{% if argument is none or argument == 'null' %}null{% elif arguments[loop.index0]['type'] == 'string' and '\n' not in argument %}{{ argument | trim('"') | trim("'") | tojson() | replace('{BIGFUNCTIONS_DATASET}',  project + '.' + dataset ) | replace('\n', '\n      ') }}{% else %}{{ argument | replace('{BIGFUNCTIONS_DATASET}',  project + '.' + dataset ) | replace('\n', '\n      ') }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}){% if type == 'procedure' %};{% elif 'output' in bigfunction and type != 'table_function' %} as {{ output.name }}{% endif %}
{%- if (example.with_clause is defined or example.temp_table is defined) and type != 'table_function' %}
from sample_data
{% endif %}
{% if type == 'procedure' and template %}select html from bigfunction_result;{% endif %}
{%- if type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}
```

{% endfilter %}


{% endfor %}



{% if type not in ('procedure', 'table_function') and 'output' in example %}

<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
{%- set output_name_length = output.name | length -%}
{%- set output_length = example.output | length -%}
{%- set hyphens_length = [output_name_length, output_length] | max -%}
{%- set hyphens = '-' * hyphens_length -%}
{%- set name_padding_length = [0, output_length - output_name_length] | max -%}
{%- set name_padding = ' ' * name_padding_length -%}
{%- set value_padding_length = [0, output_name_length - output_length] | max -%}
{%- set value_padding = ' ' * value_padding_length -%}
+-{{ hyphens }}-+
| {{ output.name }}{{ name_padding }} |
+-{{ hyphens }}-+
| {{ example.output | escape }}{{ value_padding }} |
+-{{ hyphens }}-+
</code>
</pre>

{% endif %}

{% if type in ('procedure', 'table_function') and 'output' in example %}

<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
{{ example.output }}
</code>
</pre>

{% endif %}


{% if example.screenshot %}<a href="../{{ example.screenshot }}"><img alt="screenshot" src="../{{ example.screenshot }}" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>{% endif %}
{% endfor %}









{% if use_case is defined and use_case %}

## Use cases

{{ use_case }}
{% endif %}


{% if project == 'bigfunctions' %}

---

??? question "Need help or Found a bug?"

    ??? success "Get help using `{{ name }}`"

        The community can help! Engage the conversation on [Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q)

        **We also provide [professional suppport](../chat_with_us.md)**.


    ??? success "Report a bug about `{{ name }}`"

        If the function does not work as expected, please

        - [report a bug](https://github.com/unytics/bigfunctions/issues/new/choose) so that it can be improved.
        - or open the discussion with the community on [Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q).

        **We also provide [professional suppport](../chat_with_us.md)**.

---


[Show your :heart: by adding a :star: on :simple-github: :octicons-arrow-right-24:](https://github.com/unytics/bigfunctions){ .md-button  target="_blank" style="width: 100%; text-align: center;" }

{% endif %}



<!-------------------------------------
SCRIPT TO HANDLE SECRET ENCRYPTION SNIPPET
-------------------------------------->
<script src="https://cdn.jsdelivr.net/npm/node-forge@1.0.0/dist/forge.min.js"></script>
<script>
const pem = `
{{ public_key_to_encrypt_secrets }}
`;

const publicKey = forge.pki.publicKeyFromPem(pem);


function encrypt() {
  const plainText = document.getElementById('secret-to-encrypt').value;
  const authorizedUsers = document.getElementById('authorized-users').value;
  if (!plainText) {
    alert("Missing secret value! Please add a secret.");
    return;
  }
  if (!authorizedUsers) {
    alert("Missing Authorized users! Please add at least one user.");
    return;
  }
  const plainObj = {
    s: plainText,
    u: authorizedUsers,
  };
  const plainObjAsString = JSON.stringify(plainObj);
  const encrypted = publicKey.encrypt(plainObjAsString, 'RSA-OAEP', {
    md: forge.md.sha256.create(),
    mgf1: { md: forge.md.sha256.create() }
  });
  const encryptedB64 = forge.util.encode64(encrypted);
  navigator.clipboard.writeText(`ENCRYPTED_SECRET(${encryptedB64})`);
  alert("Successfully copied the encrypted secret in clipboard.\n\nPaste it in your query as shown in examples.");
}
</script>
