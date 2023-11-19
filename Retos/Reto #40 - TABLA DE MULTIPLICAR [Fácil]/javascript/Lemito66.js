/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

const multiplicationTable = (number, stop) => {
    for (let i = 1; i <= stop; i++) {
        console.log(`${number} x ${i} = ${number * i}`);
    }
};

console.log(multiplicationTable(5, 30));