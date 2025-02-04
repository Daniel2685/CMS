document.querySelectorAll('.print-button').forEach(button => {
    button.addEventListener('click', function () {
        var form = this.closest("form"); // Encuentra el formulario más cercano
        var printWindow = window.open('', '', 'width=1000,height=800');
        printWindow.document.write(`
            <html>
            <head>
                <title>Impresión</title>
                <style>
                    /* Estilos para la ventana de impresión */
                    @media print {
                        @page {
                            margin: 0; /* Eliminar márgenes para la impresión */
                        }
                        body {
                            font-family: "Noto Serif", serif;
                            margin: 0;
                            padding: 20px;
                        }
                        .header {
                            display: flex;
                            flex-direction: row;
                            align-items: center;

                            margin-bottom: 20px;
                            border-bottom: 2px solid #ccc;
                            padding-bottom: 10px;
                        }
                        .header img {
                            height: 200px;
                            width: auto;
                        }
                        .header-data{
                            text-align:center;
                            flex-grow:1;
                        }
                        form {
                            padding: 20px;
                            border: 1px solid #ccc;
                            border-radius: 8px;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            max-width: 800px;
                            margin: auto;
                        }
                        label {
                            display: block;
                            margin: 10px 0 5px;
                            font-weight: bold;
                        }
                        input[type="text"], input[type="email"], input[type="number"], textarea {
                            width: 100%;
                            padding: 10px;
                            margin-bottom: 20px;
                            border: 1px solid #ccc;
                            border-radius: 4px;
                            font-size: 16px;
                        }
                        input[type="submit"] {
                            background-color: #4CAF50;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            border-radius: 4px;
                            cursor: pointer;
                            font-size: 16px;
                        }
                        input[type="submit"]:hover {
                            background-color: #45a049;
                        }
                        textarea {
                            height: 150px;
                        }
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <img src="/static/media/logo.png" alt="LOGO LOGO LOGO LOGO LOGO LOGO LOGO LOGO LOGO">
                    <div class="header-data">
                        <h1>Clínica Multidisciplinaria de Salud</h1>
                        <h2>Universidad Autónoma del Estado de México</h2>
                    </div>
                    <img src="/static/media/logo2.png" alt="Logo 2">
                </div>
                ${form.outerHTML} <!-- Inserta el formulario aquí -->
            </body>
            </html>
        `);
        printWindow.document.close();
        printWindow.focus();
        printWindow.print();
        printWindow.close();
    });
});
