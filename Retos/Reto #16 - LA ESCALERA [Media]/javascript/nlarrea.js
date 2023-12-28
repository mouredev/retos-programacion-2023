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

function drawStairs(stairs) {
    if (stairs > 0) {               // upward direction
        for (let stair = 0; stair <= stairs; stair++) {
            if (stair === 0) console.log(' '.repeat(stairs * 2) + '_');
            else console.log(' '.repeat((stairs - stair) * 2) + '_|');
        }
    } else if (stairs < 0) {        // downward direction
        stairs = Math.abs(stairs);
        for (let stair = 0; stair <= stairs; stair++) {
            if (stair === 0) console.log('_');
            else console.log(' '.repeat(stair * 2 - 1) + '|_');
        }
    } else if (stairs === 0) {       // flat
        console.log('__');
    }
}


drawStairs(4);
drawStairs(-4);
drawStairs(0);