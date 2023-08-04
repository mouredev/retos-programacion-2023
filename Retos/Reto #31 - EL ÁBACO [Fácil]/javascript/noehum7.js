function transformarAbaco(arr) {
  const resultado = arr.map(cuenta => cuenta.split("---")[0].length);
  return Number(resultado.join(""));
}

const arr = ["O---OOOOOOOO",
   "OOO---OOOOOO",
   "---OOOOOOOOO",
   "OO---OOOOOOO",
   "OOOOOOO---OO",
   "OOOOOOOOO---",
   "---OOOOOOOOO"];

transformarAbaco(arr);
