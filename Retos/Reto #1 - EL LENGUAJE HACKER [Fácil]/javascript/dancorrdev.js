let message = prompt("Ingrese su texto aqui");
const leetDictionary = {
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
  l: "£",
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
  " ": " ",
};
console.log(hackerTranslator(message));
function hackerTranslator(message) {
  let messageTraslated = "";
  for (let i = 0; i < message.length; i++) {
    let letter = message[i].toLowerCase();
    if (letter in leetDictionary) {
      messageTraslated += leetDictionary[letter];
    } else {
      messageTraslated += message[i];
    }
  }
  return messageTraslated;
}
