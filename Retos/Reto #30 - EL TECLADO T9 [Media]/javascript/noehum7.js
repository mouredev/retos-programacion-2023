function conversionT9(cadena) {
  map = { 
  2: "ABC",
  3: "DEF",
  4: "GHI",
  5: "JKL",
  6: "MNO",
  7: "PQRS",
  8: "TUV",
  9: "WXYZ",
  } 
  const cadenaArray = cadena.split("-");
  const resultado = cadenaArray.map(pulsacion => map[pulsacion.charAt(0)]?.charAt(pulsacion.length - 1)).join("").toLowerCase();
  return resultado;
}

console.log(conversionT9("6-666-88-777-33-3-33-888"));
