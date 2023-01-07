/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const LEET_CHARS = {
  a: '4',
  b: 'I3',
  c: '[',
  d: ')',
  e: '3',
  f: '|=',
  g: '&',
  h: '#',
  i: '1',
  j: ',_|',
  k: '>|',
  l: '1',
  m: '/\\/\\',
  n: '^/',
  o: '0',
  p: '|*',
  q: '(_,)',
  r: 'I2',
  s: '5',
  t: '7',
  u: '(_)',
  v: '\\/',
  w: '\\/\\/',
  x: '><',
  y: 'j',
  z: '2',
  1: 'L',
  2: 'R',
  3: 'E',
  4: 'A',
  5: 'S',
  6: 'b',
  7: 'T',
  8: 'B',
  9: 'g',
  0: 'o'
};

const convertNaturalToLeet = ( natural:string ):string => {
  return natural
          .toLowerCase()
          .replace(
            /[abcdefghijklmnopqrstuvwxyz1234567890]/g, 
            (m) => LEET_CHARS[m]
          );
}

const NaturalString:string = 'SamsarDev01052023';
const LeetString:string = convertNaturalToLeet(NaturalString);

console.log(`Lenguaje Natural: ${NaturalString}`);
console.log(`Lenguaje Leet: ${LeetString}`);