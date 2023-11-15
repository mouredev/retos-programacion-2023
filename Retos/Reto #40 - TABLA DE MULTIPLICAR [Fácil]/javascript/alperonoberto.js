/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

const readline = require('readline-sync');

const table = readline.question('Choose a number to show its multiplication table: ');

for(let i = 1; i < 11; i++) {
    console.log(`${Number(table)} x ${i} = ${Number(table) * i}`);
}