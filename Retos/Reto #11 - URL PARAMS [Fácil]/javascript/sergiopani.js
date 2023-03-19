/**
 * Url de ejemplo:
 * https://retosdeprogramacion.com?year=2023&challenge=0
 * 
 * Objetivo -> devulver un objeto con los parametros
 */

const urlToParams = (url) =>{
    //Paso 1 -> Cortamos el length del string en el primer ?
    let urlParams = url.slice(url.indexOf('?')+1);

    //Paso 2 -> Creamos el objeto donde guardaremos los parametros
    let params = {};

    //Paso 3 -> Hacemos nested split para separar los parametros
    urlParams.split('&').forEach((param) => {
        let [key, value] = param.split('=');
        params[key] = value;
    }
    );

    return params;

}

urlToParams('https://retosdeprogramacion.com?year=2023&challenge=0')
