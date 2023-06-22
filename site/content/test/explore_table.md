---
template: main.html
title: "Test"
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
        <p>
            <progress id="bigfunction-progress" class="bu-progress bu-is-primary bu-is-hidden" max="100">60%</progress>
        </p>
      </div>
    </div>
  </div>
</div>


</form>



<script src="https://apis.google.com/js/api.js"></script>
<script src="https://accounts.google.com/gsi/client"></script>


<script>
    // https://developers.google.com/drive/api/quickstart/js
    // https://developers.google.com/identity/oauth2/web/guides/use-token-model
    // https://developers.google.com/identity/gsi/web/tools/configurator

    gapi.load('client');

    function authenticate() {
        const tokenClient = google.accounts.oauth2.initTokenClient({
            client_id: '749389685934-us0f5irn6vqkp2lq7vgjs6g8ek45f5ei.apps.googleusercontent.com',
            scope: 'https://www.googleapis.com/auth/bigquery',
            callback: (tokenResponse) => {
                if (tokenResponse && tokenResponse.access_token) {
                    gapi.client.load('bigquery', 'v2', executeQuery);
                }
            },
        });
        tokenClient.requestAccessToken();
    }

    function alert(errorMessage) {
        const alert = document.createElement('div');
        alert.innerHTML = `
            <div class="bu-modal bu-is-active">
                <div class="bu-modal-background"></div>
                <div class="bu-modal-card">
                    <header class="bu-modal-card-head bu-has-background-danger">
                        <p class="bu-modal-card-title bu-is-normal bu-has-text-white bu-is-size-5">ERROR!</p>
                        <button class="bu-delete" aria-label="close"></button>
                    </header>
                    <section class="bu-modal-card-body">
                        <p class="bu-is-size-7">${errorMessage}</p>
                    </section>
                </div>
            </div>
        `;
        document.body.appendChild(alert);
        const modals = document.getElementsByClassName("bu-modal");
        document.querySelectorAll('.bu-modal-background, .bu-modal-close, .bu-modal-card-head .bu-delete, .bu-modal-card-foot .bu-button').forEach((elem) => {
            elem.addEventListener('click', () => {
                for (const modal of modals) {
                    modal.classList.remove('bu-is-active');
                }
            });
        });
    }

    function toggleProgressBar() {
        document.getElementById('bigfunction-progress').classList.toggle('bu-is-hidden');
    }

    let DATASETS;

    function getDatasets() {
        let request = gapi.client.bigquery.datasets.list({
            'projectId': project,
            'maxResults': 10000,
        });
        request.execute(response => {
            console.log(response);
            if (response.error) {
                return alert(response.error.message);
            }
            DATASETS = response.datasets;
            executeQuery();
        });
    }

    function executeQuery() {

        const form = document.getElementById("function-form");
        const formData = new FormData(form);
        const fully_qualified_table = formData.get('fully_qualified_table');
        const fully_qualified_table_parts = fully_qualified_table.split(".");
        if (fully_qualified_table_parts.length !== 3) {
            return alert('Fully Qualified Table param has wrong pattern.<br>➜ It should be like `project.dataset.table`');
        }
        project = fully_qualified_table_parts[0];
        dataset = fully_qualified_table_parts[1];

        if (gapi.client.getToken() === null) {
            return authenticate();
        }

        if (!DATASETS) {
            return getDatasets();
        }

        let datasetLocation;
        for (const _dataset of DATASETS) {
            if (_dataset.datasetReference.datasetId === dataset) {
                datasetLocation = _dataset.location;
            }
        }
        if (!datasetLocation) {
            return alert(`Could not find dataset ${dataset} in project ${project}`);
        }
        console.log('datasetLocation:', datasetLocation);
        const bigfunction_dataset = datasetLocation.replaceAll('-', '_').toLowerCase();
        console.log('bigfunction_dataset:', bigfunction_dataset);

        const query = `
        call bigfunctions.${bigfunction_dataset}.explore_table('${fully_qualified_table.replaceAll("'", "")}');
        select * from bigfunction_result
        `
        console.log('query:', query);


        let request = gapi.client.bigquery.jobs.query({
            'query': query,
            'timeoutMs': 600000,
            'projectId': project,
            'useLegacySql': false
        });
        toggleProgressBar();
        request.execute(response => {
            console.log(response);
            toggleProgressBar();
            if (response.error) {
                return alert(response.error.message);
            }
        });

        // gapi.client.bigquery.datasets.list({
        //     'projectId': "compte-nickel-dataprod"
        // }).execute(response => {
        //     console.log(response)
        // });
    }


</script>