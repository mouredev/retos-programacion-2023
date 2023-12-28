/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

const keyPadMap = new Map([
    ['2', 'ABC'],
    ['3', 'DEF'],
    ['4', 'GHI'],
    ['5', 'JKL'],
    ['6', 'MNO'],
    ['7', 'PQRS'],
    ['8', 'TUV'],
    ['9', 'WXYZ'],
    ['0', ' '],
  ]);

function evaluate(expression) {
    let decoded = '';
    if (typeof expression !== 'string') {
        throw new Error(`Invalid input: ${expression}`);
    }

    const chars = expression.split('-');
    for (const char of chars) {
        if (isValidSequence(char)) {
            decoded += multitapDecode(char);
        } else {
            throw new Error(`Found Invalid sequence: ${char}`);
        }
    }
    return decoded;
}
  
function isValidSequence(input){
    const sequenceRegex = /^(\d)\1*$/;
    return sequenceRegex.test(input);
}

function multitapDecode(sequence){
    let decoded = '';
    if (keyPadMap.has(sequence[0])) {
        const mapValueSplitted = keyPadMap.get(sequence[0]).split('');
        decoded = mapValueSplitted.length >= sequence.length ? 
                    mapValueSplitted[sequence.length-1] : 
                    '?';
    } else {
        throw new Error(`Invalid character: ${sequence[0]}`);
    }
    return decoded;
}

// Test cases

console.log(evaluate('2-22-222')); // Output: ABC
console.log(evaluate('999-444-33')); // Output: YIE
console.log(evaluate('2-ccc-3')); // Output: Found Invalid sequence
console.log(evaluate('7-111')); // Output: Invalid character
console.log(evaluate('2-3333-44')); // Output: A?H
console.log(evaluate(33)); // Output: Invalid input