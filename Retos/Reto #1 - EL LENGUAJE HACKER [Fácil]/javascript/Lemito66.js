/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const transform_to_language_hacker = (word) => {
  let objectOfWords = {
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
    1: "L",
    2: "R",
    3: "E",
    4: "A",
    5: "5",
    6: "b",
    7: "T",
    8: "B",
    9: "g",
    0: "0",
  };
  let finally_word = ""
  for (const iterator of word) {
    if (iterator.toLowerCase() && Object.keys(objectOfWords).includes(iterator.toLowerCase())) {
        finally_word += objectOfWords[iterator.toLowerCase()]
    } else {
        finally_word += iterator
    }
  }
  return finally_word
};

console.log(transform_to_language_hacker('Lemito66'));
//13/\/\/17066
