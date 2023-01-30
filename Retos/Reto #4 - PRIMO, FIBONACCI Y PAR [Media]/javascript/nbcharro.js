/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */



function iniciar(numero) {
	const numeroEsPrimo = esPrimo(numero);
	const numeroEsFibonacci = esFibonacci(numero);
	const numeroEsPar = esPar(numero);
	const frase = obtenerFrase(numero, numeroEsPrimo, numeroEsFibonacci, numeroEsPar);
	return frase;
}

const numero11 = iniciar(11);
console.log(numero11);
const numero144 = iniciar(144);
console.log(numero144);
const numero5 = iniciar(5);
console.log(numero5);

function esPrimo(numero) {
	for (let index = 2; index < numero; index++) {
		if (numero % index == 0) {
			return false;
		}
	}
	return true;
}

function esFibonacci(numero) {
	const sol = [0, 1];
	for (let i = 2; i <= numero; i++) {
		sol[i] = sol[i - 1] + sol[i - 2];
		if (sol[i] == numero) {
			return true;
		}
	}
}

function esPar(numero) {
	return (numero % 2) == 0;
}

function obtenerFrase(numero, esPrimo, esFibonacci, esPar) {
	let frase = 'El numero ' + numero;
	if (esPrimo) {
		frase += ' es primo,'
	} else {
		frase += ' no es primo,'
	}
	if (esFibonacci) {
		frase += ' es fibonacci'
	} else {
		frase += ' no es fibonacci'
	}
	if (esPar) {
		frase += ' y es par'
	} else {
		frase += ' y es impar'
	}
	return frase;
}