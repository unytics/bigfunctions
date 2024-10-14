let isChartJsLoaded = false;
let isGoogleChartsLoaded = false;
let isFunnelGraphJsLoaded = false;


window.escapeHTML = function(html) {
  if(!trustedTypes) {
    return html;
  }
  const policy = trustedTypes.createPolicy("forceInner", {createHTML: (to_escape) => to_escape});
  return policy.createHTML(html);
};


const escapeScript = function(script) {
  if(!trustedTypes) {
    return script;
  }
  const policy = trustedTypes.createPolicy("forceInner", {createScript: (to_escape) => to_escape});
  return policy.createScript(script);
};


const setInnerHTML = function(elm, html) {
  elm.innerHTML = window.escapeHTML(html);
  Array.from(elm.querySelectorAll('script')).forEach( oldScript => {
      const newScript = document.createElement('script');
      Array.from(oldScript.attributes).forEach( attr => newScript.setAttribute(attr.name, attr.value) );
      newScript.text = escapeScript(oldScript.innerHTML);
      oldScript.parentNode.replaceChild(newScript, oldScript);
  });
};


const run = async function() {
  if (!isChartJsLoaded || !isGoogleChartsLoaded || !isFunnelGraphJsLoaded) {
    return;
  }
  const results_table_container = document.querySelector('bq-tab-content:not(.cfc-hidden) bq-results-table');
  if (!results_table_container) {
    return;
  }
  const cells = results_table_container.querySelectorAll('td div:not(.cfc-flex-container)');
  if (cells.length !== 1) {
    return;
  }
  const cell = cells[0];
  const content = cell.innerText;
  if (!content.startsWith("<html")) {
    return;
  }
  if (content.endsWith("...")) {
    cell.nextElementSibling.firstElementChild.click();
    return;
  }
  const html = `<section id="bf-container" class="section">${content}</section>`
  setInnerHTML(results_table_container, html);
};


const loadBulmaCss = function() {
  const bulma = document.createElement('link');
  bulma.setAttribute('rel', 'stylesheet');
  bulma.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css');
  document.head.appendChild(bulma);
};


const loadChartJs = function() {
  fetch('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js')
  .then((response) => response.text())
  .then((text) => {
    const script = document.createElement('script');
    script.text = escapeScript(text);
    document.head.appendChild(script);
    isChartJsLoaded = true;
  });
};


const loadGoogleChart = function() {
  fetch('https://www.gstatic.com/charts/loader.js')
  .then((response) => response.text())
  .then((text) => {
    const script = document.createElement('script');
    script.text = escapeScript(text);
    document.head.appendChild(script);
    google.charts.load('current', {packages: ['sankey']});
    google.charts.setOnLoadCallback(function() { isGoogleChartsLoaded = true; });
  });
};


const loadFunnelGraphJs = function() {
  const css = document.createElement('link');
  css.setAttribute('rel', 'stylesheet');
  css.setAttribute('href', 'https://unpkg.com/funnel-graph-js@1.3.9/dist/css/main.min.css');
  document.head.appendChild(css);

  const css2 = document.createElement('link');
  css2.setAttribute('rel', 'stylesheet');
  css2.setAttribute('href', 'https://unpkg.com/funnel-graph-js@1.3.9/dist/css/theme.min.css');
  document.head.appendChild(css2);

  fetch('https://unpkg.com/funnel-graph-js@1.3.9/dist/js/funnel-graph.min.js')
  .then((response) => response.text())
  .then((text) => {
    const regex = /innerHTML=(\w+)/gi;
    text = text.replace(regex, 'innerHTML=window.escapeHTML($1)');
    const script = document.createElement('script');
    script.text = escapeScript(text);
    document.head.appendChild(script);
    isFunnelGraphJsLoaded = true;
  });


}

loadBulmaCss();
loadFunnelGraphJs();
loadChartJs();
loadGoogleChart();
setInterval(run, 100);
