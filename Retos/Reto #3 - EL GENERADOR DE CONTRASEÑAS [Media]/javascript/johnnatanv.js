/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const randomPassword = (upper, number, symbol) => {
  let lowerLetter = "abcdefghijklmnopqrstuvwxyz";
  let upperLetter = lowerLetter.toUpperCase();
  let numbers = "0123456789";
  let symbols = '~`!@#$%^&*()_-+={[}]|:;"<,>.?/';
  let min = 8,
    max = 16;
  let passwordLength = Math.floor(Math.random() * (max - min)) + min;

  let DATA_RANDOM_STRING = lowerLetter;

  if (upper) DATA_RANDOM_STRING += upperLetter;
  if (number) DATA_RANDOM_STRING += numbers;
  if (symbol) DATA_RANDOM_STRING += symbols;

  let password = "";

  for (let i = 0; i <= passwordLength; i++) {
    password +=
      DATA_RANDOM_STRING[Math.floor(Math.random() * DATA_RANDOM_STRING.length)];
  }

  console.log(password);
};

// * Testing de el Generador de Contraseñas

randomPassword(); // * Solo letras minusculas
randomPassword(true); // * Solo letras mayusculas
randomPassword(false, true); // * Letras minusculas y numeros
randomPassword(true, true); // * Letras minusculas, mayusculas y numeros
randomPassword(true, false, true); // * Letras minusculas, mayusculas y simbolos
randomPassword(true, true, true); // * Letras minusculas, mayusculas, numeros y simbolos
randomPassword(false, false, true); // * Letras minusculas y simbolos
