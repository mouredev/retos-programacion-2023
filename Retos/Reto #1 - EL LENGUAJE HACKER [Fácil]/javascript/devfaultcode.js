/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const readline = require("readline");

function phraseChanger(character) {
    let newCharacter
    switch (character) {
        
        case 'a':
            return newCharacter = '4'

        case 'b':
            return newCharacter = 'I3'

        case 'c':
            return newCharacter = '['

        case 'd':
            return newCharacter = ')'

        case 'e':
            return newCharacter = '3'

        case 'f':
            return newCharacter = '|='

        case 'g':
            return newCharacter = '&'
        
        case 'h':
            return newCharacter = '#'

        case 'i':
            return newCharacter = '1'

        case 'j':
            return newCharacter = ',_|'

        case 'k':
            return newCharacter = '>|'

        case 'l':
            return newCharacter = '1'

        case 'm':
            return newCharacter = '/\/\ '

        case 'n':
            return newCharacter = '^/'

        case 'o':
            return newCharacter = '0'

        case 'p':
            return newCharacter = '|*'

        case 'q':
            return newCharacter = '(_,)'

        case 'r':
            return newCharacter = 'I2'

        case 's':
            return newCharacter = '5'

        case 't':
            return newCharacter = '7'

        case 'u':
            return newCharacter = '(_)'

        case 'v':
            return newCharacter = '\/'

        case 'w':
            return newCharacter = '\/\/'

        case 'x':
            return newCharacter = '><'

        case 'y':
            return newCharacter = 'j'

        case 'z':
            return newCharacter = '2'

        case '0':
            return newCharacter = 'o'

        case '1':
            return newCharacter = 'L'

        case '2':
            return newCharacter = 'R'

        case '3':
            return newCharacter = 'E'

        case '4':
            return newCharacter = 'A'

        case '5':
            return newCharacter = 'S'

        case '6':
            return newCharacter = 'b'

        case '7':
            return newCharacter = 'T'

        case '8':
            return newCharacter = 'B'

        case '9':
            return newCharacter = 'g'

        default:
            return character
    }
}

function hackerLenguage() {
    let sentence
    let phraseLength
    let newPhrase = ''
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    rl.question("Please write a phrase or sentence: ", function (answer){
        sentence = answer.toLowerCase()
        phraseLength = answer.length
        for (let i = 0; i < phraseLength ; i++) {
            newPhrase += phraseChanger(sentence.charAt(i))
        }
        console.log(newPhrase);
        rl.close();
    })

}

hackerLenguage()

