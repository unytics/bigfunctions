function renderHTML() {
    document.querySelectorAll('.bq-results-table thead th:nth-child(2)').forEach(element => element.style = "width: 100%;");

    document.querySelectorAll('.bq-results-table td [sandboxuid]').forEach(div => {
        const html = div.innerText;
        document.querySelector('bq-results-table').innerHTML = html;
    });
}
renderHTML();


setInterval(renderHTML,1000);
