/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

const cuentaAtras = (numeroInicial, segundos) => {
  if (numeroInicial > 0) {
    for (let i = numeroInicial; i >= 0; i--) {
      console.log(i);
      sleep(segundos);
    }
  }
};

const sleep = (ms) => {
  const time = new Date().getTime() + ms;
  while (new Date().getTime() < time) continue;
};

cuentaAtras(5, 1000);
