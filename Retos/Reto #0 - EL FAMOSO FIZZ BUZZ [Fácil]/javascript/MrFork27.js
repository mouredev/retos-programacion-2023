/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const NUM_LIST_LENGTH = 100;

for (let i = 1; i <= NUM_LIST_LENGTH; i++) {
    let is3Multiple = i % 3 === 0;
    let is5Multiple = i % 5 === 0;
    let isFullMultiple = is3Multiple && is5Multiple;

    if (isFullMultiple) {
        console.log("fizzbuzz");
    } else if (is3Multiple) {
        console.log("fizz");
    } else if (is5Multiple) {
        console.log("buzz");
    } else {
        console.log(i);
    }
}
