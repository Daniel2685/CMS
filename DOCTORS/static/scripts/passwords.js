document.addEventListener('DOMContentLoaded', function () {
    const passwordField = document.querySelector('.password-field[name="password"]');
    const password2Field = document.querySelector('.password-field[name="password2"]');
    const form = document.querySelector('form');  // Selecciona el formulario

    form.addEventListener('submit', function (e) {
        if (passwordField.value !== password2Field.value) {
            e.preventDefault();  // Evita el envío del formulario
            alert('Las contraseñas no coinciden.');
            passwordField.value = '';
            password2Field.value = '';
        }
    });
});