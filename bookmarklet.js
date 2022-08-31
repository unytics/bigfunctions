fetch('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js').then((response) => response.text()).then((text) => {const script = document.createElement('script'); script.text = text; document.head.appendChild(script);});

const bulma = document.createElement('link'); bulma.setAttribute('rel', 'stylesheet'); bulma.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css'); document.head.appendChild(bulma);


const setInnerHTML = function(elm, html) {
  elm.innerHTML = html;
  Array.from(elm.querySelectorAll("script")).forEach( oldScript => {
    const newScript = document.createElement("script");
    Array.from(oldScript.attributes)
      .forEach( attr => newScript.setAttribute(attr.name, attr.value) );
    newScript.appendChild(document.createTextNode(oldScript.innerHTML));
    oldScript.parentNode.replaceChild(newScript, oldScript);
  });
};

const renderHTML = function() {
    const bq_results_table = document.querySelector('.bq-results-table');
    if (!bq_results_table) { return; }

    const cells_div = bq_results_table.querySelectorAll('td div');
    if (cells_div.length > 1) { return; }

    const html = cells_div[0].innerText;

    document.querySelector('.bq-results-table thead th:nth-child(2)').style = "width: 100%;";
    setInnerHTML(bq_results_table, html);
    console.log('bigfunctions: successfully replaced table content');
};


setInterval(renderHTML, 1000);
