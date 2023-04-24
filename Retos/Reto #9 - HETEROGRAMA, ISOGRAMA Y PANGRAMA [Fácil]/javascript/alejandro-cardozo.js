/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

/**
 * This function returns true if a string contains no repeated characters, and false otherwise.
 * @param  {String} str the string to analyze
 * @return {Boolean}    true if the string contains no repeated characters, and false otherwise
 */
function isHeterogram(str) {
  const { charsInWord } = charsInString(str);
  return Object.values(charsInWord).every((el) => el === 1);
}

/**
 * This function returns true if a string contains the same number of occurrences of all characters, and false otherwise.
 * @param  {String} str the string to analyze
 * @return {Boolean}    true if the string contains the same number of occurrences of all characters, and false otherwise
 */
function isIsogram(str) {
  const { charsInWord, formattedWord } = charsInString(str);
  const isogramOrder = charsInWord[formattedWord[0]];
  return Object.values(charsInWord).every((el) => el === isogramOrder);
}

/**
 * This function returns true if a string contains all the letters of the alphabet, and false otherwise.
 * @param  {String} str the string to analyze
 * @return {Boolean}    true if the string contains all the letters of the alphabet, and false otherwise.
 */
function isPangram(str) {
  const { charsInWord } = charsInString(str);
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  for (char of alphabet) {
    if (!charsInWord[char]) {
      return false;
    }
  }
  return true;
}

/**
 * This function returns an object containing the frequency of characters in a string
 * and the formatted string in lower case with no non-alphanumeric characters.
 * @param  {String} str the string to analyze
 * @return {Object}     an object with the character frequency and the formatted string
 */
function charsInString(str) {
  const charsInWord = {};
  const formattedWord = str.toLowerCase().replace(/\W/g, '');
  for (char of formattedWord) {
    if (charsInWord[char]) {
      charsInWord[char]++;
    } else {
      charsInWord[char] = 1;
    }
  }
  return { charsInWord, formattedWord };
}

/* TESTS */
console.log('');
console.log('isHeterogram tests');
console.log('- centrifugado -->', isHeterogram('centrifugado')); //true
console.log('- adulterinos -->', isHeterogram('adulterinos')); //true
console.log('- perro -->', isHeterogram('perro')); //false
console.log('- gaviota -->', isHeterogram('gaviota')); //false
console.log('');
console.log('isIsogram tests');
console.log('- caucasus -->', isIsogram('caucasus')); //true
console.log('- intestines -->', isIsogram('intestines')); //true
console.log('- puppy -->', isIsogram('puppy')); //false
console.log('- kitty -->', isIsogram('kitty')); //false
console.log('');
console.log('isPangram tests');
console.log(
  "- What is love? Baby don't hurt me -->",
  isPangram("What is love? Baby don't hurt me")
); //false
console.log(
  '- Never gonna give you up -->',
  isPangram('Never gonna give you up')
); //false
console.log(
  '- Sylvia wagt quick den Jux bei Pforzheim -->',
  isPangram('Sylvia wagt quick den Jux bei Pforzheim')
); //true
console.log(
  '- Jackdaws love my big sphinx of quartz -->',
  isPangram('Jackdaws love my big sphinx of quartz')
); //true
console.log('');