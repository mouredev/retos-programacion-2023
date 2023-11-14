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

function cadena(a,b){
    if(a.length!==b.length) return console.log('Las deben contener la misma cantidad de caracteres')
    let lista = []
    for(let i=0; i<a.length; i++){
        if(a[i]!==b[i]) lista.push(b[i])
    }
    return lista
}
console.log(cadena('Me llamo mouredev','Me llemo mouredov'))
console.log(cadena('Me llamo.Brais Moure','Me llamo brais moure'))