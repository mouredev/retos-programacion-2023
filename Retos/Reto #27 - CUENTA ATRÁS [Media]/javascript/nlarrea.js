/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

function countDown(start, step=1) {
    if (
        start < 0 || step < 0 ||
        !Number.isInteger(start) || !Number.isInteger(step)
    ) {
        throw new TypeError('The function only takes two positive integers as parameters!');
    }

    let count = start;

    console.log(count);
    count--;

    if (count >= 0) {
        setTimeout(() => {
            countDown(count, step);
        }, step * 1000)
    }
}


countDown(5, 1);