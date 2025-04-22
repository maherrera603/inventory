import { form, form_history, overlay_history } from "../elements.js";
import { formData, loadAlert } from "../helpers/helpers.js";
import { expressionReg } from "../helpers/expression.js";
import { http } from "../helpers/http.js";


const validForm = () => {
    const { id = undefined, name, price, quantity, sku, status, category } = formData( new FormData( form ));
    const validStatus = [ "available", "exhausted" ];

    if( !expressionReg.text.test( name )) return ["Ingrese el nombre del producto, debe contener mas de 3 caracteres"]

    if( !expressionReg.number.test( sku ) ) return ["Ingrese un sku valido"]
    
    if( sku.length < 10 || sku.length > 10 ) return [ "el sku debe contener 10 digitos" ];
    
    if( !expressionReg.number.test( quantity) || parseInt( quantity) < 1 ) return [ "Ingrese la cantidad del producto"]
    
    if( !expressionReg.number.test( price ) || parseFloat( price) < 50 ) return [ "Ingrese un precio valido" ]

    if( !validStatus.includes( status) ) return [ "seleccione el estado del producto"]

    return [ undefined, { id, name, price, quantity, sku, status, category}] ;
}



const handleSubmit = async ( event ) => {
    event.preventDefault();
    const [ error, data ] = validForm();
    if( error ) return loadAlert( error, "alert-danger");

    const url_request = data.id === undefined 
        ? "/inventario/productos/save" 
        : "/inventario/productos/update";

    const { code, msg, product = {} } = await http( url_request, data );

    console.log(code);
    

    if( code !== 201 && code !== 200 ) return loadAlert( msg, "alert-danger");
    
    if (code == 200 ) form.reset();
    
    if (code == 201) setTimeout( () => activeFormHistory(  product ), 500 );
    
    return loadAlert( msg, "alert-success")
}


const activeFormHistory = ({ id, user, name }) => {
    form_history.querySelector("#id_product").value = id
    form_history.querySelector("#user").value = user
    form_history.querySelector("#product").value = name
    overlay_history.classList.add("overlay_history_active")
}

form.addEventListener( "submit", handleSubmit );