export const http = async( url, data ) => {
    const resp = await fetch( url , {
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-Type": "application/json"
        }
    });

    if ( resp.redirected ) {
        window.location.href = resp.url
        return;
    }
    
    const result = await resp.json();
    return result;
}
