// ## Enunciado

// ```
// /*
//  * Escribe un programa que reciba un texto y transforme lenguaje natural a
//  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
//  *  se caracteriza por sustituir caracteres alfanuméricos.
//  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
//  *   con el alfabeto y los números en "leet".
//  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
//  */
// ```

const diccionarioLeet = {
    // Letras mayúsculas
    "A": "4",
    "B": "8",
    "C": "(C)",
    "D": "|)",
    "E": "3",
    "F": "|=",
    "G": "6",
    "H": "|-|",
    "I": "1",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "|\\/|",
    "N": "|\\\|",
    "O": "0",
    "P": "|*",
    "Q": "0",
    "R": "|2",
    "S": "5",
    "T": "7",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "><",
    "Y": "¥",
    "Z": "2",
    // Letras minúsculas
    "a": "4",
    "b": "8",
    "c": "(C)",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "|-|",
    "i": "1",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "|\\/|",
    "n": "|\\\|",
    "o": "0",
    "p": "|*",
    "q": "0",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "¥",
    "z": "2",
    //números
    '1': "L",
    '2': "R",
    '3': "E",
    '4': "A",
    '5': "S",
    '6': "b",
    '7': "T",
    '8': "B",
    '9': "g",
    '0': "O",
};

function changeLetters(sentence) {
    let textChanged = sentence.replace(/[a-zA-Z0-9]/g, (c) => diccionarioLeet[c])
    return console.log(textChanged);
}
let sentence = 'Hola mundo en 2023'
changeLetters(sentence)