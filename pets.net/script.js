document.addEventListener('DOMContentLoaded', function() {
    const inputBusqueda = document.getElementById('search-input'); // trae el texto del usuario
    const botonesVet = document.querySelectorAll('button[data-localidad]'); // selecciona los botones con atributo data-localidad

    inputBusqueda.addEventListener('input', function() {
        filtroVetLocalidad();
    });

    function filtroVetLocalidad() {
        const texto = inputBusqueda.value.toLowerCase();
        botonesVet.forEach(boton => {
            const localidad = boton.getAttribute('data-localidad').toLowerCase();
            if (localidad.includes(texto)) {
                boton.style.display = '';
            } else {
                boton.style.display = 'none';
            }
        });
    }
});
