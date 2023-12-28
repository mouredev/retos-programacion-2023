/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

/**
 *
 * @param {String} str
 */
function analyzeText(str) {
  let numOfWords = 0,
    averageLengthOfWords = 0,
    numOfSentences = 0;

  let longestWord = 0;

  let sumOfLengths = 0; // Para calcular la long media de palabras => averageLengthOfWords = (sumOfLengths / numOfWords)

  let i = 0;
  let j = 0;
  while (i <= str.length) {
    // Jump Spaces and special characters
    while (i < str.length && !isLetter(str[i])) i++;

    // We're found a word or end of string.
    j = i;
    while (i < str.length && isLetter(str[i])) i++;

    if (i === str.length) break;

    // We are in a word
    if (str[i] === '.') numOfSentences++;

    numOfWords++;
    sumOfLengths += i - j;
    longestWord = Math.max(longestWord, i - j);
  }

  if (str.length > 0 && isLetter(str[i - 1])) {
    numOfSentences++;
    numOfWords++;
    i--;
    sumOfLengths += i - j;
    longestWord = Math.max(longestWord, i - j);
  }

  averageLengthOfWords = Math.floor(
    sumOfLengths / (str.length === 0 ? 1 : numOfWords) // We can't divide by 0 if it's an empty string.
  );
  console.log('Num of Words: ' + numOfWords);
  console.log('Average Length of Words: ' + averageLengthOfWords);
  console.log('Num of sentences:  ' + numOfSentences);
  console.log('Longest word:  ' + longestWord);
}

function isLetter(char) {
  return (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z');
}

analyzeText('Hello. This is an example of string for testing.');

// analyzeText('');

// analyzeText(
//   'El rescate del telescopio espacial Hubble: como es el plan espacial para evitar que caiga a la Tierra. La ultima asistencia técnica ocurrio en 2009, pero luego del retiro de los transbordadores espaciales, la NASA no lo ha vuelto a reparar. Piezas daniadas y falta de combustible para mantenerse en orbita, son las principales urgencias.'
// );

// analyzeText(
//   'El rescate del telescopio espacial Hubble: como es el plan espacial para evitar que caiga a la Tierra. La ultima asistencia técnica ocurrio en 2009, pero luego del retiro de los transbordadores espaciales, la NASA no lo ha vuelto a reparar. Piezas daniadas y falta de combustible para mantenerse en orbita, son las principales urgencias'
// );
