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

const infiltrado = (cadena1, cadena2) => {
    let caracteres = []
    if(cadena1.length != cadena2.length) {
        return "Las cadenas deben tener la misma longitud"
    } else {
        for(i = 0; i <= cadena1.length; i++){
            if (cadena1[i] != cadena2[i]){
                caracteres.push(cadena2[i])
            }
        }
        return caracteres
    }
}

console.log(infiltrado("Me llamo mortizp ", "me.llamo mortizp/")) // = [ 'm', '.', '/' ]
console.log(infiltrado("Tengo un. perro llamado Nika", "t>ngo una perro .yamado nica")) // = [ 't', '>', 'a', '.', 'y', 'n', 'c' ]
