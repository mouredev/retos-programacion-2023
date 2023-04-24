/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leet = [
  "4",
  "l3",
  "[",
  ")",
  "3",
  "|=",
  "&",
  "#",
  "1",
  ",_l",
  ">|",
  "1",
  "/\\/\\",
  "^/",
  "0",
  "|*",
  "(_,)",
  "l2",
  "5",
  "7",
  "|_|",
  "\\/",
  "\\/\\/",
  "><",
  "`/",
  "2",
];

function transformar(palabra) {
  let arreglo = palabra.toLowerCase().split("");
  const resultado = arreglo.map((e) => {
    return e
      .replace(/a/g, leet[0])
      .replace(/b/g, leet[1])
      .replace(/c/g, leet[2])
      .replace(/d/g, leet[3])
      .replace(/e/g, leet[4])
      .replace(/f/g, leet[5])
      .replace(/g/g, leet[6])
      .replace(/h/g, leet[7])
      .replace(/i/g, leet[8])
      .replace(/j/g, leet[9])
      .replace(/k/g, leet[10])
      .replace(/l/g, leet[11])
      .replace(/m/g, leet[12])
      .replace(/n/g, leet[13])
      .replace(/o/g, leet[14])
      .replace(/p/g, leet[15])
      .replace(/q/g, leet[16])
      .replace(/r/g, leet[17])
      .replace(/s/g, leet[18])
      .replace(/t/g, leet[19])
      .replace(/u/g, leet[20])
      .replace(/v/g, leet[21])
      .replace(/w/g, leet[22])
      .replace(/x/g, leet[23])
      .replace(/y/g, leet[24])
      .replace(/z/g, leet[25]);
  });
  console.log(resultado.join(""));
}

transformar("mouredev");
