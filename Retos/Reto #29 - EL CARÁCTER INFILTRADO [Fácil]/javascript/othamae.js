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



const findDifferentChars = (str1, str2) => {
    if (str1.length !== str2.length) {
        return "The strings must have the same length"
    }
    const differentChars = [];
    for (let i = 0; i < str1.length; i++) {
        if (str1[i] !== str2[i]) {
            differentChars.push(str2[i])
        }
    }

    return differentChars
}

console.log(findDifferentChars("Me llamo mouredev", "Me llemo mouredov"))
console.log(findDifferentChars("Me llamo.Brais Moure", "Me llamo brais moure"))