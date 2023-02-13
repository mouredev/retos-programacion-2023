/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const fizzBuzz = () => {
  let result = '';
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      result += 'FizzBuzz';
    } else if (i % 3 === 0) {
      result += 'Fizz';
    } else if (i % 5 === 0) {
      result += 'Buzz';
    } else {
      result += i;
    }
    result += '\n';
  }
  return result.trim();
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges