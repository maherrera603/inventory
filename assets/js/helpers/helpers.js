import { alert, alert_popup  } from "../elements.js";

export const formData = ( formData ) => Object.fromEntries( formData.entries() );

export const loadAlert = ( msg, cssClass ) => {
    alert.innerText = msg;
    alert.classList.add( cssClass );

    setTimeout(() => {
        alert.innerText = "";
        alert.classList.remove(cssClass);
    }, 3000);
}


export const loadAlertPopup = ( msg, cssClass ) => {
    alert_popup.innerText = msg;
    alert_popup.classList.add( cssClass );

    setTimeout(() => {
        alert_popup.innerText = "";
        alert_popup.classList.remove(cssClass);
    }, 3000);
}
