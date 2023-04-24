/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isPrime(number) {
	// comprobar si el número es par y así descarlos todos con excepción del 2
	if (number < 2 || (number % 2 == 0 && number != 2)) {
		return false;
	}
  
	// Se revisa el modulo empezando en 3 y sin tener en cuenta los pares
	for (let i = 3; i <= (number / 2); i += 2) {
		if (number % i == 0) {
			return false;
		}
	}

	return true;
}

function fibonnaci(number) {
	// Se utliza la identidad de Binet para figurar si es de la secuencia de fibonnaci
	let binet = 5 * number * number;
	if (Number.isInteger(Math.sqrt(binet+4))) {
		return true;
	}
	if (Number.isInteger(Math.sqrt(binet-4))) {
		return true;
	}
	return false;
}

function checkNumber(number) {
	// Crea el mensaje sobre las condiciones descritas
	let message = "El número " + number.toString();
	message += isPrime(number) ? "" : " no";
	message += " es primo,";
	message += fibonnaci(number) ? "" : " no";
	message += " es fibonnaci y";
	message += number % 2 != 0 ? " es impar" : " es par";
	return message;
}

console.log(checkNumber(37))
console.log(checkNumber(73))
console.log(checkNumber(5))
console.log(checkNumber(2))
console.log(checkNumber(8))
console.log(checkNumber(46))
console.log(checkNumber(13))
