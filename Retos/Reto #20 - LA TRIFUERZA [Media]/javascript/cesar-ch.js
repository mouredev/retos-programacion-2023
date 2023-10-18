/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

 function drawTrifuerza(n) {
    let trifuerza = ''

    for (let i = 0; i < 2 * n; i++) {
        if (i < n) {
            trifuerza += ' '.repeat(((2 * n) - 1) - i)
            trifuerza += '*'.repeat((2 * (i + 1)) - 1)
        } else {
            trifuerza += ' '.repeat(((2 * n) - 1) - i)
            trifuerza += '*'.repeat((2 * (i - n + 1)) - 1)
            trifuerza += ' '.repeat((2 * (2 * n - i)) - 1)
            trifuerza += '*'.repeat((2 * (i - n + 1)) - 1)
        }
        trifuerza += '\n'

    }

    return trifuerza
}


console.log(drawTrifuerza(3));