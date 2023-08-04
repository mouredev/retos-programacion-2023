/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

function countdown(number, seconds) {
    if (!Number.isInteger(number) || !Number.isInteger(seconds) || number < 0 || seconds < 0) {
        console.log('Only positive integers are accepted')
        return
    } 
    if (number >= 0) {        
        setTimeout(() => {
            console.log(number)
            if (number > 0) {
                countdown(number-1, seconds)
            }          
        }, seconds*1000)
    }    
}


countdown(5,3)