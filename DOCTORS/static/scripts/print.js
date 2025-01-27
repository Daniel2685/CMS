document.querySelectorAll('#print-button').forEach(button => {
    button.addEventListener('click', function () {
        // Obtener el contenedor del formulario
        const formContainer = this.closest('.tab-content');
        
        // Guardar el contenido actual del formulario
        const contentToPrint = formContainer.innerHTML;

        // Crear un contenedor temporal para el contenido de impresión
        const printWindow = window.open('', '_self'); // Abrir en la misma ventana

        // Escribir el contenido a imprimir directamente en el documento de la página
        printWindow.document.write(`
            <html>
            <head>
                <title>Imprimir Formulario</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                    }
                    /* Asegúrate de ajustar los estilos según sea necesario */
                    img { max-width: 100%; }
                </style>
            </head>
            <body>
                ${contentToPrint}
            </body>
            </html>
        `);

        // Cerrar el documento y comenzar la impresión directamente
        printWindow.document.close();
        printWindow.print();
    });
});
