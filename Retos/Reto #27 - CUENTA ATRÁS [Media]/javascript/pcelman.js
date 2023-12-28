/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

function countBack(startingNumber, interval) {
    let eachStep = startingNumber;
  
    while (eachStep >= 0) {
      console.log(eachStep);
      eachStep -= interval;
    }
  }
  
  countBack(20, 2);