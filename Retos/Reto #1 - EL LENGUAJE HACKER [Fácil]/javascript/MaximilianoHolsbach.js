/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leet = {
  a: 4,
  b: 8,
  c: "<",
  d: "|)",
  e: 3,
  f: "|=",
  g: 6,
  h: "(-)",
  i: "|",
  j: "]",
  k: ">|",
  l: 1,
  m: "^^",
  n: "^",
  o: 0,
  p: "|º",
  q: 9,
  r: "|^",
  s: 5,
  t: 7,
  u: "(_)",
  v: "u",
  w: "uu",
  x: "><",
  y: "`/",
  z: 7,
  " ": " ",
};// Generamos un diccionario para asignarle valores al alfabeto

let newText = ""; // Inicializamos una variable para concatenar los valores a codificar
function hacker(texto) {
  let minuscula = texto.toLocaleLowerCase(); // Normalizamos cualquier texto a minuscula
  for (let i = 0; i < minuscula.length; i++){ // Iteramos el texto
    for (let k in leet) { // Iteramos el diccionario
      if (minuscula[i] == k) { // Comprobamos si el caracter es igual a la clave
        let nuevo = leet[k]; // Asignamos el valor de la clave a una variable
        newText += nuevo; // Concatenamos los valores en la variable global
      }
    }
  }
  return newText;
}

console.log(
  hacker(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  )
);
