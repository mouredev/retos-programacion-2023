/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
const ENCODING_VALUE = 3;
const alphabet: string[] = [...Array(26).keys()].map((index) =>
  String.fromCharCode(index + 97)
);

const textToCesarEncrypt = (text: string): string => {
  const rgx_keys_encrypt = new RegExp(/[a-z]/gi);
  const textToArray = text.toLowerCase();
  const lastLetter = alphabet.length - 1; // start over if the letter is z
  return textToArray.replace(rgx_keys_encrypt, (word) => {
    const found = alphabet.indexOf(word);
    const indexAl = (found === lastLetter ? -1 : found) + ENCODING_VALUE;
    return alphabet[indexAl];
  });
};
// holaza buenas -> krodcd exhqdv

const textToCesarDecrypt = (text: string): string => {
  const rgx_keys_decrypt = new RegExp(/[a-z]/gi);
  const textToArray = text.toLowerCase();
  const lastLetter = alphabet.length - 1; // start over if the letter is z
  return textToArray.replace(rgx_keys_decrypt, (word) => {
    const found = alphabet.indexOf(word);
    const indexAl = (found === 0 ? lastLetter + 1 : found) - ENCODING_VALUE;
    return alphabet[indexAl < 0 ? lastLetter : indexAl];
  });
};
// krodcd exhqdv -> holaza buenas