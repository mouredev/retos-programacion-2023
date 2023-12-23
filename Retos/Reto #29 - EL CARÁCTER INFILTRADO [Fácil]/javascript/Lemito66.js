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

const find_differences = (str1, str2) => {
    const differences = [];
    if (str1.length === str2.length) {
        for (let i = 0; i < str1.length; i++) {
            if (str1[i] !== str2[i]) {
                differences.push(str2[i]);
            }
        }
    }
    return differences;
};

console.log(find_differences("Me llamo mouredev", "Me llemo mouredov"));