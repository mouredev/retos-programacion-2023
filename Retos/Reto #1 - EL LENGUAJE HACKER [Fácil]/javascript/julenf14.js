/*
  Escribe un programa que reciba un texto y transforme lenguaje natural a
  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
   se caracteriza por sustituir caracteres alfanuméricos.
  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

const caracteresNatural = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];

const caracteresHacker = [
  "4",
  "I3",
  "[",
  ")",
  "3",
  "|=",
  "&",
  "#",
  "1",
  ",_|",
  ">|",
  "1",
  "/\\/\\",
  "^/",
  "0",
  "|*",
  "(_,)",
  "I2",
  "5",
  "7",
  "(_)",
  "/",
  "//",
  "><",
  "j",
  "2",
];

console.log(lenguajeLeet("Hola mundo"));

function lenguajeLeet(texto) {
  let textoLeet = "";

  for (let i = 0; i < texto.length; i++) {
    let letra = texto.substr(i, 1);
    let posicionLetra = caracteresNatural.indexOf(letra.toUpperCase());
    if (posicionLetra >= 0) {
      textoLeet += caracteresHacker[posicionLetra];
    } else {
      textoLeet += letra;
    }
  }

  return textoLeet;
}
