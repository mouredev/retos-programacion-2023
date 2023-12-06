const reto = (texto: string): Record<string, number | string> => {
	texto = texto.trim();
	const masLarga = (actual: string, larga: string) => (actual.length > larga.length) ? actual : larga
	let palabras = 1, longitudPalabra = 0, oraciones = 0;
	let palabraMasLarga = '', palabraActual = '';

	for (let c = 0; c < texto.length; c++) {
		const caracter = texto[c];

		if (caracter === " " || caracter === ".") {
			longitudPalabra += palabraActual.length;
			palabraMasLarga = masLarga(palabraActual, palabraMasLarga)
			palabraActual = '';
			caracter === " " ? palabras++ : oraciones++
		} else palabraActual += caracter;
	}

	return {
		'Numero de palabras': palabras,
		'Numero de oraciones': oraciones,
		'Longitud media': longitudPalabra / palabras,
		'Palabra mas larga': palabraMasLarga
	}
}

const texto = "Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior."

console.log(reto(texto));
