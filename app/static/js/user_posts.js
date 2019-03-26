$(document).ready(function () {
    $("#showEdit").click(function () {
        $("#theform").slideDown("slow");
    });
    $("#cancel").click(function () {
        $("#theform").slideUp("slow");
    });
});