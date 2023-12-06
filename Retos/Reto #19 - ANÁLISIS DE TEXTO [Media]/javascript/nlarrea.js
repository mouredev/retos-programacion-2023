/*
 * Crea un programa que analice texto y obtenga:
 * #- Número total de palabras.
 * #- Longitud media de las palabras.
 * #- Número de oraciones del texto (cada vez que aparecen un punto).
 * #- Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */


function checkText(text) {
    if (!text) return 'You have to enter some text!';

    const words = text.split(" ");
    const numOfWords = words.length;

    let wordsInfo = {};
    let maxLength = {word: words[0], wLength: words[0].length};
    const regex = /[^A-zÀ-ú]/g;     // any character A-z including accents
    
    let totalLength = 0;

    let numSentences = 1;

    for (let [index, word] of words.entries()) {
        // store the current word and its length
        wordsInfo[index] = {
            word: word.replace(regex, ''),
            wLength: word.replace(regex, '').length,
        };

        // update the largest word and its length
        if (maxLength.wLength < wordsInfo[index].wLength) {
            maxLength.word = wordsInfo[index].word;
            maxLength.wLength = wordsInfo[index].wLength;
        } else if (maxLength.wLength === wordsInfo[index].wLength && index !== 0) {
            maxLength.word = [maxLength.word];
            maxLength.word.push(word)
        }

        totalLength += wordsInfo[index].wLength;

        // count the number of sentences
        if (word.includes(".") && index !== (numOfWords - 1)) {
            numSentences++;
        }
    }

    // get the average word length
    const averageLength = Math.floor(totalLength / numOfWords);

    printResult(numOfWords, averageLength, numSentences, maxLength);
}


function printResult(nWords, averageLength, nSentences, maxLength) {
    console.log(`Number of words: ${nWords}`);
    console.log(`Average word length: ${averageLength}`);
    console.log(`Number of sentences: ${nSentences}`);
    console.log(`Largest word(s):\n'${maxLength.word}' (${maxLength.wLength} letters)`);
}


const text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non culpa impedit natus cum nobis in?'
checkText(text);