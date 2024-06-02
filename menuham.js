document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const menu = document.querySelector('.menu-de-opciones');

    hamburgerMenu.addEventListener('click', function () {
        menu.classList.toggle('active');
    });
});
