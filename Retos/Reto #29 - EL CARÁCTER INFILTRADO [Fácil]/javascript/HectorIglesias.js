/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

function comparar_cadenas(cadena_1, cadena_2){
    let aux= new Array
    if(cadena_1.length == cadena_2.length){
        for(let i=0; i<cadena_1.length; i++){
            if(cadena_1[i] != cadena_2[i]){
                aux.push(cadena_2[i])
            }
        }
        return aux
    }
    else{
        return "La longitud de las dos cadenas debe ser la misma"
    }
}

console.log(comparar_cadenas("Hola mundo", "hola.Mundo"))