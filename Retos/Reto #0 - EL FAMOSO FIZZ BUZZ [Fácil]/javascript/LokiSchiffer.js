/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function fizzbuzz(num) {
  let threeMultiple, fiveMultiple, message;

	for (let i = 1; i <=  num; i++){
		threeMultiple = i % 3 == 0;
		fiveMultiple = i % 5 == 0;

		if (threeMultiple && fiveMultiple) {
			message = "fizzbuzz";
		}
		else if (threeMultiple) message = "fizz";
		else if (fiveMultiple) message = "buzz";
		else message = i;

		console.log(message);
	}
}

fizzbuzz(100)