/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

// Optimizado 💅🏼
for (let i = 0; i <= 100; i++) {
    const isFizz = i % 3 === 0;
    const isBuzz = i % 5 === 0;
    console.log(isFizz && isBuzz ? "fizzbuzz" : isFizz ? "fizz" : isBuzz ? "buzz" : i);
}
