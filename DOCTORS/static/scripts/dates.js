document.addEventListener("DOMContentLoaded", function() {
    // Obtener los campos de fecha
    const dateOfRecordFields = document.querySelectorAll('[name="date_of_record"]');

    // Función para establecer la fecha actual
    function setCurrentDate() {
        const today = new Date();
        const day = String(today.getDate()).padStart(2, '0');  // Día con 2 dígitos
        const month = String(today.getMonth() + 1).padStart(2, '0'); // Mes con 2 dígitos
        const year = today.getFullYear();

        // Crear la fecha en formato dd-mm-yyyy (o el formato que prefieras)
        const formattedDate = `${day}-${month}-${year}`;

        // Asignar la fecha a todos los campos
        dateOfRecordFields.forEach(function(field) {
            field.value = formattedDate;
        });
    }

    // Ejecutar la función al cargar la página
    setCurrentDate();
    console.log("Fechas cargadas");
});
