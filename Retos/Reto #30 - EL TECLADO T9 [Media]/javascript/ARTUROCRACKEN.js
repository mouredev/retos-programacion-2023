/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

const alphabet = {2: "a", 22: "b", 222: "c", 3: "d", 33: "e", 333: "f", 4: "g", 44: "h", 444: "i", 5: "j", 55: "k", 555: "l", 6: "m", 66: "n", 666: "o", 7: "p", 77: "q", 777: "r", 7777: "s", 8: "t", 88: "u", 888: "v", 9: "w", 99: "x", 999: "y", 9999: "z"};

function t9keyboard(input) {
  if (typeof input !== "string") {
    console.error("input must be a string.")
  }

  let listOfCharacters = input.split("-");

  let result = "";

  for (character in listOfCharacters) {
    result += alphabet[listOfCharacters[character]];
  }

  console.log(result.toUpperCase());
  
  return;
}

t9keyboard("6-666-88-777-33-3-33-888");
t9keyboard("2-777-8-88-777-666-222-777-2-222-55-33-66");
t9keyboard("3-666-66-33");
