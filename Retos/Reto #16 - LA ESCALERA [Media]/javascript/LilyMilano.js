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

function drawStaircase(steps) {
	const resultParts = [];

	switch (true) {
		case steps === 0:
			resultParts.push(`__`);
			break;
		case steps > 0:
			resultParts.push(`${' '.repeat(steps)}_\n`);
			for (let i = 0; i < steps; i++) {
				resultParts.push(`${' '.repeat(steps - i - 1)}_|\n`);
			}
			break;
		case steps < 0:
			for (let i = 0; i < Math.abs(steps); i++) {
				resultParts.push(`${' '.repeat(i)}|_\n`);
			}
			resultParts.push(`${' '.repeat(Math.abs(steps))}|`);
			break;
	}
	return resultParts.join('');
}

// Testing:

console.log(drawStaircase(0));
console.log(drawStaircase(6));
console.log(drawStaircase(-6));
