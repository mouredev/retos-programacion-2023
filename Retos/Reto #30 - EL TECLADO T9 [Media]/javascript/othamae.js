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

const T9 = {
    0: ' ',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

const pulseTranslation = (pulsations) => {
    let result = ''
    const numbers = pulsations.split('-')
    for (let i = 0; i < numbers.length; i++) {
        const puls = numbers[i].length
        const letters = T9[numbers[i][0]].split('')
        result += letters[puls - 1]       
    }
      return result
}

console.log(pulseTranslation('6-666-88-777-33-3-33-888'))


console.log(pulseTranslation('666-8-44-2-6-2-33'))
