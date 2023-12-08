/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

for (numero = 1; numero <= 100; numero++) {
    if ((numero % 3) == 0 && (numero % 5) == 0) {
        console.log("FizzBuzz");
    } else if ((numero % 3) == 0) {
        console.log("Fizz");
    } else if ((numero % 5) == 0) {
        console.log("Buzz");
    } else {
        console.log(numero);
    }
}

// Reto #0 - EL FAMOSO FIZZ BUZZ || Resuelto por: https://github.com/Ramizdo
