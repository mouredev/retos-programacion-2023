/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


const hackerSpeak = {
    "a": "4",
    "b": "I3",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "&",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "1",
    "m": "/\\/\\",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "I2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "j",
    "z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o"
}

function translateToHackerSpeak(text) {
    let hackText = "";
    for (let i = 0; i < text.length; i++) {
        let selectedWord = text[i];
        let hackedWord = hackerSpeak[selectedWord.toLowerCase()]
        if(hackedWord == undefined){
            hackText += selectedWord
        }else{
            hackText += hackedWord
        }
    }
    return hackText
}
//Examples
console.log(translateToHackerSpeak("LEET")); // 1337
console.log(translateToHackerSpeak("HELLO")); // #3110
console.log(translateToHackerSpeak("HACKER")); // #4[>|3I2
console.log(translateToHackerSpeak("BANANA")); // I34^/4^/4
console.log(translateToHackerSpeak('This is a string test.')); // 7#15 15 4 57I21^/& 7357.
console.log(translateToHackerSpeak('Hola Mundo - Retos Semanales')); // #014 /\/\(_)^/)0 - I23705 53/\/\4^/4135
console.log(translateToHackerSpeak('JavaScript')); // ,_|4\/45[I21|*7