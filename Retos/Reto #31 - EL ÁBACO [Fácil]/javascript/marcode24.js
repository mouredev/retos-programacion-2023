/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */

const getNumber = (abacus) => {
  let number = 0;
  const abacusLength = abacus.length;

  for (let rowIndex = 0; rowIndex < abacusLength; rowIndex++) {
    const row = abacus[rowIndex];
    if (!/^[^-]*-{3}[^-]*$/.test(row) || row.length !== 12) {
      number = 'Invalid abacus';
      break;
    }
    number += row.split('---')[0].length * (10 ** (abacusLength - rowIndex - 1));
  }
  return number.toLocaleString('en-US');
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
