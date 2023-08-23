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

function Ladder(num) {
    let latter = ''
    if (num === 0) {
        latter = '__'
    } else if (num > 0) {
        for (let i = 0; i < num; i++) {
            if (i === 0) {
                latter += ' '.repeat((num - i) * 2)
                latter += '_\n'
            }
            latter += ' '.repeat((num - i - 1) * 2)
            latter += '_'
            latter += '|\n'
        }

    } else {
        for (let i = 0; i > num; i--) {
            if (i === 0) {
                latter += '_\n'
            }
            latter += ' '.repeat(Math.abs(i) * 2 + 1)
            latter += '|'
            latter += '_\n'
        }
    }
    return latter
}


console.log(Ladder(7));
console.log(Ladder(-7));