/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

function extraeValores(url) {

  return ((url
    .split('?')[1] || '') // get the query string part
    .split('&') || []) // split params
    .filter((param) => param !== '') // when no params, we have an empty string here that needs to be filtered out
    .map((param) => param.split('=')[1]); // keep only the value of each param
}
console.log(extraeValores('https://retosdeprogramacion.com?year=2023&challenge=0'));
console.log(extraeValores('https://retosdeprogramacion.com?year=2023&challenge=0&name=me&age=45'));
console.log(extraeValores('https://retosdeprogramacion.com'));
console.log(extraeValores('https://retosdeprogramacion.com?'));