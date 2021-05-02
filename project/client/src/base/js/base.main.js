
import $ from "jquery";

console.log('base.main.js');

/*============================================================================================================== */
/*=========================================== menu functionality start ========================================= */
/*============================================================================================================== */

var menu_btn = $('#menu .collapsible');

function toggle_menu() {
    menu.classList.toggle("active");
}

function set_menu_active(flag) {
    if (flag) {
        menu.classList.add("active");
    } else {
        menu.classList.remove("active");
    }
}

menu_btn.on('click', function (e) {
    toggle_menu();
});

$(window).on('click', function (e) {
    // is element other then the menu and what inside is clicked?
    if (e.target != menu_btn && menu_btn[0].contains(e.target) == false) {
        //Hide the menus if visible
        set_menu_active(false);
    } else {
    }
});

/*============================================================================================================== */
/*=========================================== menu functionality end =========================================== */
/*============================================================================================================== */