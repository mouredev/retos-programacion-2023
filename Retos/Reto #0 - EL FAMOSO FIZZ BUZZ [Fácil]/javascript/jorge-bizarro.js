/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

for (let valueNumber = 1; valueNumber <= 100; valueNumber++) {
  let valueToPrint = '';

  if (valueNumber % 3 === 0)
    valueToPrint += 'Fizz';

  if (valueNumber % 5 === 0)
    valueToPrint += 'Buzz';

  valueToPrint ||= valueNumber;

  console.log(valueToPrint);
}
