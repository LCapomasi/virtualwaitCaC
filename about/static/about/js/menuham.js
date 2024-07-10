document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const menu = document.querySelector('.menu-de-opciones');
    const menuItems = document.querySelectorAll('.menu-de-opciones a');

    // Función para abrir y cerrar el menú
    function toggleMenu() {
        menu.classList.toggle('active');
    }
    // Evento de clic en el botón del menú
    hamburgerMenu.addEventListener('click', toggleMenu);

    // Evento de clic en cada enlace del menú
    menuItems.forEach(item => {
        item.addEventListener('click', function () {
            toggleMenu(); // Cerrar el menú al hacer clic en un enlace
        });
    });
});
