/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

function cuenta_atras(inicio, segundos){
    if(typeof(inicio) != "number" || typeof(segundos) != "number" || inicio < 0 || segundos < 0 || 
       Number.isInteger(inicio) == false || Number.isInteger(segundos) == false){
        console.log("Por favor, ingrese un número entero positivo");
    }

    setTimeout(() => {
        console.log(inicio);
        if(inicio > 0) cuenta_atras(inicio - 1, segundos);
    }, segundos * 1000);
}

console.log(cuenta_atras(10, 5));
// console.log(cuenta_atras(10, 5));
// console.log(cuenta_atras(-5, 10));
// console.log(cuenta_atras(0, 10));
// console.log(cuenta_atras(4.6, 5));