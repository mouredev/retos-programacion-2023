/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const process = require('process');

// define charsets
const lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
const symbols = ['\\', '!', '\"', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '@', '#', '¡', '-', '<', '>', '_', '.', ':', ',', ';', '{', '}', '[', ']', '^', '*', 'Ç'];

function generateRandomPassword(length = 8, withNumbers = false, withUppercase = false, withSymbols = false) {
  let charSet = [...lowercase];
  if (withNumbers) {
    charSet = charSet.concat(...numbers)
  }
  if (withUppercase) {
    charSet = charSet.concat(...uppercase)
  }
  if (withSymbols) {
    charSet = charSet.concat(...symbols);
  }

  // iterate on the shuffle to get a better result
  // for (let i = 0; i < 10; i++) {
  for (let i in [...charSet]) {
    charSet.sort(() => 0.5 - Math.random());
  }

  const password = charSet.slice(0, length);
  // verify password fulfills specs
  if (!containsChar(password, lowercase)) {
    return generateRandomPassword(length, withNumbers, withUppercase, withSymbols);
  }
  if (withUppercase && !containsChar(password, uppercase)) {
    return generateRandomPassword(length, withNumbers, withUppercase, withSymbols);
  }
  if (withNumbers && !containsChar(password, numbers)) {
    return generateRandomPassword(length, withNumbers, withUppercase, withSymbols);
  }
  if (withSymbols && !containsChar(password, symbols)) {
    return generateRandomPassword(length, withNumbers, withUppercase, withSymbols);
  }
  return password.join('');
}

/**
 * Function that checks if ```set``` constains any of the elements in ```elements```
 * @param {*} set 
 * @param {*} elements 
 * @returns 
 */
function containsChar(set, elements) {
  return elements.some((c) => set.includes(c));
}

// parse command line args to setup the generator
const arguments = process.argv.slice(2, process.argv.length);
// define defaults
let passLenght = 8;
let useUppercase = false;
let useNumbers = false;
let useSymbols = false;

if (arguments.includes('-h')) {
  console.log(`\
  contraseña -n -l -u -s N
  Si no se porporcionan parámetros, se usarán los parámetros por defecto.
    -n  incluye números
    -u  incluye mayúsculas
    -s  incluye símbolos
    N   número de caracteres a incluir en la constraseña
  `);
  process.exit(0);
}
if (arguments.includes('-u')) { useUppercase = true; }
if (arguments.includes('-n')) { useNumbers = true; }
if (arguments.includes('-s')) { useSymbols = true; }
passLenght = arguments.filter((s) => !s.startsWith('-'))[0] || 8;
if (passLenght < 8 || passLenght > 16) {
  console.log('La longitud debe ser un número entre 8 y 16');
  process.exit(-1);
}

console.log(generateRandomPassword(passLenght, useNumbers, useUppercase, useSymbols));
