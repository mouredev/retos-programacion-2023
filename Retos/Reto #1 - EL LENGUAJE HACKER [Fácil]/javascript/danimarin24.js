/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function leet(txt) {
  txt = txt.toUpperCase();

  const leet_alphabet = {
    A: "4",
    B: "l3",
    C: "[",
    D: ")",
    E: "3",
    F: "|=",
    G: "&",
    H: "#",
    I: "1",
    J: ",_|",
    K: ">|",
    L: "1",
    M: "/\\/\\",
    N: "^/",
    O: "0",
    P: "|*",
    Q: "(_,)",
    R: "l2",
    S: "5",
    T: "7",
    U: "(_)",
    V: "\\/",
    W: "\\/\\/",
    X: "><",
    Y: "j",
    Z: "2",
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

  let leet_txt = txt.split("");

  for (let i = 0; i < leet_txt.length; i++) {
    if (leet_alphabet[leet_txt[i]]) {
      leet_txt[i] = leet_alphabet[leet_txt[i]];
    }
  }
  return leet_txt.join("");
}

let txt = "¡Hola Brais! Esto es un mensaje de prueba";
const x = leet(txt);

console.log("Original: " + txt);
console.log("Hacker " + x);

// @author Daniel Marín || Solución para el Reto #1 - EL LENGUAJE HACKER [Fácil]
