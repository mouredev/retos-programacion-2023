'use strict';
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
(() => {
  let i = 1;
  while (i <= 100) {
    if (i % 5 === 0 && i % 3 === 0) console.log('fizzbuzz');
    else if (i % 5 === 0) console.log('buzz');
    else if (i % 3 === 0) console.log('fizz');
    else console.log(i);
    i++;
  }
})();
