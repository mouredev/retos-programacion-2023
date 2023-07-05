/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *
 * NOTA Los caracteres que no estén en el alfabeto se mantienen igual
 */

const alphabet = {
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
  r: "|2",
  s: "5",
  t: "7",
  u: "(_)",
  v: "\\/",
  w: "\\/\\/",
  x: "><",
  y: "j",
  z: "2",
  1: "L",
  2: "R",
  3: "E",
  4: "A",
  5: "S",
  6: "b",
  7: "T",
  8: "B",
  9: "g",
  0: "o",
};

type KeyAlphabet = keyof typeof alphabet;

function transformCharacter(characterKey: string) {
  return alphabet[characterKey as KeyAlphabet];
}

function printTransformedText(text: string, textTranformed: string) {
  console.log(text, "=>", textTranformed);
}
function transformText(text: string = "") {
  const textTransformated = text
    .toLowerCase()
    .replace(/([a-z0-9])/g, (letter: string) => transformCharacter(letter));
  printTransformedText(text, textTransformated);
}

transformText("hola mundo 1344");
