let isChartJsLoaded = false;


const escapeHTML = function(html) {
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
  elm.innerHTML = escapeHTML(html);
  Array.from(elm.querySelectorAll('script')).forEach( oldScript => {
      const newScript = document.createElement('script');
      Array.from(oldScript.attributes).forEach( attr => newScript.setAttribute(attr.name, attr.value) );
      newScript.text = escapeScript(oldScript.innerHTML);
      oldScript.parentNode.replaceChild(newScript, oldScript);
  });
};


const run = async function() {
  if (!isChartJsLoaded) {
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
  const html = `<section class="section">${content}</section>`
  setInnerHTML(results_table_container, html);
};


const loadBulmaCss = function() {
  const bulma = document.createElement('link');
  bulma.setAttribute('rel', 'stylesheet');
  bulma.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css');
  document.head.appendChild(bulma);
};


const loadChartjs = function() {
  fetch('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js')
  .then((response) => response.text())
  .then((text) => {
    const script = document.createElement('script');
    script.text = escapeScript(text);
    document.head.appendChild(script);
    isChartJsLoaded = true;
  });
};




loadBulmaCss();
loadChartjs();
setInterval(run, 100);




