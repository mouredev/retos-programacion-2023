  let lenguaje = {
  "a": "4",
  "b": "I3",
  "c": "[",
  "d": ")", 
  "e": "3",
  "f": "|=",
  "g": "&",
  "h": "#",
  "i": "1",
  "j": ",_|",
  "k": ">|",
  "l": "1",
  "m": "JVI",
  "n": "^/",
  "o": "0",
  "p": "|*",
  "q": "(_,)",
  "r": "I2",
  "s": "5",
  "t": "7",
  "u": "(_)",
  "v": "\/",
  "w": "\/\/",
  "x": "><",
  "y": "j",
  "z": "2"
}



function hacker(texto) {
  let ret = "";
  for (palabra of texto) {
    let minuscula = palabra.toLowerCase();
    ret += lenguaje[minuscula]
  }   
  return ret
}

hacker("LenguajeHacker")
