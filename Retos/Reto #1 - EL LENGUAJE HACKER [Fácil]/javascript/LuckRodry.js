/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leetLetters = {
    a:"4",
    b:"I3",
    c:"[",
    d:")",
    e:"3",
    f:"|=",
    g:"&",
    h:"#",
    i:"1",
    j:",_|",
    k:">|",
    l:"1",
    m:"/\\/\\",
    n:"^/",
    o:"0",
    p:"|*",
    q:"(_,)",
    r:"I2",
    s:"5",
    t:"7",
    u:"(_)",
    v:"|/",
    w:"Ш",
    x:"><",
    y:"j",
    z:"2",
    0:"L",
    1:"R",
    2:"E",
    3:"A",
    4:"S",
    5:"b",
    6:"T",
    7:"B",
    8:"g",
    9:"o"
}



function translator(text)
{
    let HackerText = "";
    for (let i = 0; i < text.length; i++) {
        if (leetLetters[text[i].toLowerCase()]) {
            HackerText+=leetLetters[text[i].toLowerCase()];
        }else{
            HackerText+=text[i];
        }
        
    }
    return HackerText;
}

console.log(translator("Reto Semanal 1"));