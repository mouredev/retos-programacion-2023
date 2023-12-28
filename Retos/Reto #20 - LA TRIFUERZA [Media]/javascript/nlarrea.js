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

function drawTriforce(rows) {
    let result = '';
    let leftSpace = 2 * rows - 1;//?

    for (let i=1; i<=rows; i++) {
        result += ' '.repeat(leftSpace) + '*'.repeat(2 * i - 1) + '\n'
        leftSpace--;
    }

    for (let i=1; i<=rows; i++) {
        result += `${' '.repeat(leftSpace) + '*'.repeat(2 * i - 1) + ' '.repeat(leftSpace + 1)}`.repeat(2) + '\n';
        leftSpace--;
    }

    console.log(result);
}


drawTriforce(4);