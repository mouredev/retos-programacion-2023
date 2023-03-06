/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

function detectarHeterograma(texto) {
	// Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
	const letras = texto.toLowerCase().split('');
	let letrasSeparadas = new Map();
	letras.forEach(letra => {
		if (letrasSeparadas.has(letra)) {
			const sumar = letrasSeparadas.get(letra) + 1;
			letrasSeparadas.set(letra, sumar);
		} else {
			letrasSeparadas.set(letra, 1);
		}
	});
	letrasSeparadas.delete(' ');
	let esHistograma = true;
	letrasSeparadas.forEach((cantidadLetra, letra) => {
		if (cantidadLetra > 1 && esLetra(letra)) {
			esHistograma = false;
		}
	});
	return esHistograma;
}

function detectarIsograma(texto) {
	// Un isograma es una palabra o frase que tiene todas las letras repetidas almenos 1 vez.
	const letras = texto.toLowerCase().split('');
	let letrasSeparadas = new Map();
	letras.forEach(letra => {
		if (letrasSeparadas.has(letra)) {
			const sumar = letrasSeparadas.get(letra) + 1;
			letrasSeparadas.set(letra, sumar);
		} else {
			letrasSeparadas.set(letra, 1);
		}
	});
	letrasSeparadas.delete(' ');
	let esIsograma = true;
	letrasSeparadas.forEach((cantidadLetra, letra) => {
		if (cantidadLetra == 1 && esLetra(letra)) {
			esIsograma = false;
		}
	});
	return esIsograma;
}

function detectarPangrama(texto) {
	// Un pangrama es un texto que usa todas las letras posibles del alfabeto de un idioma
	const abecedarioEs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
	const letras = texto.toLowerCase().split('');
	const letters = new Set(letras);
	let esIsograma = true;
	abecedarioEs.forEach(letra => {
		if (!letters.has(letra) && esLetra(letra)) {
			esIsograma = false;
		}
	});
	return esIsograma;
}

function esLetra(str) {
	var regex = /[a-z]/;
	if (regex.test(str)) {
		return true;
	} else {
		return false;
	}
}

const histograma = detectarHeterograma("Reto de programacion numero 9");
const histograma2 = detectarHeterograma("yuxtaponer");
console.log(histograma, histograma2);

const isograma = detectarIsograma("Reto de programacion numero 9");
const isograma2 = detectarIsograma("dracondicionar");
console.log(isograma, isograma2);

const pangrama = detectarPangrama("Reto de programacion numero 9");
const pangrama2 = detectarPangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.");
console.log(pangrama, pangrama2);