/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

function getColNumber(colname) {
  let result = 0
  for(const i in colname) {
    let jump = 26 ** ((colname.length - 1) - i);
    result += (colname.charCodeAt(i) - 64) * jump; 
  }
  return result;
}

console.log(getColNumber('A')) // 1
console.log(getColNumber('Z')) // 26
console.log(getColNumber('AA')) // 27
console.log(getColNumber('CA')) // 79
console.log(getColNumber('HA')) // 209
console.log(getColNumber('ABC')) // 731
console.log(getColNumber('AAK')) // 713
console.log(getColNumber('GHE')) // 713
console.log(getColNumber('XFD')) // 16384

// @by npminit-dev