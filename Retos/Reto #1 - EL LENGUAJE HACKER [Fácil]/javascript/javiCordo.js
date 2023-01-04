//
// javiCordo.js
//
//
//  Created by Javier Alejandro Cordovés Almaguer on 03/01/23.

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

let text = "Un hola mundo! de tipo leet";
let newText = "";

const dictLeet = {
  a: "4",
  b: "l3",
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
};

/**
 *
 * @param word
 * @returns Clean sign text
 */
function normalize(word) {
  let newWord = word.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "");
  return newWord.replace(/\s{2,}/g, " ");
}

/**
 *
 * @param text
 * @description Change normal text to leet text
 */
function changeToLeet(text) {
  for (let word of normalize(text)) {
    if (word === " ") newText += " ";
    else newText += dictLeet[word];
  }
  console.log(newText);
}

changeToLeet(text);
