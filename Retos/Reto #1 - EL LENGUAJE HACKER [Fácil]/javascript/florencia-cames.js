/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const hackerText = {
  A: "4",
  B: "8",
  C: "(",
  D: "|)",
  E: "3",
  F: "|=",
  G: "6",
  H: "|-|",
  I: "1",
  J: "_|",
  K: "|<",
  L: "1",
  M: "|\\/|",
  N: "|\\|",
  O: "0",
  P: "|2",
  Q: "(,)",
  R: "|2",
  S: "5",
  T: "7",
  U: "|_|",
  V: "\\/",
  W: "\\/\\/",
  X: "><",
  Y: "`/",
  Z: "2",
};

const hackerTranslate = (text) => {
  let result = "";
  for (let index = 0; index < text.length; index++) {
    let char = text.charAt(index).toUpperCase();
    if (hackerText[char]) {
      result += hackerText[char];
    } else {
      result += char;
    }
  }
  return result;
};

console.log(hackerTranslate("Hello World!"));
