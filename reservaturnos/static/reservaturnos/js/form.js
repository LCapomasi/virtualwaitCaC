const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    edad: /^\d{1,3}$/, // 1 a 3 numeros.
    dni: /^\d{7,8}$/, // 7 a 8 numeros.
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,

}

const campos = {

    nombre: false,
    apellido: false,
    edad: false,
    dni: false,
    email: false,

}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;

        case "apellido":
            validarCampo(expresiones.apellido, e.target, 'apellido');
            break;

        case "edad":
            validarCampo(expresiones.edad, e.target, 'edad');
            break;

        case "dni":
            validarCampo(expresiones.dni, e.target, 'dni');
            break;

        case "email":
            validarCampo(expresiones.email, e.target, 'email');
            break;

    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} .formulario__input`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} .formulario__input`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

/*formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    // debugger
    const terminos = document.getElementById('terminos');

    if (campos.nombre && campos.apellido && campos.edad && campos.dni && campos.email && terminos.checked) {
        formulario.reset(); 
        campos['nombre']=false;
        campos['apellido']=false;
        campos['edad']=false;
        campos['dni']=false;
        campos['email']=false;

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 10000);

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});*/
