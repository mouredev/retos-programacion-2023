/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
const fizzBuzz = (number: number): string => {
  const isFizz = number % 3 === 0;
  const isBuzz = number % 5 === 0;
  const isFizzBuzz = isFizz && isBuzz;

  if (isFizzBuzz) {
    return 'FizzBuzz';
  }

  if (isFizz) {
    return 'Fizz';
  }

  if (isBuzz) {
    return 'Buzz';
  }

  return number.toString();
}
// Create range from 1 to 100
const numbers: Array<number> = Array.from(Array(100).keys()).map(n => n + 1);
// Iterate over list
const fizzBuzzList: Array<string> = numbers.map(number => fizzBuzz(number));
console.log(fizzBuzzList.join('\n'));