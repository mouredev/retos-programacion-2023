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
    let totalWords = 0
    let averageWordLength = 0
    let totalSentences = 0
    let longestWord = ''

    text.replaceAll(/\(|\)|\[|\]|\n/g,'').split(' ').map(word => {
        if (word.includes('.')) {
            totalSentences++
        }

        return word.split('.').map(w => {
            console.log(w)
            if(w.match(/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$|[y]/g) && w.length > 0){
                console.log(w)
                console.log(w.match(/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$|[y]/g).join(''))
                totalWords++
                averageWordLength += w.length
                if (w.length > longestWord.length) {
                    longestWord = w
                }
            }
        })

    })
    averageWordLength /= totalWords

    return {
        totalWords: totalWords,
        averageWordLength: averageWordLength,
        totalSentences: totalSentences,
        longestWord: longestWord
    }
}


console.log(analizeText(`Crea un programa que analice texto y obtenga :
- Número total de palabras.
- Longitud media de las palabras.
- Número de oraciones del texto (cada vez que aparecen un punto).
- Encuentre la palabra más larga.

Todo esto utilizando un único bucle.`))