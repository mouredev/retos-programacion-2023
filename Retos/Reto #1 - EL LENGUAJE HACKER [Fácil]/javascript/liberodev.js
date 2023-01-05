/*
    Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    se caracteriza por sustituir caracteres alfanuméricos.
        - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
        con el alfabeto y los números en "leet".
        (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

let dictionaryLeet = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"1",
    "m":"/\\/\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q": "(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\\/",
    "w":"\\/\\/",
    "x":"><",
    "y":"j",
    "z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"5",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"0"
}

function encripterToLeet (text){
    let len = text.length;
    let encryptedText = "";

    for (var i = 0; i < len; i++) {
        if (text.charAt(i) in dictionaryLeet)
            encryptedText += dictionaryLeet[text.charAt(i)]
        else
            encryptedText += text.charAt(i)
    }
    
    return encryptedText
}

let text = prompt("Introduce el texto a \"hackear\": ").toLowerCase();

console.log(text);
console.log(encripterToLeet(text));