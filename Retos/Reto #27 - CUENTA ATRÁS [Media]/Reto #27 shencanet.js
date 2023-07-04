
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
function cuentaRegresiva(numeroInicial, tiempoEntreNumeros) {
  // Validar si los parámetros son números enteros
  if (!Number.isInteger(numeroInicial) || !Number.isInteger(tiempoEntreNumeros) || numeroInicial <= 0 || tiempoEntreNumeros <= 0) {
    console.log('Los parámetros deben ser números enteros Positivos.');
    return;
  }

  let contador = numeroInicial;

  const intervalo = setInterval(() => {
    console.log(contador);

    if (contador === 0) {
      clearInterval(intervalo);
      setTimeout(() => {
      console.log('¡Feliz año nuevo!')
        
      },1500);
    }

    contador--;
  }, tiempoEntreNumeros);
  console.log(`Contando...`);
}

// Ejemplo de uso:
cuentaRegresiva(10, 1000)