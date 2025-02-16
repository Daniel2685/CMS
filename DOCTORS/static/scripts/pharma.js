document.addEventListener('DOMContentLoaded', function() {
    // Seleccionamos todos los campos ChoiceField por su nombre (para opciones farmacológicas)
    const pharmaSelectList = document.querySelectorAll('[name="pharma_options"]');
    
    // Seleccionamos todos los campos pharmacological_treatment por su nombre
    const pharmaSelectedList = document.querySelectorAll('[name="pharmacological_treatment"]');

    // Verificamos que ambos grupos de campos existan
    if (pharmaSelectList.length > 0 && pharmaSelectedList.length > 0) {
        // Iteramos sobre todos los pharma_options
        pharmaSelectList.forEach(function(pharmaSelect, index) {
            // Para cada pharma_options, agregamos el evento de cambio (change)
            pharmaSelect.addEventListener('change', function() {
                const selectedOption = pharmaSelect.options[pharmaSelect.selectedIndex];
                
                // Obtenemos el campo pharmacological_treatment correspondiente para este pharma_options
                const pharmaSelected = pharmaSelectedList[index]; 

                // Actualizamos el campo pharmacological_treatment seleccionado con el texto correspondiente
                pharmaSelected.value += selectedOption.text + '    \n'; // Si es un textarea

                // Llamamos a la función para ajustar el número de filas
                adjustTextareaHeight(pharmaSelected);
            });
        });
    }

    // Función que ajusta la altura del textarea
    function adjustTextareaHeight(textarea) {
        // Establecemos temporalmente el height para medir el scroll
        textarea.style.height = 'auto'; // Reseteamos la altura
        textarea.style.height = `${textarea.scrollHeight}px`; // Ajustamos la altura a su contenido

        // Opcional: También puedes aumentar el número de filas (rows) si lo prefieres
        const rows = Math.floor(textarea.scrollHeight / 20); // 20px por cada fila (aproximadamente)
        textarea.setAttribute('rows', rows);
    }
});