function showOptions() {
    const updt = document.getElementById("updt");
    const dlt = document.getElementById("dlt");
    updt.classList.add("trueHeight");
    dlt.classList.add("trueHeight");
} 
window.onclick = function (event) {
    const updt = document.getElementById("updt");
    const dlt = document.getElementById("dlt");
    if(!event.target.classList.contains("show")) {
        if(updt.classList.contains('trueHeight')) {
            updt.classList.remove('trueHeight');
        }
        if(dlt.classList.contains('trueHeight')) {
            dlt.classList.remove('trueHeight');
        }
    }
}