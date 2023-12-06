/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
const assert = require('assert')
function friday13(year, month) {
  const date = new Date(year, month - 1, 13);
  return date.getDay() === 5;
}

const testValues = [true, false, false, false, false, false, false, false, false, true, false, false];
for (let i = 1; i <= testValues.length; i++) {
  assert(friday13(2023, i) === testValues[i - 1], `Expected month ${i} to ${testValues[i - 1] ? '' : 'not '}have a Friday 13`)
}

