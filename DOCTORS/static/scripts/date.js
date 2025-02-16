document.addEventListener("DOMContentLoaded", function() {
    const startInput = document.getElementById("id_start_incapacity");
    const endInput = document.getElementById("id_end_incapacity");
    const totalDaysInput = document.getElementById("id_total_days");

    function validateDates() {
        if(startInput.value && endInput.value){
            const startDate = new Date(startInput.value);
            const endDate = new Date(endInput.value);
            // Verificar si las fechas son correctas
            if (startDate > endDate) {
                alert("La fecha de inicio no puede ser posterior a la fecha de fin.");
                endInput.value = '';
                return;
            }
            if (endDate < startDate) {
                alert("La fecha de fin no puede ser anterior a la fecha de inicio.");
                endInput.value = '';
                return;
            }
            // Calcular los días entre las fechas
            const diffTime = endDate - startDate;
            const totalDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1; // Sumar 1 para incluir ambos días
            totalDaysInput.value = totalDays;
        }
    }

    // Agregar eventos de cambio de fecha
    startInput.addEventListener("change", validateDates);
    endInput.addEventListener("change", validateDates);
});
