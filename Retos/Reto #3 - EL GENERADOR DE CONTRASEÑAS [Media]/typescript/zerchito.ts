/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const CHARACTERS_LIB = {
  alphabet: "abcdefghijklmnopqrstuvwxyz",
  numbers: "0123456789",
  symbols: "&/\\^=?!@#$%*+.,:;|()[]{}<>-_"
}

function generatePassword (
  numberOfCharacters: number,
  enableUpperCase: boolean,
  enableNumbers: boolean,
  enableSimbols: boolean
) {
  let password = '';
  let library = CHARACTERS_LIB.alphabet;
  if(enableUpperCase) library += CHARACTERS_LIB.alphabet.toUpperCase();
  if(enableNumbers) library += CHARACTERS_LIB.numbers;
  if(enableSimbols) library += CHARACTERS_LIB.symbols;
  for(let number = 0; number < numberOfCharacters; number++){
    const random = Math.random() * library.length-1;
    password = password + library.charAt(random); 
  }
  return password;
}

console.log(generatePassword(16, true, true, true));
