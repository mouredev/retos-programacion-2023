/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

function getParameters( url = ""){
    var result = [];
    if ( url === '' || url.indexOf('?') === -1) return result;    
    var params = (url.substring(url.indexOf('?')+1, url.lenght)).split('&');    
    for( let i = 0; i < params.length; i++ ) {
        result.push(params[i].substring(params[i].indexOf('=')+1, params[i].length));
    }
    return (result);
}

var url = "https://retosdeprogramacion.com?year=2023&challenge=0";

console.log(getParameters(url));