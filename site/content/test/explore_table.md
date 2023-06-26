---
template: layouts/function.html
title: "Explore Table"
ogtitle: "BigFunctions supercharge BigQuery"
description: "BigFunctions are open-source BigQuery routines that give you SQL-superpowers. BigFunctions can show data-visualizations inside BigQuery console, compute advanced transforms such as sentiment score of a text, or send data to any of your favorite SAAS tool. BigFunctions is dbt's best friend."
image: "https://unytics.io/bigfunctions/assets/logo_and_name.png"
image_alt: "Supercharge BigQuery with BigFunctions"
image_width: "2500"
image_height: "541"
hide:
  - navigation
  - toc
---

# Explore Table

Show table infos and column statistics

---


<form id="function-form" action="javascript:void(0);">


<div class="bu-field bu-is-horizontal">
    <div class="bu-field-label bu-is-normal">
        <label class="bu-label">Fully Qualified Table</label>
    </div>
    <div class="bu-field-body">
    <div class="bu-field">
        <div class="bu-control">
            <input class="bu-input" type="text" name="fully_qualified_table" value="" placeholder="project.dataset.table">
        </div>
    </div>
    </div>
</div>

<div class="bu-field bu-is-horizontal">
  <div class="bu-field-label">
    <!-- Left empty for spacing -->
  </div>
  <div class="bu-field-body">
    <div class="bu-field">
      <div class="bu-control">
        <button onclick="executeQuery();" class="bu-button bu-is-primary bu-is-small">
          Run
        </button>
        <div id="bigfunction-progress" class="bu-is-hidden">
            <p>
                <progress class="bu-progress bu-is-primary" max="100">60%</progress>
            </p>
            <p id="bigfunction-progress-message" class="bu-is-family-code"></p>
        </div>
      </div>
    </div>
  </div>
</div>


</form>

<div id="result_container">

<h2>Result</h2>
<hr>
<div id="result"></div>


</div>










