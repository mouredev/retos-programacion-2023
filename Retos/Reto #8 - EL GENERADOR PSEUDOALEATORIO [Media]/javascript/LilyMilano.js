'use strict';

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

function pseudoRandom() {
	let start = performance.now();
	let end = performance.now();
	let p = Math.round((end - start) * 10000);

	if (p >= 0 && p <= 100) {
		return p;
	} else return 'unexpected value';
}

console.log(pseudoRandom()); // Log: 67
