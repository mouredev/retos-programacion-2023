/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

function analizeText(text) {
  text = text.trim().replaceAll("\n", " ");

  let numWords = 0;
  let numSentences = 0;
  let longestWord = "";
  let averageLength = 0;

  let words = text.split(" ");
  let wordsLength = 0;

  words.forEach((word) => {
    if (word.length > longestWord.length) {
      longestWord = word;
    }

    if (word.includes(".")) {
      numSentences += 1;
    }

    wordsLength += word.length;
  });

  numWords = words.length;
  averageLength = Math.round(wordsLength / numWords);

  console.log(`Resultados:
    Numero total de palabras: ${numWords}
    Longitud media de las palabras: ${averageLength}
    Numero de oraciones del texto: ${numSentences}
    Palabra mas larga: ${longestWord}`);
}

const text1 =
  "Hola perro, como te va? a mi bien. y a ti? bien tambien. por eso, te llamas pellensarniustiquio.";
const text2 = `
Ey, el texto 1
no tiene mucho sentido.

Pero este tampoco es que lo tenga...
`;

analizeText(text1);
analizeText(text2);
