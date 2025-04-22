import { form } from "../elements.js";
import { formData, loadAlert } from "../helpers/helpers.js";
import { expressionReg } from "../helpers/expression.js";
import { http } from "../helpers/http.js";

const validForm = () => {
    const { email, password } = formData( new FormData( form ) );

    if( !expressionReg.email.test(email) ) return [ "formato de email incorrecto" ]

    if( !expressionReg.password.test( password ) ) return [ "La contraseña debe contener mas de 8 caracteres" ]

    return [ undefined, { email, password } ]
}


const handleSubmit = async( event ) => {
    event.preventDefault();
    
    const [ error, data ] = validForm();

    if( error ) return loadAlert( error, "alert-danger" );

    const { code, status, msg } = await http( "/login", data );

    console.log( msg)
    
    code === 200 && form.reset();

    return loadAlert( msg, code !== 200 ? "alert-danger": "alert-success" );

}


form.addEventListener( 'submit', handleSubmit );

