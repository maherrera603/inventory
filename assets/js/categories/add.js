import { form } from "../elements.js";
import { formData, loadAlert } from "../helpers/helpers.js";
import { expressionReg } from "../helpers/expression.js";
import { http } from "../helpers/http.js";


const validateForm = () => {
    const { category, status, id = undefined } = formData( new FormData( form ) );
    const validStatus = [ "active", "inactive" ];

    if( !expressionReg.text.test( category ) ) return [ "La categoria debe contener mas de 3 caracteres" ];
    if( !validStatus.includes( status )) return [ "seleccione el estado de la categoria"];
    
    return [ undefined, { category, status, id }]
}

const handleSubmit = async ( event ) => {
    event.preventDefault();
    
    const [ error, data ]= validateForm( );
    if( error) return loadAlert( error, "alert-danger");

    const url_request = data.id === undefined 
        ? "/inventario/categorias/save"
        : "/inventario/categorias/update";

    const { code, msg} = await http( url_request , data );
    if ( code !== 201) return loadAlert( msg, "alert-danger" );
    
    code === 201 && form.reset();
    return loadAlert( msg, "alert-success");
}

form.addEventListener("submit", handleSubmit );