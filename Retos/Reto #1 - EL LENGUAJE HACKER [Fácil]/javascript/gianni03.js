// para la web se debe utilizar la linea comentada
// let input = prompt("Ingrese un texto: ");

// para que funcione por consola tengo el texto harcodeado
let input = "Hola, me llamo Gianni y tengo 43 añios porque naci en 1980."
let text = input.toLowerCase();


const leet = {
  a: "4",
  b: "I3",
  c: "[",
  d: "(",
  e: "3",
  f: "|=",
  g: "&",
  h: "#",
  i: "1",
  j: "_|",
  k: "|<",
  l: "1",
  m: "|v|",
  n: "^/",
  o: "0",
  p: "|*",
  q: "9",
  r: "I2",
  s: "5",
  t: "7",
  u: "(_)",
  v: "\/",
  w: "\/\/",
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
  0: "O"
}
console.log(leet);

function encript(text){
  let secretCode = "";
  console.log(text)

  for (letter of text){
    if (leet[letter]){
      console.log(leet[letter]);
      secretCode += leet[letter];
    } else {
      secretCode += letter;
    }
  }
return secretCode;
}

console.log(encript(text));