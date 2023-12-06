/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
const alphabet = 'abcdefghijklmnñopqrstuvwxyz';


/**
 * Function that checks if a string is a heterogram: each letter appears just once
 * @param {} word
 * @returns
 */
function heterogram(word) {
  const frequencies = Object.values(findFrequencies(word));
  return frequencies.every(x => x === 1);
}

/**
 * Function that checks if every letter in a word appears the same number of times
 */
function isogram(word) {
  const frequencies = Object.values(findFrequencies(word));
  return frequencies.every(freq => freq === frequencies[0]);
}

function findFrequencies(text) {
  return text.replace(/[ !"$%&/()=?¿¡|@.,-_<>ç+*{}[\]\\]/, '')
    .replace(/[áäà]/, 'a')
    .replace(/[éèë]/, 'e')
    .replace(/[íìï]/, 'i')
    .replace(/[óòö]/, 'o')
    .replace(/[úùü]/, 'u')
    .toLowerCase().split('').reduce((set, letter) => { set[letter] = (set[letter] || 0) + 1; return set; }, {});
}

/**
 * Funtion that checks if a string is a pangram: conatains all the letters in the alphabet
 */
function pangram(inputString) {
  const inputChars = inputString.toLowerCase().split('');
  return alphabet.split('').every((char) => inputChars.indexOf(char) !== -1);
}


function test(str) {
  console.log(`"${str}" is an heterogram? ${heterogram(str)}`);
  console.log(`"${str}" is an isogram? ${isogram(str)}`);
  console.log(`"${str}" is a pangram? ${pangram(str)}`);
}


test('Mi hijo degustó en el festival de bayas una extraña pizza de kiwi con queso');
test('yoyó');
test('murciélago');