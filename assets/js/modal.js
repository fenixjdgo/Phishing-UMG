/**
* Este archivo contiene la funcionalidad que hace funcionar el modal
*/

$('#disclamer').modal('show');

// Boton aceptar
const acceptIt = document.querySelector('#accept_it');

acceptIt.onclick = () => {
    $('#disclamer').modal('hide');
}