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
    let totalRows = 2 * rows;
    let firstSpaces = 2 * rows - 1;
    let triforce = '';
    for (let i=1; i<=totalRows; i++) {
        if (i === 1) {
            triforce += `${' '.repeat(firstSpaces)}*\n`;
            firstSpaces--;
        } else if (i % 2 === 0) {
            triforce += `${' '.repeat(firstSpaces)}` + '*** '.repeat(i / 2) + '\n';
            firstSpaces--;
        } else if (i % 2 !== 0) {
            triforce += `${' '.repeat(firstSpaces)}` + ('*' + ' '.repeat(3)).repeat((i + 1) / 2) + '\n';
            firstSpaces--;
        }
    }
    console.log(triforce);
}

drawTriforce(2);