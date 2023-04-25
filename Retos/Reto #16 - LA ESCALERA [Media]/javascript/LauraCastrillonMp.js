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

function escalera (numeroEscalera) {
    let escalera = '';
    console.log(`-----------------------------------\n Escalones introducidos: ${numeroEscalera}`)

    if (numeroEscalera > 0) {
        escalera += `${"  ".repeat(numeroEscalera)}_\n`;
        for (let i = 0; i < numeroEscalera; i++) {
            escalera += `${'  '.repeat(numeroEscalera - i - 1)}_|\n`;
        }
    } else if (numeroEscalera < 0) {
        escalera += '_\n';
        for (let i = 0; i < Math.abs(numeroEscalera); i++) {
            escalera += `${'  '.repeat(i)} |_\n`;
        }
    } else {
        escalera = '__';
    }
    return escalera;
}
console.log(escalera(4));
console.log(escalera(-4));
console.log(escalera(0));