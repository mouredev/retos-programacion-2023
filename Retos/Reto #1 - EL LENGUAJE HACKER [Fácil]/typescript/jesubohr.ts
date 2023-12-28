const LEET_ALPHABET = {
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
  0: 'o',
  1: 'L',
  2: 'R',
  3: 'E',
  4: 'A',
  5: 'S',
  6: 'b',
  7: 'T',
  8: 'B',
  9: 'g',
}

function toLeetText(text: string) {
  return text
    .split('')
    .map(char => LEET_ALPHABET[char.toLowerCase()] ?? char)
    .join('')
}

console.log(toLeetText('Hello World!'))
