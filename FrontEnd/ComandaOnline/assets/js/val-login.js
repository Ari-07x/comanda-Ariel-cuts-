const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	password: /^(?=(?:.*\d){2})(?=(?:.*[A-Z]){1})(?=(?:.*[a-z]){1})\S{8}$/, //solo 8 Caracteres, Mayusculas, Minusculas, Numeros sin espacios en blanco sin repetir el mismo caracter mas de 4 veces.


}

const campos = {
	correo: false,
	password: false
}

const validarFormulario = (e) => {
	switch (e.target.name) {
	
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "password":
			validarCampo(expresiones.password, e.target, 'password');
			validarPassword2();
		break;
		
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} .ic`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} .ic`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} .ic`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} .ic`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}


inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	e.preventDefault();

	const terminos = document.getElementById('terminos');
	if(campos.correo && campos.password ){
		formulario.reset();
	
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
		document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
			icono.classList.remove('formulario__grupo-correcto');
		});
	} else {
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
});
function mostrar(){
	var tipo = document.getElementById('password');
	var icon = document.getElementById('ov');
	if(tipo.type =='password'){
		document.getElementById('password').setAttribute('type', 'text');
		icon.classList.toggle('fa-eye-slash');
		
	}
	else{
		document.getElementById('password').setAttribute('type', 'password');
		icon.classList.remove('fa-eye-slash');
	
	}
	
  }
