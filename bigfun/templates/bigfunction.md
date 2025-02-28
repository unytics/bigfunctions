---
title: "{{ name }} - BigQuery function"
description: "BigFunction {{ name }} is a BigQuery function which {{ description.split('\n')[0] }}"
hide:
  - navigation
  - toc
{% if hide_in_doc %}
search:
  exclude: true
{% endif %}
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > {{ name }}
</span>

# {{ name }}


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  {% if author %}
  <a href="{{ author.url }}" title="{% if not author.name.startswith('Credits') %}Author: {% endif %}{{ author.name }}" target="_blank">
    <img src="{{ author.avatar_url }}" alt="author photo" width="32" style=" border-radius: 50% !important">
  </a>
  {% endif %}
  <a href="{REPO_URL}/tree/main/{{ filename }}" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>


{% if project == 'bigfunctions' %}

??? note "Call or Deploy `{{ name }}` ?"


    ??? success "Call `{{ name }}` directly"

        - `{{ name }}` function is deployed in 39 public datasets for all of the 39 BigQuery regions.
        - *You need to use the dataset in the same region as your datasets (otherwise you may have a function not found error).*
        - It can be called by anyone. Just copy / paste examples below in your BigQuery console. It just works!

        Public BigFunctions Datasets:

        | Region | Dataset |
        |--------|---------|
        {% for dataset in dataset.split(',') -%}
        | `{{ dataset.replace('_', '-') }}` | `{{ project }}.{{ dataset }}` |
        {% endfor -%}
        |  ...   |   ...   |


    ??? success "Deploy `{{ name }}` in your project"

        - You may prefer to deploy the BigFunction in your own project to build and manage your own catalog of functions.
        - This is particularly useful if you want to create private functions (for example calling your internal APIs).
        - :octicons-arrow-right-24: Get started by reading [the framework page ](../framework.md)

        `{{ name }}` function can be deployed with:

        ```bash
        pip install bigfunctions
        bigfun get {{ name }}
        bigfun deploy {{ name }}
        ```

        {% if secrets is defined -%}
        `{{ name }}` function depends on secrets. For it to work you must store the following secrets in [Google Secret Manager](https://console.cloud.google.com/security/secret-manager){ target="_blank" } in the same project where you deploy the function (and give Accessor role to the service account of the function):

        | name | description | documentation to get the secret |
        |------|-------------|-----|
        {% for secret in secrets -%}
        | `{{ secret.name }}` | {{ secret.description }} | [doc]({{ secret.documentation_link }}){ target="_blank" } |
        {% endfor %}
        {% endif %}




{% endif %}



## Description

**Signature**

```
{{ signature }}
```

**Description**

{{ description }}




{% set arguments_containing_secrets = arguments|selectattr('contains_secret')|map(attribute='name')|list %}

{% if arguments_containing_secrets %}


## ⚠️ Encrypt your secrets!

!!! note ""

    *Do NOT write secrets in plain text in your SQL queries!*

Otherwise, anyone with access to your BigQuery logs can read them.

Instead, generate an encrypted version of your secret that you can safely share.

> *Enter a secret value to encrypt below along with the emails of the users who are authorized to use it.*
> *It will generate an encrypted version that you can paste into the arguments of your function (exactly like if you passed the plain text version).*
> *If a user, who is not in the auhorized users list, tries to use the encrypted version, the function will raise a permission error.*
> *Besides, the encrypted version can only be used with this function `{{ name }}`.*


!!! example "Encrypt a secret"

    <div>
      <input id="secret-to-encrypt" type="text" class="md-input" placeholder="secret">
      <input id="authorized-users" type="text" class="md-input" placeholder="you@example.com">
      <button class="md-button md-button--primary" onclick="encrypt();">Encrypt Secret</button>
    </div>


??? info "How secret encryption works"

    Technically, this encryption system uses the same encryption mechanism used to transfer data over the internet.
    It uses a pair of a public and private keys.

    The public key (contained in this web page) is used to encrypt a text.
    The corresponding private key is the only one who is able to decrypt the text.
    The private key is stored in a secret manager and is only accessible to this function.
    Thus, this function (and this function only) can decrypt it.

    Moreover, the function will check that the caller of the function belong to the kist of `authorized users`
    that you gave at encryption time.

    Thanks to this:

    - Nobody but this function will be able to decrypt it.
    - Nobody but `authorized users` can use the encrypted version in a function.
    - No function but the function `{{ name }}` can decrypt it.


{% endif %}






{% if template or (output and output.name == 'html') %}

??? example "See the result as a data visualization in BigQuery Console!"

    **The result of this function can be vizualized as an html report directly in BigQuery Console!**

    1. Install this bookmarklet: <a href="javascript:(function()%7Blet%20isChartJsLoaded%20%3D%20false%3B%0Alet%20isGoogleChartsLoaded%20%3D%20false%3B%0Alet%20isFunnelGraphJsLoaded%20%3D%20false%3B%0A%0A%0Awindow.escapeHTML%20%3D%20function(html)%20%7B%0A%20%20if(!trustedTypes)%20%7B%0A%20%20%20%20return%20html%3B%0A%20%20%7D%0A%20%20const%20policy%20%3D%20trustedTypes.createPolicy(%22forceInner%22%2C%20%7BcreateHTML%3A%20(to_escape)%20%3D%3E%20to_escape%7D)%3B%0A%20%20return%20policy.createHTML(html)%3B%0A%7D%3B%0A%0A%0Aconst%20escapeScript%20%3D%20function(script)%20%7B%0A%20%20if(!trustedTypes)%20%7B%0A%20%20%20%20return%20script%3B%0A%20%20%7D%0A%20%20const%20policy%20%3D%20trustedTypes.createPolicy(%22forceInner%22%2C%20%7BcreateScript%3A%20(to_escape)%20%3D%3E%20to_escape%7D)%3B%0A%20%20return%20policy.createScript(script)%3B%0A%7D%3B%0A%0A%0Aconst%20setInnerHTML%20%3D%20function(elm%2C%20html)%20%7B%0A%20%20elm.innerHTML%20%3D%20window.escapeHTML(html)%3B%0A%20%20Array.from(elm.querySelectorAll('script')).forEach(%20oldScript%20%3D%3E%20%7B%0A%20%20%20%20%20%20const%20newScript%20%3D%20document.createElement('script')%3B%0A%20%20%20%20%20%20Array.from(oldScript.attributes).forEach(%20attr%20%3D%3E%20newScript.setAttribute(attr.name%2C%20attr.value)%20)%3B%0A%20%20%20%20%20%20newScript.text%20%3D%20escapeScript(oldScript.innerHTML)%3B%0A%20%20%20%20%20%20oldScript.parentNode.replaceChild(newScript%2C%20oldScript)%3B%0A%20%20%7D)%3B%0A%7D%3B%0A%0A%0Aconst%20run%20%3D%20async%20function()%20%7B%0A%20%20if%20(!isChartJsLoaded%20%7C%7C%20!isGoogleChartsLoaded%20%7C%7C%20!isFunnelGraphJsLoaded)%20%7B%0A%20%20%20%20return%3B%0A%20%20%7D%0A%20%20const%20results_table_container%20%3D%20document.querySelector('bq-tab-content%3Anot(.cfc-hidden)%20bq-results-table')%3B%0A%20%20if%20(!results_table_container)%20%7B%0A%20%20%20%20return%3B%0A%20%20%7D%0A%20%20const%20cells%20%3D%20results_table_container.querySelectorAll('td%20div%3Anot(.cfc-flex-container)')%3B%0A%20%20if%20(cells.length%20!%3D%3D%201)%20%7B%0A%20%20%20%20return%3B%0A%20%20%7D%0A%20%20const%20cell%20%3D%20cells%5B0%5D%3B%0A%20%20const%20content%20%3D%20cell.innerText%3B%0A%20%20if%20(!content.startsWith(%22%3Chtml%22))%20%7B%0A%20%20%20%20return%3B%0A%20%20%7D%0A%20%20if%20(content.endsWith(%22...%22))%20%7B%0A%20%20%20%20cell.nextElementSibling.firstElementChild.click()%3B%0A%20%20%20%20return%3B%0A%20%20%7D%0A%20%20const%20html%20%3D%20%60%3Csection%20id%3D%22bf-container%22%20class%3D%22section%22%3E%24%7Bcontent%7D%3C%2Fsection%3E%60%0A%20%20setInnerHTML(results_table_container%2C%20html)%3B%0A%7D%3B%0A%0A%0Aconst%20loadBulmaCss%20%3D%20function()%20%7B%0A%20%20const%20bulma%20%3D%20document.createElement('link')%3B%0A%20%20bulma.setAttribute('rel'%2C%20'stylesheet')%3B%0A%20%20bulma.setAttribute('href'%2C%20'https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Fbulma%400.9.4%2Fcss%2Fbulma.min.css')%3B%0A%20%20document.head.appendChild(bulma)%3B%0A%7D%3B%0A%0A%0Aconst%20loadChartJs%20%3D%20function()%20%7B%0A%20%20fetch('https%3A%2F%2Fcdnjs.cloudflare.com%2Fajax%2Flibs%2FChart.js%2F3.9.1%2Fchart.min.js')%0A%20%20.then((response)%20%3D%3E%20response.text())%0A%20%20.then((text)%20%3D%3E%20%7B%0A%20%20%20%20const%20script%20%3D%20document.createElement('script')%3B%0A%20%20%20%20script.text%20%3D%20escapeScript(text)%3B%0A%20%20%20%20document.head.appendChild(script)%3B%0A%20%20%20%20isChartJsLoaded%20%3D%20true%3B%0A%20%20%7D)%3B%0A%7D%3B%0A%0A%0Aconst%20loadGoogleChart%20%3D%20function()%20%7B%0A%20%20fetch('https%3A%2F%2Fwww.gstatic.com%2Fcharts%2Floader.js')%0A%20%20.then((response)%20%3D%3E%20response.text())%0A%20%20.then((text)%20%3D%3E%20%7B%0A%20%20%20%20const%20script%20%3D%20document.createElement('script')%3B%0A%20%20%20%20script.text%20%3D%20escapeScript(text)%3B%0A%20%20%20%20document.head.appendChild(script)%3B%0A%20%20%20%20google.charts.load('current'%2C%20%7Bpackages%3A%20%5B'sankey'%5D%7D)%3B%0A%20%20%20%20google.charts.setOnLoadCallback(function()%20%7B%20isGoogleChartsLoaded%20%3D%20true%3B%20%7D)%3B%0A%20%20%7D)%3B%0A%7D%3B%0A%0A%0Aconst%20loadFunnelGraphJs%20%3D%20function()%20%7B%0A%20%20const%20css%20%3D%20document.createElement('link')%3B%0A%20%20css.setAttribute('rel'%2C%20'stylesheet')%3B%0A%20%20css.setAttribute('href'%2C%20'https%3A%2F%2Funpkg.com%2Ffunnel-graph-js%401.3.9%2Fdist%2Fcss%2Fmain.min.css')%3B%0A%20%20document.head.appendChild(css)%3B%0A%0A%20%20const%20css2%20%3D%20document.createElement('link')%3B%0A%20%20css2.setAttribute('rel'%2C%20'stylesheet')%3B%0A%20%20css2.setAttribute('href'%2C%20'https%3A%2F%2Funpkg.com%2Ffunnel-graph-js%401.3.9%2Fdist%2Fcss%2Ftheme.min.css')%3B%0A%20%20document.head.appendChild(css2)%3B%0A%0A%20%20fetch('https%3A%2F%2Funpkg.com%2Ffunnel-graph-js%401.3.9%2Fdist%2Fjs%2Ffunnel-graph.min.js')%0A%20%20.then((response)%20%3D%3E%20response.text())%0A%20%20.then((text)%20%3D%3E%20%7B%0A%20%20%20%20const%20regex%20%3D%20%2FinnerHTML%3D(%5Cw%2B)%2Fgi%3B%0A%20%20%20%20text%20%3D%20text.replace(regex%2C%20'innerHTML%3Dwindow.escapeHTML(%241)')%3B%0A%20%20%20%20console.log(text)%3B%0A%20%20%20%20const%20script%20%3D%20document.createElement('script')%3B%0A%20%20%20%20script.text%20%3D%20escapeScript(text)%3B%0A%20%20%20%20document.head.appendChild(script)%3B%0A%20%20%20%20isFunnelGraphJsLoaded%20%3D%20true%3B%0A%20%20%7D)%3B%0A%0A%0A%7D%0A%0AloadBulmaCss()%3B%0AloadFunnelGraphJs()%3B%0AloadChartJs()%3B%0AloadGoogleChart()%3B%0AsetInterval(run%2C%20100)%3B%7D)()%3B">bigfunctions</a> *(it has to be done only once)*
    2. Open BigQuery console
    3. Click on the installed bookmarklet.
        - From now on, the bookmarklet code will observe the BigQuery console page.
        - If a BigQuery result appears with a unique cell containing html content, it will be rendered.
    4. You will have to click on the bookmarklet *again*:
        - If you refresh the Bigquery console page,
        - If you open the BigQuery console in a new tab of your browser.
    5. Run the query of the example and open the result of the latest subquery. The result will be shown as a nice html content.

    <br>

    ![bookmarklet usage](../assets/bookmarklet_usage.gif)

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

{% if datasets|length > 1 %}

{% for dataset in datasets[:nb_datasets] %}


=== "{% if dataset|length <=2 %}{{ dataset | upper | replace('_', '-') }}{% else %}{{ dataset | replace('_', '-') }}{% endif %}"

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
    {% if type == 'procedure' %}call{% elif type == 'table_function' %}select * from{% else %}select{% endif %} {{ project }}.{{ dataset }}.{{ name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}',  project + '.' + dataset ) | replace('\n', '\n      ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if type == 'procedure' %};{% elif 'output' in bigfunction and type != 'table_function' %} as {{ output.name }}{% endif %}
    {%- if (example.with_clause is defined or example.temp_table is defined) and type != 'table_function' %}
    from sample_data
    {% endif %}
    {% if type == 'procedure' and template %}select html from bigfunction_result;{% endif %}
    {%- if type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}
    ```

{% endfor %}


{% else %}

{% for dataset in datasets %}

```sql
{% if example.with_clause is defined %}
with sample_data as (
  {{ example.with_clause | indent(2) }}
)
{% endif %}
{% if example.temp_table is defined %}
create temp table sample_data as (
  {{ example.temp_table | indent(2) }}
);
{% endif %}
{% if type == 'procedure' %}call{% elif type == 'table_function' %}select * from{% else %}select{% endif %} {{ project }}.{{ dataset }}.{{ name }}({% for argument in example.arguments %}{{ argument | replace('{BIGFUNCTIONS_DATASET}',  project + '.' + dataset ) | replace('\n', '\n  ') }}{% if not loop.last %}, {% endif %}{% endfor %}){% if type == 'procedure' %};{% elif 'output' in bigfunction and type != 'table_function' %} as {{ output.name }}{% endif %}
{%- if (example.with_clause is defined or example.temp_table is defined) and type != 'table_function' %}
from sample_data
{% endif %}
{% if type == 'procedure' and template %}select html from bigfunction_result;{% endif %}
{%- if type == 'procedure' and example.output %}select * from bigfunction_result;{% endif %}

```

{% endfor %}

{% endif %}


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


{% if project == 'bigfunctions' %}

??? question "Need help using `{{ name }}`?"

    The community can help! Engage the conversation on [Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q)

    **For professional suppport, don't hesitate to [chat with us](../chat_with_us.md)**.


??? warning "Found a bug using `{{ name }}`?"

    If the function does not work as expected, please

    - [report a bug](https://github.com/unytics/bigfunctions/issues/new/choose) so that it can be improved.
    - or open the discussion with the community on [Slack](https://join.slack.com/t/unytics/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q).

    **For professional suppport, don't hesitate to [chat with us](../chat_with_us.md)**.


{% endif %}


{% if use_case is defined and use_case %}

## Use cases

{{ use_case }}
{% endif %}


{% if project == 'bigfunctions' %}

## Spread the word

BigFunctions is fully open-source. Help make it a success by spreading the word!

[Share on :fontawesome-brands-linkedin: :octicons-arrow-right-24:](https://www.linkedin.com/sharing/share-offsite/?url=https://unytics.io/bigfunctions/bigfunctions/{{ name }}){ .md-button target="_blank" }
[Add a :octicons-star-fill-16: on :simple-github: :octicons-arrow-right-24:](https://github.com/unytics/bigfunctions){ .md-button .md-button--primary target="_blank" }

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
    return;
  }
  if (!authorizedUsers) {
    return;
  }
  const plainObj = {
    secret: plainText,
    authorized_users: authorizedUsers,
    function: "{{ name }}",
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
