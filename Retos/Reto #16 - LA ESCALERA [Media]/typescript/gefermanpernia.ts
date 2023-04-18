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


function dibujarEscalera(numeroEscalones: number): void {
	const isAscendente = numeroEscalones > 0;
	const numeroPasos = Math.abs(numeroEscalones);

	if (numeroPasos === 0) {
		console.log('__');
		return; 
	}


	let escalera = '';

	if (!isAscendente) escalera =  "_\n";
	else escalera= "  ".repeat(numeroPasos)+"  _\n"
	
	for (let i = 0; i < numeroPasos; i++) {
		const espacios = '  '.repeat(isAscendente ? numeroPasos - i : i);
		const peldaño = isAscendente ? `${espacios}_|` : `${espacios} |_`;
		escalera += `${peldaño}\n`;
		
	}
	
	

	console.log(escalera);
}


dibujarEscalera(-10)

dibujarEscalera(0)

dibujarEscalera(10)