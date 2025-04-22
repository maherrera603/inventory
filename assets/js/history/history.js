import { form_history } from "../elements.js";
import { formData, loadAlertPopup } from "../helpers/helpers.js";
import { http } from "../helpers/http.js"


const handleValidForm = () => {
    const { id_product, user, type_move, quantity, description } = formData( new FormData( form_history ));

    if( id_product.length < 1 ) return [ "el id del producto es invalido", undefined];

    if( user.length < 1) return [ "el id del usuario es invalido", undefined ];

    if( type_move === undefined) return [ "Seleccione el tipo de movimiento", undefined ];

    if( parseInt( quantity ) < 1 ) return [ "Ingrese el valor de la cantidad", undefined ];

    if( description.length < 10 ) return [ "Ingrese una descripcion mas detallada del moviento", undefined ];

    return [ undefined, { id: id_product, user, type: type_move, quantity, description }];
}

const handleSubmit = async( event ) => {
    event.preventDefault();

    const [ error, data ] = handleValidForm();
    if( error ) return loadAlertPopup( error, "alert_popup_danger" );

    const { code, msg } = await http("/inventario/historial/save", data ); 

    if( code !== 201 ) return loadAlertPopup( msg, "alert_popup_danger" );

    return loadAlertPopup( msg, "alert_popup_success" );
}


form_history.addEventListener( "submit", handleSubmit );