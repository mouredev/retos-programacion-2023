/*
Un heterograma es una palabra o frase que no contiene ninguna letra repetida

Un isograma  es una palabra o frase en la que cada letra aparece el mismo número de veces. Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente.

Un pangrama es una frase en la que aparecen todas las letras del abecedario. Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto.

*/

function repeticionesLetras(text: string) {
	function normalize(word: string) {
		return word.toLowerCase().replace(/[.!¡?¿,:{}()[]]/g, "");
	}
	let dict: { [key: string]: number } = {};
	let separatedWords = text.split("");
	for (let word of separatedWords) {
		if (normalize(word) in dict) {
			++dict[normalize(word)];
		} else {
			dict[normalize(word)] = 1;
		}
	}
	delete dict[" "]
	return dict
}

const heterograma = (texto: string) => {
	let letras = repeticionesLetras(texto)
	for (let k in letras) {
		let v = letras[k];
		if (v > 1) {
			return false;
		}
	}
	return true;
}

const isograma = (texto: string): boolean => {
	let repeticiones = Array.from(new Set(Object.values(repeticionesLetras(texto))))

	return 1 == repeticiones.length
}

const pangrama = (texto: string): boolean => {
	return Object.keys(repeticionesLetras(texto)).length == 27
}

const reto = (cadena: string) => {
	console.log(heterograma(cadena) ? 'Es un heterograma' : 'No es un heterograma')
	console.log(isograma(cadena) ? 'Es un isograma' : 'No es un isograma')
	console.log(pangrama(cadena) ? 'Es un pangrama' : 'No es un pangrama')
}

reto('abcdefghijklmnñopqrstuvwxyz');
