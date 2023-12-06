/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

function escalera(escalones) {
  if(escalones > 0) {
    console.log(' '.repeat(escalones * 2) + '_');
    for(let i = escalones; i >= 1; i--){
      console.log(' '.repeat((i * 2) - 2) + '_|');
    }
  } else if(escalones < 0) {
    escalones *= -1;
    console.log('_');
    for(let i = 1; i <= escalones; i++){
      console.log(' '.repeat((i * 2) - 1) + '|_');
    }
  } else {
    console.log('__');
  }
}

escalera(4);
escalera(-4);
escalera(0);