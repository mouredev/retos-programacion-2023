/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const passwordGenerator = () => {
  let listOfWords = [];
  let finallyPassword = "";
  for (var i = 0; i < lengthOfPassword(); i++) {
    var chooseLetter =
      completeList()[Math.floor(Math.random() * completeList().length)];
    listOfWords.push(chooseLetter);
  }
  finallyPassword += listOfWords.join("");
  return finallyPassword;
};

const lengthOfPassword = () => {
  lengthOfNumber = [];
  for (let number = 8; number <= 16; number++) {
    lengthOfNumber.push(number);
  }
  return lengthOfNumber[Math.floor(Math.random() * lengthOfNumber.length)];
};

const completeList = () => {
  var lowerCase = "abcdefghijklmnopqrstuvwxyz".split("");
  var upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  var numbers = "0123456789".split("");
  var punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".split("");
  return lowerCase.concat(upperCase, numbers, punctuation);
};

console.log(passwordGenerator());
