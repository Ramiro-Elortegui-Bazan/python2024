// hace que no se ejecute hasta que el DOM este cargado 
document.addEventListener('DOMContentLoaded', function() {
//selecciona los elementos de busqueda por su id 
    const inputBusqueda = document.getElementById('search-input'); 
    const botonesVet = document.querySelectorAll('button[data-localidad]'); //Selecciona todos los botones que tengan el atributo data-localidad y los almacena en la variable botonesVet. 

    inputBusqueda.addEventListener('input', function() {
        filtroVetLocalidad();//usuario escriba algo (evento input), se llama a la función filtroVetLocalidad, para filtarar

    });

    function filtroVetLocalidad() { //lo convierte a minúsculas
        const texto = inputBusqueda.value.toLowerCase();
        botonesVet.forEach(boton => {
            const localidad = boton.getAttribute('data-localidad').toLowerCase();//minuscula 

            // si aparece en el buscador es visible y si no no xd
            if (localidad.includes(texto)) {
                boton.style.display = '';
            } else {
                boton.style.display = 'none';
            }
        });
    }
});
