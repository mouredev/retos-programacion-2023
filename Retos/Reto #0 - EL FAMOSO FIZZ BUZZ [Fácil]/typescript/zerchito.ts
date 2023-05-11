/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const MAX = 100;
const MIN = 1;
function fizzbuzz(): void {
  for(let num = MIN; num<=MAX; num++){
    let response = '';
    if ( num%3 ===0 ) {
      response = 'fizz';
    }
    if ( num%5 === 0 ) {
      response = response + 'buzz';
    }
    console.log(response || num);
  }
}

fizzbuzz();
