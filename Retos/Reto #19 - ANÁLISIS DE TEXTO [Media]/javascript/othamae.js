/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

function textAnalyze(text) {
    let words = text.split(' ');
    let sentences = text.split('.');
    let longestWord = words[0];

    for (let i = 0; i < words.length; i++) {
        if (words[i].length > longestWord.length) {
            longestWord = words[i];
        }
    }

    return {
        words: words.length,
        averageWordLength: words.join('').length / words.length,
        sentences: sentences.length,
        longestWord: longestWord
    }
}

const text = "Crea un programa que analice texto y obtenga:  Número total de palabras.  Longitud media de las palabras.  Número de oraciones del texto(cada vez que aparecen un punto). Encuentre la palabra más larga (Supercalifragilisticoespialidoso). Todo esto utilizando un único bucle."
console.log(textAnalyze(text))