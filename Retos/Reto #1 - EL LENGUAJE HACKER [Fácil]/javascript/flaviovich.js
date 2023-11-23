/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

console.clear();

const toLeet = (text) => {
  if (text === null || text === undefined || text.length === 0) return "";

  const leet = [
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
    "^^",
    "^/",
    "0",
    "|*",
    "(_,)",
    "|2",
    "5",
    "7",
    "(_)",
    "|/",
    "'//",
    "><",
    "j",
    "2",
  ];
  const numbers = ["o", "L", "R", "E", "A", "S", "b", "T", "B", "g"];
  let index;

  return text
    .split("")
    .map((element) => {
      index = element.toUpperCase().charCodeAt(0) - 65;
      return leet[index]
        ? leet[index]
        : isNaN(parseInt(element))
        ? element
        : numbers[element];
    })
    .join("");
};

console.log(toLeet("Hola, soy Flavio, tengo 25 años"));
console.log(toLeet(null));
console.log(toLeet("¡Hola! ¿Cómo estás?"));
