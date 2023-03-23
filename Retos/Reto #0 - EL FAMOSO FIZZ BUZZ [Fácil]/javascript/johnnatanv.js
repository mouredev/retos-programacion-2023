/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const fizzbuzz = (num) => {
  for (let print = 1; num >= print; print++) {
    if (print % 3 === 0 && print % 5 === 0) console.log("fizzbuzz");
    else if (print % 3 === 0) console.log("fizz");
    else if (print % 5 === 0) console.log("buzz");
    else console.log(print);
  }
};

const maxNum = 100;

fizzbuzz(maxNum);

// Github @JohnnatanV
