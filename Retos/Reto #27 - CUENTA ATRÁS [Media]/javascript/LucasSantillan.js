/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
*/

function theFinalCountdown(num, intervalo) {
  console.log(num);
  if (num == 0) {
    return;
  } else {
    num = num - 1;
    let inter = intervalo * 1000;
    setTimeout(theFinalCountdown, inter, num, intervalo);
  }
}

theFinalCountdown(5, 1);
