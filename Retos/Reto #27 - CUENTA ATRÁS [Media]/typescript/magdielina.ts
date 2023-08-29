/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

const countdown = (start: number, interval: number, first : boolean = true) => {
    if(Number.isInteger(start) && Number.isInteger(interval) && (start > 0 || !first) && interval > 0) {
         if(start >= 0) {
            console.log(`Count... ${start}`);
            start--;
            setTimeout(countdown, interval * 1000, start, interval, false);

        }
     } else {
         console.log('Parameters are invalid, please provide only positive numbers');
     }
 }
 countdown(10, 1);