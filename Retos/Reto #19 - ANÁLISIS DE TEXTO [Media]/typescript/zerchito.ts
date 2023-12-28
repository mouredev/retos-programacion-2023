/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

{
  function analyzeText(text: string): void {
    text = text.trim();
    let wordsCount = 0;
    let wordsLenght= 0;
    let numberOfSentences = 0;
    let longestWord = '';
    let currentWord = '';
    for(let index = 0; index < text.length; index++) {
      const char = text.charAt(index);
      if(char === ' '){
        if(currentWord.length > 0) {
          wordsCount++;
          console.log(currentWord.length)
          wordsLenght += currentWord.length;
          longestWord = currentWord.length > longestWord.length ? currentWord : longestWord;
        }
        currentWord = '';
      } else if (char === '.') {
        if(currentWord.length > 0) {
          wordsCount++;
          console.log(currentWord.length)
          wordsLenght += currentWord.length;
          longestWord = currentWord.length > longestWord.length ? currentWord : longestWord;
          numberOfSentences++;
        }
        currentWord = '';
      } else {
        currentWord += char;
      }
    }
    if(currentWord.length > 0) {
      wordsCount++;
      console.log(currentWord.length)
      wordsLenght += currentWord.length;
      longestWord = currentWord.length > longestWord.length ? currentWord : longestWord;
      numberOfSentences++;
    }
    console.log(`Number of words: ${wordsCount}`);
    console.log(`Words lenght media: ${wordsLenght / wordsCount}`);
    console.log(`Number of sentences: ${numberOfSentences}`);
    console.log(`Longest word: ${longestWord}`);
  }

  analyzeText('Esta es una prueba. para ver si el analizador funciona. hehe. Hola ten un lindo dia')
}