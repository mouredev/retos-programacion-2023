/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword(n, letrasMayusculas, numeros, simbolos) {
  // string vacio donde se generara la password
  let password = "";

  // variables donde se almacenaran los caracteres que se utilizaran para la password
  let capitalLetters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
  let lowercaseLetters = "abcdefghijklmnñopqrstuvwxyz";
  let numbers = "0123456789";
  let symbols = ".?,;-_¡!¿*%&$/()[]{}|@><";

  // union de todos los caracteres
  let union = "";

  // con o sin letras mayusculas
  letrasMayusculas
    ? (union = union + capitalLetters)
    : (union = union + lowercaseLetters);

  // con o sin numeros
  numeros ? (union = union + numbers) : union;

  // con simbolos o sin simbolos
  simbolos ? (union = union + symbols) : union;

  // condicional para controlar la longitud de la password
  if (n >= 8 && n <= 16) {
    for (let i = 0; i < n; i++) {
      let generated = Math.floor(Math.random() * union.length);
      password = password + union.charAt(generated);
    }
  } else {
    return "Error: Longitud permitida entre 8 y 16 caracteres";
  }

  // retornar la password
  return `la contraseña generada es: ${password} `;
}

console.log(generatePassword(16, false, true, true));
