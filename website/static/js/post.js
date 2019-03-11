function showOptions() {
    var selectDiv = document.getElementById("selectDiv");
    var options = document.getElementById("options");
    selectDiv.setAttribute("style", "display: none");
    options.setAttribute("style", "display: flex")
}
function hideOptions() {
    var selectDiv = document.getElementById("selectDiv");
    var options = document.getElementById("options");
    selectDiv.setAttribute("style", "display: inline-block");
    options.setAttribute("style", "display: none")
}