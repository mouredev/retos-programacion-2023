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

const tupla = [
    ['a','b','c'],['d','e','f'],
    ['g','h','i'],['j','k','l'],['m','n','o'],
    ['p','q','r','s'],['t','u','v'],['w','x','y','z']
]

const celularT9 = (word) =>{
    const separatorChar = word.split('-')

    let traslateWord = []
    separatorChar.forEach((number)=>{
        const transformNumber = parseInt(number.split('')[0])
        traslateWord.push(tupla[transformNumber-2][number.length-1])
    })
    return traslateWord.join('')
}
console.log(celularT9('6-666-88-777-33-3-33-888'))