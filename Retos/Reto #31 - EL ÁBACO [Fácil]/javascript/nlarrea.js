/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */

function abacusNumber(array) {
    if (array.length !== 7) {
        return 'Error: Abacus must have a length of 6 digits.';
    }

    if (array.some(digit => digit.length !== 12 || digit.split('0').length !== 10)) {
        return 'Wrong number definition in abacus!';
    }

    const numbers = array.map(digit => digit.split('---')[0].length);
    const number = new Intl.NumberFormat('es-ES').format(numbers.join(''));
    return number;
}


const numberArray = [
    '0---00000000',
    '000---000000',
    '---000000000',
    '00---0000000',
    '0000000---00',
    '000000000---',
    '---000000000'
];

console.log(abacusNumber(numberArray));     // 1.302.790