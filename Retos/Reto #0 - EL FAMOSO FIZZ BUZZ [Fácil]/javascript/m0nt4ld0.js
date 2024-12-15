/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
let fizz = 0;
let buzz = 0;

for (let i = 1; i <= 100; i++) {
  fizz++;
  buzz++;

  console.log(fizz === 3 && buzz === 5 ? "fizzbuzz" : fizz === 3 ? "fizz" : buzz === 5 ? "buzz" : i);
  
  if (fizz === 3) fizz = 0;
  if (buzz === 5) buzz = 0; 
}
