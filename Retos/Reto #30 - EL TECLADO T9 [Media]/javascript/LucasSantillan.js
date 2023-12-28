const teclado = {
  "0": " ",
  "2": "A",
  "22": "B",
  "222": "C",
  "3": "D",
  "33": "E",
  "333": "F",
  "4": "G",
  "44": "H",
  "444": "I",
  "5": "J",
  "55": "K",
  "555": "L",
  "6": "M",
  "66": "N",
  "666": "O",
  "7": "P",
  "77": "Q",
  "777": "R",
  "7777": "S",
  "8": "T",
  "88": "U",
  "888": "V",
  "9": "W",
  "99": "X",
  "999": "Y",
  "9999": "Z"
};

function t9(mensaje) {
  let decodMensaje = mensaje.split('-');
  let resuldato = '';
  decodMensaje.forEach(valor => {
    if (teclado[valor]) {
      resuldato += teclado[valor];
    }
  });
  return resuldato;
}

console.log(t9('7777-666-999-0-555-88-222-2-7777'));
console.log(t9('6-666-88-777-33-3-33-888'));
