/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


function getParamsUrl(url) {
    return url.match(/\=\w+/gi).map(e => e.split('=')[1])
}

console.log(getParamsUrl('https://retosdeprogramacion.com?year=2023&challenge=0'))

