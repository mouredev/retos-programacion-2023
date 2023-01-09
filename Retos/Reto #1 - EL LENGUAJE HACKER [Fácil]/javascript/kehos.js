/*
 * Reto #1 - El lenguaje hacker
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 03/01/2023
 */

const characterMapping = {
  a: '4',
  'á': '4',
  b: 'I3',
  c: '[',
  d: ')',
  e: '3',
  'é': '3',
  f: '|=',
  g: '&',
  h: '#',
  i: '1',
  'í': '1',
  j: ',_|',
  k: '>|',
  l: '1',
  m: '/\\/\\',
  n: '^/',
  o: '0',
  'ó': '0',
  p: '|*',
  q: '(_,)',
  r: 'I2',
  s: '5',
  t: '7',
  u: '(_)',
  'ú': '(_)',
  v: '\\/',
  w: '\\/\\/',
  x: '><',
  y: 'j',
  z: '2',
  '1': 'L',
  '2': 'R',
  '3': 'E',
  '4': 'A',
  '5': 'S',
  '6': 'b',
  '7': 'T',
  '8': 'B',
  '9': 'g',
  '0': 'o',
};

// Test string
const text = 'El veloz murciélago hindú comía cardillo y kiwi';

// Return text converting all its characters to L33T SP34K
function convertText(textToConvert = text) {
  let resultText = '';
  for (let char of textToConvert.toLowerCase()) {
    resultText += characterMapping[char] || char;
  }
  return resultText;
}

console.log(convertText());
