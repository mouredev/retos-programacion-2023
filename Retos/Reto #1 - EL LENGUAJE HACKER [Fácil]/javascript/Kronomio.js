
const dictionary = {
  A: "4",
  B: "I3",
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
  R: "I2",
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
function traducir (texto){
  return texto.toUpperCase()
  .split('')
  .map((letra)=>dictionary[letra])
  .join('');
}

const traducirTexto=texto =>{
  return texto
    .toUpperCase()
    .split("")
    .map((letra) => dictionary[letra]||letra)
    .join("");
}
const textoEntrada="Texto de prueba de traduccion 123456";

console.log('Texto original:', textoEntrada);
console.log('Traducción:', traducirTexto(textoEntrada));
