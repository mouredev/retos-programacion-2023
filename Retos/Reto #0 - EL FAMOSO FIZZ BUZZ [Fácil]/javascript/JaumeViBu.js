/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const fizzbuzz = (val) => {

  let res = '';
  const isMultipleOf3 = val % 3 == 0;
  const isMultipleOf5 = val % 5 == 0;

  res += isMultipleOf3 ? 'fizz' : '';
  res += isMultipleOf5 ? 'buzz' : '';
  res += res == '' ? val : '';

  return res;
}

const printFizzbuzzFromTo = (startVal, endVal, step) => {

  let output = [];

  for (let i = startVal; i <= endVal; i += step) {
    output.push(`${fizzbuzz(i)}\n`);
  }

  console.log(output.join(''));
}

printFizzbuzzFromTo(1, 100, 1);