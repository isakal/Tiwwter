// function showOptions() {
//     const updt = document.getElementById("updt");
//     const dlt = document.getElementById("dlt");
//     updt.classList.add("trueHeight");
//     dlt.classList.add("trueHeight");
// } 
// window.onclick = function (event) {
//     const updt = document.getElementById("updt");
//     const dlt = document.getElementById("dlt");
//     if(event.target.classList.contains("show")) {
//         if (updt.classList.contains('trueHeight') && dlt.classList.contains('trueHeight')) {
//             updt.classList.remove('trueHeight');
//             dlt.classList.remove('trueHeight');
//         }
//         else {
//             showOptions();
//         }
//     }
//     else {
//         updt.classList.remove('trueHeight');
//         dlt.classList.remove('trueHeight');
//     }
// }

$(document).ready(function () {
    $(".show").click(function () {
        if ($("#options").hasClass("slid")) {
            $("#options").slideUp("fast");
            $("#options").removeClass("slid");
        }
        else {
            $("#options").slideDown("fast");
            $("#options").addClass("slid");
        }
    });
});

$(document).click(function (event) {
    if (!event.target.classList.contains("show")) {
        $("#options").slideUp("fast");
        $("#options").removeClass("slid");
    }
});