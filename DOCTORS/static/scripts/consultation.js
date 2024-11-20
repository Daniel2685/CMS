// Función para mostrar el contenido del panel seleccionado
function showContent(panelId) {
    // Obtiene todos los elementos con la clase 'tab-content'
    var panels = document.getElementsByClassName('tab-content');

    // Oculta todos los paneles
    for (var i = 0; i < panels.length; i++) {
        panels[i].classList.remove('active');
    }

    // Muestra el panel seleccionado
    document.getElementById(panelId).classList.add('active');
}

// Ejecuta al cargar la página
window.onload = function() {
    // Mostrar el panel 1 inicialmente
    showContent('panel1');
}