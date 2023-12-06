/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const getParameters = (url) => {
    let index = url.indexOf('?');

    if (index === -1 || index === (url.length - 1)) {
        return "No hay parámetros";
    }
    
    let parameters = url.slice(url.indexOf('?') + 1);

    const getValues = (params) => {
        let value;

        if (params.indexOf('&') !== -1) {
            value = params.slice(params.indexOf('=') + 1, params.indexOf('&'));
            params = params.slice(params.indexOf('&') + 1);
        } else {
            value = params.slice(params.indexOf('=') + 1);
            params = "";
        }
        
        return [params, value];
    }

    let value;
    let values = [];

    do {
        [parameters, value] = getValues(parameters);
        values.push(value);
    } while(parameters.indexOf('=') !== -1);

    if (values.length === 1 && values[0] === "") return "Los parámetros no están definidos"

    return values;
}


console.log(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0"));    // ['2023', '0']
console.log(getParameters("https://retosdeprogramacion.com"));                          // No hay parámetros
console.log(getParameters("https://retosdeprogramacion.com?"));                         // No hay parámetros
console.log(getParameters("https://retosdeprogramacion.com?year=2023"));                // ['2023']
console.log(getParameters("https://retosdeprogramacion.com?year=2023&"));               // ['2023']
console.log(getParameters("https://retosdeprogramacion.com?year=&"));                   // Los parámetros no están definidos