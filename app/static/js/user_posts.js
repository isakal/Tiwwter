$(document).ready(function () {
    $("#showEdit").click(function () {
        $("#theform").slideDown("slow");
        $("#showEdit").css('display', 'none');
    });
    $("#cancel").click(function () {
        $("#theform").slideUp("slow");
        $("#showEdit").css('display', 'inline-block');
    });
});
