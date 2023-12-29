/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */


const printTable = table => {
    for (let row of table) {
        console.log(row);
    }
};


const multiplicationTable = number => {
    // Check if data is correct
    if (typeof number !== 'number') {
        console.log('The given data must be a number!');
    } else if (number < 0) {
        console.log('The given number must be positive!');
    }

    // Get the table
    const min = 1;
    const max = 10;
    const table = Array.from({length: max-min+1}, (_, idx) => `${number} x ${idx + min} = ${number * (idx + min)}`);
    printTable(table);
};


multiplicationTable(5);