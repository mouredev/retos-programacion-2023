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


function findChangingCharacters(string1, string2) {
    let changingCharacters = [];
    for (let i = 0; i < string1.length; i++) {
      if (string1[i] !== string2[i]) {
        changingCharacters.push(string2[i]);
      }
    }
    return changingCharacters;
  }
  
  console.log(findChangingCharacters("hello paula", "hello Paule"));
  