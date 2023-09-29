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

const teclas = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

function T9(pulsaciones) {
    return pulsaciones.split('-').map(tecla => {
        const num = tecla.length
        return teclas[tecla[0]][num - 1]
    }).join('')
}


console.log(T9('6-666-88-777-33-3-33-888'))// MOUREDEV
console.log(T9('5-2-888-2-7777-222-777-444-7-8'))// MOUREDEV