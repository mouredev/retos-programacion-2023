/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */


function countdown(number, seconds) {
    let time = number;
    let intervalId = setInterval(function () {
        console.log(time);
        time--;
        if (time < 0) {
            clearInterval(intervalId);
        }
    }, seconds * 1000);
}


console.log(countdown(10, 2))
