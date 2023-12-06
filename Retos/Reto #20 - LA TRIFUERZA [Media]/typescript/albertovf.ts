function trifuerza(nivel: number): void {
	const longitud: number = 2 * nivel;

	for (let n = 1; n <= nivel; n++) {
		let linea: string = '*'.repeat(2 * n - 1);
		linea = linea.padStart((longitud * 2 - linea.length) / 2 + linea.length);
		console.log(linea);
	}

	for (let n = 1; n <= nivel; n++) {
		let linea: string = '*'.repeat(2 * n - 1);
		let bordes = ' '.repeat(nivel - n);
		linea = bordes + linea + bordes + bordes + ' ' + linea;
		console.log(linea);
	}
}

trifuerza(5)