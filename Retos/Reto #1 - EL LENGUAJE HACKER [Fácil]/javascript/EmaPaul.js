/*
Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanuméricos.
Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

*/

function hackerLanguage(text) {
  let arrText = text.split("");
  let textHack = [];
  for (let i = 0; i < arrText.length; i++) {
    if (arrText[i] === "a" || arrText[i] == "A") {
      arrText[i] = "4";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "b" || arrText[i] == "B") {
      arrText[i] = "I3";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "c" || arrText[i] == "C") {
      arrText[i] = "[";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "d" || arrText[i] == "D") {
      arrText[i] = ")";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "e" || arrText[i] == "E") {
      arrText[i] = "3";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "f" || arrText[i] == "F") {
      arrText[i] = "|=";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "g" || arrText[i] == "G") {
      arrText[i] = "&";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "h" || arrText[i] == "H") {
      arrText[i] = "#";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "i" || arrText[i] == "I") {
      arrText[i] = "1";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "j" || arrText[i] == "J") {
      arrText[i] = ",_|";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "k" || arrText[i] == "K") {
      arrText[i] = ">|";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "l" || arrText[i] == "L") {
      arrText[i] = "1";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "m" || arrText[i] == "M") {
      arrText[i] = "/\\/\\";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "n" || arrText[i] == "N") {
      arrText[i] = "^/";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "ñ" || arrText[i] == "Ñ") {
      arrText[i] = "ñ";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "o" || arrText[i] == "O") {
      arrText[i] = "0";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "p" || arrText[i] == "P") {
      arrText[i] = "|*";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "q" || arrText[i] == "Q") {
      arrText[i] = "(_,)";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "r" || arrText[i] == "R") {
      arrText[i] = "I2";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "s" || arrText[i] == "S") {
      arrText[i] = "5";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "t" || arrText[i] == "T") {
      arrText[i] = "7";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "u" || arrText[i] == "U") {
      arrText[i] = "(_)";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "v" || arrText[i] == "V") {
      arrText[i] = "/";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "w" || arrText[i] == "W") {
      arrText[i] = "\\/\\/";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "x" || arrText[i] == "X") {
      arrText[i] = "><";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "y" || arrText[i] == "Y") {
      arrText[i] = "j";
      textHack.push(arrText[i]);
    } else if (arrText[i] == "z" || arrText[i] == "Z") {
      arrText[i] = "2";
      textHack.push(arrText[i]);
    } else if (typeof arrText[i] == "string") {
      textHack.push(arrText[i]);
    }
  }
  return textHack.join("");
}

console.log(hackerLanguage("leet"));
