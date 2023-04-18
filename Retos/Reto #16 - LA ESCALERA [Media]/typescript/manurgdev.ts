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

const createStairs = (n: number): string => {
    if (n === 0) return '__';

    let stairs = '';
    const isAscending = n > 0;
    const steps = Math.abs(n);
    let spaces = '  '.repeat(steps);

    stairs = isAscending ? `${spaces}_\n` : '_\n';
    spaces = isAscending ? spaces.slice(0, -2) : ' ';

    [...Array(steps)].forEach(() => {
        stairs += isAscending ? `${spaces}_|\n` : `${spaces}|_\n`;
        spaces = isAscending ? spaces.slice(0, -2) : `${spaces}  `;
    });

    return stairs;
}

console.log(createStairs(6));
console.log(createStairs(0));
console.log(createStairs(-10));