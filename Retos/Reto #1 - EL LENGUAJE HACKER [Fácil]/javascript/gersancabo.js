/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const DictionaryNormal2Leet = {
    a: "4",
    b: "I3",
    c: "[",
    d: ")",
    e: "3",
    f: "|=",
    g: "&",
    h: "#",
    i: "1",
    j: ",_|",
    k: ">|",
    l: "1",
    m: "/\\/\\",
    n: "^/",
    o: "0",
    p: "|*",
    q: "(_,)",
    r: "I2",
    s: "5",
    t: "7",
    u: "(_)",
    v: "\\/",
    w: "\\/\\/",
    x: "><",
    y: "j",
    z: "2",
    0: "o",
    1: "L",
    2: "R",
    3: "E",
    4: "A",
    5: "S",
    6: "b",
    7: "T",
    8: "B",
    9: "g"
}

/**
 * Transform a normal text in leet text
 * 
 * @param {string} textInput normal text
 * @returns {string} textOutput leet text
 */
function normal2leet(textInput) {
    let textOutput = "";
    textInput = textInput.toLowerCase();
    for (let i = 0; i < textInput.length; i++) {
        let textCharacter = textInput.charAt(i)
        let leetCharacter = DictionaryNormal2Leet[textCharacter];
        if (leetCharacter != undefined) {
            textCharacter = leetCharacter
        }
        textOutput += textCharacter;
    }
    return textOutput;
}

/**
 * Ask for a text to convert to leet alphabet
 */
function askAText() {
    let textInput = "";
    rl.question("Escribe tu texto:\n", function (answer) {
        textInput = answer;
        console.log(normal2leet(textInput));
        rl.close();
    });
}

askAText();