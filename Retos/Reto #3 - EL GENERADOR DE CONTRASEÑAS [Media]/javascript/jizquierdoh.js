/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const NUMBERS = '0123456789'.split('');
const UPPERCASE = LETTERS.split('');
const LOWERCASE = LETTERS.toLowerCase().split('');
const SPECIAL_CHARS = '@#$%&*-_=+!/?()'.split('');

const generatePassword = (
  length = 8,
  withUppercase = false,
  withSpecialChars = false,
  withNumbers = false
) => {
  let charArray = [];
  let generatedPassword = '';
  charArray = [...charArray, ...LOWERCASE];
  length = length > 16 ? 16 : length && length < 8 ? 8 : length;

  if (withUppercase) {
    charArray = [...charArray, ...UPPERCASE];
  }

  if (withSpecialChars) {
    charArray = [...charArray, ...SPECIAL_CHARS];
  }

  if (withNumbers) {
    charArray = [...charArray, ...NUMBERS];
  }

  if (charArray.length <= 0) return

  const maxArrayIndex = charArray.length;
  const minArrayIndex = 0;
  for (let idx = 0; idx < length; idx++) {
    const randomIndex = Math.floor(
      Math.random() * (maxArrayIndex - minArrayIndex) + minArrayIndex
    );

    generatedPassword += charArray[randomIndex];
  }

  return generatedPassword;
}

console.log(generatePassword(7, true, true, true));
console.log(generatePassword(8, false, true, true));
console.log(generatePassword(9, true, false, true));
console.log(generatePassword(10, true, true, false));
console.log(generatePassword(11, true, false, false));
console.log(generatePassword(12, false, false, true));
console.log(generatePassword(22, false, true, false));