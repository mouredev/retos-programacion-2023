"use strict";

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isPrime(number) {
	if (number > 1) {
		for (let i = 2; i < number; i++) {
			if (number % i === 0) {
				return false;
			}
		}
		return true;
	} else {
		return false;
	}
}

function fibonacci(number) {
	if (number === 0) {
		return 0;
	} else if (number === 1) {
		return 1;
	} else {
		return fibonacci(number - 1) + fibonacci(number - 2);
	}
}

function isFibonacci(number) {
	var sequence = [fibonacci(0)];
	let counter = 0;

	while (sequence[counter] < number) {
		counter++;
		sequence.push(fibonacci(counter));
	}

	if (sequence[counter] === number) {
		return true;
	}

	return false;
}

function isEven(number) {
	if (number % 2 === 0) {
		return true;
	}
	return false;
}

function checkNumber(number) {
	let result = isPrime(number)
		? `${number} es primo,`
		: `${number} no es primo,`;
	result += isFibonacci(number) ? ' es fibonacci' : ' no es fibonacci';
	result += isEven(number) ? ' y es par' : ' y es impar';

	return result;
}

console.log(checkNumber(2)); // 2 es primo, es fibonacci y es par
console.log(checkNumber(7)); // 7 es primo, no es fibonacci y es impar
console.log(checkNumber(5)); // 5 es primo, es fibonacci y es impar
