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

function drawStair(numSteps) {
  const totalSteps = Math.abs(numSteps);
  const asc = numSteps >= 0;
  if (numSteps === 0) {
    console.log('__');
  }
  let steps = [];
  for (let i = 0; i < totalSteps; i++) {
    const step = '_|'
      .padStart(2 * (i + 1), ' ') // fill spaces before based on the step height
      .padEnd(2 * totalSteps + 1); // fill spaces at the end to have all steps with the same length
    steps.unshift(step);
  }
  steps.unshift('_'.padStart(totalSteps * 2 + 1, ' '));
  if (!asc) {
    // if desceneding, reverse all steps
    steps = steps.map((step) => step.split('').reverse().join(''));
  }
  // print the stair
  steps.forEach((step) => console.log(step));
}

drawStair(-7);
console.log();
//drawStair(-1);
