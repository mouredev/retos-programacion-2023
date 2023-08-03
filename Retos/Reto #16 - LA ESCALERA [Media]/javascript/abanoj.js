/* Reto 16 
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

const reto16 = (num) => {
  if(typeof num !== 'number') return ':(';
  if(num === 0) return '__';
  if(num > 0){
    stairsUp('  ', num);
  } else {
    stairsDown('  ', Math.abs(num));
  }
}

const stairsUp = (space, num) => {
  for (let i = 0; i < num; i++) {
    if(i === 0) console.log(space.repeat(num+1) + '_');
    console.log(space.repeat(num-i) + '_|');
  }
}

const stairsDown = (space, num) => {
  for (let i = 0; i < num; i++) {
    if(i === 0) console.log('_');
    console.log(space.repeat(i) + ' |_');
  }
}
