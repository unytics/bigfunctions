function renderHTML() {
    document.querySelectorAll('td [sandboxuid]').forEach(div => {
        const td = div.parentNode;
        const new_td = document.createElement("div");
        new_td.innerHTML = "foo";
        td.replaceChild(new_td, div);
        console.log('fired');
    });
}
setInterval(renderHTML,1000);
