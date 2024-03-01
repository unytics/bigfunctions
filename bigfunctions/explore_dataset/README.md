---
title: "explore_dataset"
description: "BigFunction explore_dataset: Show infos about dataset tables"
---

<span>style="color: gray; position: relative; top: -1rem"><a href="..">BigFunctions </a> / explore_dataset</span>

# explore_dataset


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/paul-marcombes" title="Author: Paul Marcombes" target="_blank">
    <img src="https://lh3.googleusercontent.com/a-/ACB-R5RDf2yxcw1p_IYLCKmiUIScreatDdhG8B83om6Ohw=s260" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="explore_dataset.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
explore_dataset(fully_qualified_dataset)
```

**Description**

Show infos about dataset tables




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

    ![bookmarklet usage](/bigfunctions/site/assets/bookmarklet_usage.gif)




**Examples**













=== "EU"

    ```sql
    call bigfunctions.eu.explore_dataset("eu");
    select html from bigfunction_result;
    ```




=== "US"

    ```sql
    call bigfunctions.us.explore_dataset("us");
    select html from bigfunction_result;
    ```




=== "europe-west1"

    ```sql
    call bigfunctions.europe_west1.explore_dataset("europe_west1");
    select html from bigfunction_result;
    ```












<a href="explore_dataset.png"><img alt="screenshot" src="explore_dataset.png" style="border: var(--md-code-bg-color) solid 1rem; margin-top: -1rem; width: 100%"></a>


