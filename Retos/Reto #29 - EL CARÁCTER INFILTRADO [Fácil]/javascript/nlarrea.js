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

/**
 * Function that receives two texts of the same length and returns the
 * different characters of the second one.
 * 
 * @param {String} textOne Main text to compare
 * @param {String} textTwo Second text to compare
 * @returns {Array} Array containing the different characters
 */
function infiltratedCharacters(textOne, textTwo) {
    const infiltratedChars = [];
    const lengthOne = textOne.length;

    if (lengthOne !== textTwo.length) {
        console.log("Both texts must be equal in length!");
        return [];
    }

    for (let i=0; i<lengthOne; i++) {
        if (textOne[i] !== textTwo[i]) {
            infiltratedChars.push(textTwo[i]);
        }
    }

    if (infiltratedChars.length === 0) {
        console.log("Both texts are the same!");
    }

    return infiltratedChars;
}


console.log(infiltratedCharacters("Me llamo mouredev", "Me llemo mouredov"));           // ['e', 'o']
console.log(infiltratedCharacters("Me llamo.Brais Moure", "Me llamo brais moure"));     // [' ', 'b', 'm']
console.log(infiltratedCharacters("Me llamoBrais Moure", "Me llamo brais moure"));      // [] -> prints: Both texts must be equal in length!
console.log(infiltratedCharacters("Me llamo Brais Moure", "Me llamo Brais Moure"));     // [] -> prints: Both texts are the same!