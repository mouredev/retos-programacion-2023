/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */


const cesarEncrypt = (str, offset) => {
  const alphabet = 'abcdefghijklmnñopqrstuvwxyz';
  const alphabetLength = alphabet.length;
  return str
    .trim()
    .replace(/\s+/g, ' ')
    .split(' ')
    .map((word) => word.split('').reduce((acc, letter) => {
      const isUpperCase = letter === letter.toUpperCase();

      if (isUpperCase) letter = letter.toLowerCase();
      const index = alphabet.indexOf(letter);
      let newIndex = index + offset;

      if (newIndex >= alphabetLength) newIndex -= alphabetLength;
      if (newIndex < 0) newIndex += alphabetLength;

      const newLetter = alphabet[newIndex];
      return acc + (isUpperCase ? newLetter.toUpperCase() : newLetter);
    }, ''))
    .join(' ');
};

const cesarDecrypt = (str, offset) => cesarEncrypt(str, -offset);


// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
