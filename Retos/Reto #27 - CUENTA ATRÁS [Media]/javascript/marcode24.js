/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

const countBack = (start, interval) => {
  if (start <= 0 || interval <= 0 || !Number.isInteger(start)
    || !Number.isInteger(interval)) {
    return;
  }
  const counter = setInterval(() => {
    console.log(start);
    start--;
    if (start <= 0) {
      clearInterval(counter);
      console.log('Termino!!!');
    }
  }, interval);
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
