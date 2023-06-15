const cifradoCesar = (texto: string, desplazamiento: number): string => {
	let resultado = '';

	if (-26 > desplazamiento || desplazamiento > 26) return resultado;

	for (let caracter of texto) {
		if (caracter.match(/[A-Z]/i)) {
			const ascii = caracter.charCodeAt(0);
			let asciiDesplazado = ascii + desplazamiento;

			if (caracter.match(/[A-Z]/)) {
				if (asciiDesplazado > 90) asciiDesplazado = 65 + (asciiDesplazado - 91);
				else asciiDesplazado = 90 - (64 - asciiDesplazado);
			} else {
				if (asciiDesplazado > 122) asciiDesplazado = 97 + (asciiDesplazado - 123);
				else asciiDesplazado = 122 - (96 - asciiDesplazado);
			}
			caracter = String.fromCharCode(asciiDesplazado);
		}
		resultado += caracter;
	}

	console.log(`Texto original: ${texto}`);
	console.warn(`Texto cifrado: ${resultado}`);
	return resultado;
}

const textoOriginal = "\n/*\n * Crea un programa que realize el cifrado César de un texto y lo imprima. \n * También debe ser capaz de descifrarlo cuando así se lo indiquemos. \n * \n * Te recomiendo que busques información para conocer en profundidad cómo \n * realizar el cifrado. Esto también forma parte del reto. \n */"
const desplazamiento = -12;
cifradoCesar(textoOriginal, desplazamiento);
