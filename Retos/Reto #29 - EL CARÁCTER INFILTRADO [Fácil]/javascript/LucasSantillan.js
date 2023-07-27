function comparador(cadena1, cadena2) {
  let encontrados = [];
  let contador = 0;

  for (let i = 0; i < cadena1.length; i++) {
    if (cadena1[i] != cadena2[i]) {
      encontrados[contador] = cadena2[i];
      contador++;
    }
  }
  return encontrados;
}

console.log(comparador('Me llamo mouredev', 'Me llemo mouredov'));
console.log(comparador('Me llamo.Brais Moure', 'Me llamo brais moure'));
