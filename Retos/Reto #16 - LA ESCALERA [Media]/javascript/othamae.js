/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

function stairs(n) {
    let drawing = ''
    if (n === 0) return '__'

    if (n > 0) {
        drawing = ' '.repeat((n * 2) + 1) + '_' + '\n'
        for (let i = n; i >= 1; i--) {
            const stair = ' '.repeat((i * 2) - 1) + '_|' + '\n'
            drawing += stair
        }
    }

    if (n < 0) {
        drawing = '_' + '\n'
        for (let i = 1; i <= Math.abs(n); i++) {
            const stair = ' '.repeat((i * 2) - 1) + '|_' + '\n'
            drawing += stair
        }
    }
    return drawing;


}

const fourStairs = stairs(4)
console.log(fourStairs)
/** 
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
*/

const zeroStairs = stairs(0)
console.log(zeroStairs)
/**
 * __
 */

const fourNegStairs = stairs(-4)
console.log(fourNegStairs)

/** 
 * _
 *  |_
 *    |_
 *      |_
 *        |_
 * 
*/

