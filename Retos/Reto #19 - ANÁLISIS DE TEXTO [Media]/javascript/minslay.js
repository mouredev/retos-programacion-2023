
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

let myText = "Esto es una prueba de un texto. La palabra más larga es supercalifragilisticoespialidoso. Esta prueba tiene 3 oraciones.";
let numChar: number = 0;
let numWords: number = 0;
let numSentences: number = 0;
let wordLengthCounter: any[] = [];
let meanWords: number = 0;
let wordSeparator: string = " ";
let sentenceSeparator: string = ".";
let largestWord: string = "";
let initChar: number = 0;
let endChar: number = 0;
let resetWord: boolean = false;
let charsInWordCounter: number = 0;

class wordsAnalyzer {

    constructor() {
    }

    addToLengthArray() {
        if (charsInWordCounter != 0) {
            wordLengthCounter.push(charsInWordCounter);
        }
    }

    createLargestWord() {
        if (charsInWordCounter > largestWord.length) {
            largestWord = myText.substring(initChar, endChar);
        }
    }

    showResults() {
        console.log("Número de palabras: "+numWords);
        console.log("Letras por palabra: "+wordLengthCounter);
        console.log("Media: "+meanWords)
        console.log("Número de frases: "+numSentences);
        console.log("Palabra más larga: "+largestWord);
        console.log("-----------------------------------");
    }


    analyze() {
        for (let i = 0; i < myText.length; i++) {
            if (myText.charAt(i) == " " || myText.charAt(i) == ".") {
                numWords = (myText.charAt(i) == " ") ? numWords+1: numWords;
                numSentences = (myText.charAt(i) == ".") ? numSentences+1: numSentences;
                resetWord = true;
                this.addToLengthArray();
                this.createLargestWord();                
                charsInWordCounter = 0;   
            }
            else {
                if (resetWord) {
                    resetWord = false;
                    initChar = i;
                }    
                endChar = i;
                charsInWordCounter++;
            }
            this.createLargestWord();

            let sumWordsLength = wordLengthCounter.reduce((a, b) => a + b, 0);
            meanWords = sumWordsLength/wordLengthCounter.length;
            numChar++;
            }
        this.showResults();
    }
}

let game = new wordsAnalyzer()
game.analyze()

