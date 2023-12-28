const entrada = "6-666-88-777-33-3-33-888";
const plantilla = {
  2: "ABC",
  3: "DEF",
  4: "GHI",
  5: "JKL",
  6: "MNO",
  7: "PQRS",
  8: "TUV",
  9: "WXYZ",
};

const process = (entrada) => {
  const entradaSplit = entrada.split("-");
  let result = "";
  for (const n of entradaSplit) {
    result += plantilla[n[0]][n.length - 1];
  }
  return result;
};

console.log(process(entrada));
