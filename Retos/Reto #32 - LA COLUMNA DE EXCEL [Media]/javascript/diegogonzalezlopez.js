const testInput = 'CZ';

const baseTable = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

function returnColumn(input) {

	const inputUppercase = input.toUpperCase();

	// Chequeamos que el input esté formado sólo por letras
	const regexp = /^[A-Z]+$/;
	if (!regexp.test(inputUppercase))  {
		return '¯\\_(ツ)_/¯';
	}
	
	// El primer paso es sustituir cada letra por su equivalente numérico.
	// Dado que en Excel se empieza a contar en 1 y no en 0, se añade 1 al valor que le correspondería a cada letra
	let numbers = [];
	for (char of inputUppercase) {
		numbers.push(charToNumber(char)+1);
	}

	// El cálculo es similar a hacer cualquier cambio entre sistemas de numeración
	// En este caso sería como pasar de base26 a decimal, es decir:
	// 26 elevado a la posición del decimal multiplicado por el valor de la cifra para cada una de las cifras
	let result = 0;
	let decimalPosition = numbers.length-1;
	for (i = 0; i < numbers.length; i++) {
		result += (26**decimalPosition) * numbers[i];
		decimalPosition--;
	}

	return result;

}

function charToNumber(char) {

	for (i = 0; i < baseTable.length; i++) {
		if (char == baseTable[i]) return i;
	}

}

console.log(returnColumn(testInput));
