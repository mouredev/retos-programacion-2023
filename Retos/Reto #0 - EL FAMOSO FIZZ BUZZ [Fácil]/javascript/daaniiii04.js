/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

// Creación de la función, con numero para declarar el rango
function fizzbuzz() {
  for (let i = 1; i <= 100; i++) {
    i % 15 === 0
      ? console.log("fizzbuzz")
      : i % 5 === 0
      ? console.log("buzz")
      : i % 3 === 0
      ? console.log("fizz")
      : console.log(i);
  }
}

// llamada de la función
fizzbuzz();


// @author Daniel Marín || Solución para el Reto #0 - EL FAMOSO FIZZ BUZZ [Fácil]