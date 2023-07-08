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


function createStairs(levels: number): void {
  const upperStair = '_|';
  const lowerStair = '|_';
  if (levels === 0) {
    console.log('__');
  }
  if (levels > 0) {
    for(let i = levels; i>0; i--) {
      const floor = '  '.repeat(i) + upperStair;
      console.log(floor);
    }
  } else if(levels < 0 ) {
    levels = Math.abs(levels);
    for(let i = 0; i<levels; i++) {
      const floor = '  '.repeat(i) + lowerStair;
      console.log(floor);
    }
  }
}

createStairs(0);
createStairs(9);
createStairs(-9);