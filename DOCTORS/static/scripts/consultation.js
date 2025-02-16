function autoResizeTextarea(textarea) {
    // Reseteamos la altura para obtener el scrollHeight correcto
    textarea.style.height = 'auto';
    // Ajustamos la altura al scrollHeight del contenido
    textarea.style.height = (textarea.scrollHeight) + 'px';
}

// Función para mostrar el contenido de un panel
function showContent(panelId) {
    // Obtiene todos los elementos con la clase 'tab-content'
    var panels = document.getElementsByClassName('tab-content');

    // Oculta todos los paneles
    for (var i = 0; i < panels.length; i++) {
        panels[i].classList.remove('active');
    }

    // Muestra el panel seleccionado
    var selectedPanel = document.getElementById(panelId);
    if (selectedPanel) {
        selectedPanel.classList.add('active');
    }

    // Si el panel activo es el panel 3 (Receta), copiamos el contenido de los paneles 1 y 2 al panel 3
    if (panelId === 'panel3') {
        // Obtener los contenidos de pharmacological_treatment de los paneles 1 y 2
        var panel1 = document.getElementById('panel1');
        var panel2 = document.getElementById('panel2');
        var panel3 = document.getElementById('panel3');
        
        var pharmaTreatment1 = panel1.querySelector('[name="pharmacological_treatment"]').value;
        var pharmaTreatment2 = panel2.querySelector('[name="pharmacological_treatment"]').value;

        var diagnoses1 = panel1.querySelector('[name="diagnoses"]').value;
        var diagnoses2 = panel2.querySelector('[name="diagnoses"]').value;

        
        // Obtener el campo de prescription del panel 3
        var prescriptionField = panel3.querySelector('[name="prescription"]');
        var diagnosesField = panel3.querySelector('[name=diagnoses]')
        
        // Concatenamos el contenido de ambos campos en el campo prescription
        if (prescriptionField) {
            prescriptionField.value = pharmaTreatment1 + "\n" + pharmaTreatment2; // Unimos ambos contenidos con un salto de línea
            // Llamamos a la función para ajustar la altura del textarea
            autoResizeTextarea(prescriptionField);
        }

        if(diagnosesField) {
            diagnosesField.value = diagnoses1 + "\n" + diagnoses2;
            autoResizeTextarea(diagnosesField)
        }
    }


    if (panelId === 'panel4') {
        // Obtener los contenidos de pharmacological_treatment de los paneles 1 y 2
        var panel1 = document.getElementById('panel1');
        var panel2 = document.getElementById('panel2');
        var panel4 = document.getElementById('panel4');
        
        var diagnoses1 = panel1.querySelector('[name="diagnoses"]').value;
        var diagnoses2 = panel2.querySelector('[name="diagnoses"]').value;

        var diagnosesField = panel4.querySelector('[name=diagnoses]')
        
        if(diagnosesField) {
            diagnosesField.value = diagnoses1 + "\n" + diagnoses2;
            autoResizeTextarea(diagnosesField)
        }
    }
}

// Ejecuta al cargar la página
window.onload = function() {
    // Mostrar el panel 1 inicialmente
    showContent('panel1');
};

