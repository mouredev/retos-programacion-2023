/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leetConversor = (string:string) => {
    const leetAlphabet = ["4", "l3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "[V]", "^/", "0",
    "|*", "(,)", "l2", "5", "7", "(_)", "\/", "\/\/", "><", "j", "2"];
    
    const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"];

    const phrase:string = string.toLowerCase();
    let phraseConverted:string = "";

    for (let i = 0; i < string.length; i++) {
        for (let j = 0; j < alphabet.length; j++) {
            if (phrase[i] === alphabet[j]) {
                phraseConverted += leetAlphabet[j]
            }else if (phrase[i] === " ") {
                phraseConverted += " ";
            }
        }
        
    };

    return phraseConverted;
};

leetConversor("Gracias Mouredev");
