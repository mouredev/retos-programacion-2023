/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const MAX_LENGTH = 16;
const MIN_LENGTH = 8;
const LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
const UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const NUMBERS = "0123456789";
const SYMBOLS = "!@#$%&*()+={[}]|:;?";

function createPassword({
  length = 10,
  uppercaseLetter = true,
  numbers = true,
  symbols = true,
}) {
  const validOptions =
    LOWERCASE +
    (numbers ? NUMBERS : "") +
    (symbols ? SYMBOLS : "") +
    (uppercaseLetter ? UPPERCASE : "");

  return generateString(length, validOptions);
}

function generateString(strLength, options) {
  let result = "";
  for (let i = 0; i < strLength; i++) {
    const randomIndex = randomIntFromInterval(0, options.length - 1);
    result += options[randomIndex];
  }
  return result;
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

console.log(
  createPassword({ length: 10, upper: true, numbers: true, symbols: true })
);
