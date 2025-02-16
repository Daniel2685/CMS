// diagnoses.js

// Esperamos a que el DOM se cargue completamente antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    // Seleccionamos todos los campos ChoiceField por su nombre
    const diagnosisSelectList = document.querySelectorAll('[name="diagnoses_options"]');
    
    // Seleccionamos todos los campos diagnosis por su nombre
    const diagnosisSelectedList = document.querySelectorAll('[name="diagnoses"]');

    // Verificamos que ambos grupos de campos existan
    if (diagnosisSelectList.length > 0 && diagnosisSelectedList.length > 0) {
        // Iteramos sobre todos los diagnosis_options
        diagnosisSelectList.forEach(function(diagnosisSelect, index) {
            // Para cada diagnosis_options, agregamos el evento de cambio (change)
            diagnosisSelect.addEventListener('change', function() {
                const selectedOption = diagnosisSelect.options[diagnosisSelect.selectedIndex];
                
                // Obtenemos el campo diagnosis correspondiente para este diagnosis_options
                const diagnosisSelected = diagnosisSelectedList[index]; 

                // Actualizamos el campo diagnosis seleccionado con el texto correspondiente
                diagnosisSelected.value += selectedOption.text + '    \n'; // Si es un textarea

                // Llamamos a la función para ajustar el número de filas
                adjustTextareaHeight(diagnosisSelected);
            });
        });
    }

    // Función que ajusta la altura del textarea
    function adjustTextareaHeight(textarea) {
        // Establecemos temporalmente el height para medir el scroll
        textarea.style.height = 'auto'; // Reseteamos la altura
        textarea.style.height = `${textarea.scrollHeight}px`;  // Ajustamos la altura a su contenido

        // Opcional: También puedes aumentar el número de filas (rows) si lo prefieres
        const rows = Math.floor(textarea.scrollHeight / 20); // 20px por cada fila (aproximadamente)
        textarea.setAttribute('rows', rows);
    }
});