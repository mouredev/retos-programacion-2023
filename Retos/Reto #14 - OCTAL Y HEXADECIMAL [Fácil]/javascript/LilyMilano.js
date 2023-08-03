/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

const decimalToOctal = (decimal) => {
	if (
		typeof decimal !== 'number' ||
		decimal < 0 ||
		!Number.isInteger(decimal)
	) {
		throw new Error('Invalid input. Please enter a positive number.');
	}
	let octal = '';
	while (decimal > 0) {
		const remainder = decimal % 8;
		octal = `${remainder}${octal}`;
		decimal = decimal >> 3;
	}
	return octal;
};

const getHexadecimalDigit = (decimal) => {
	switch (decimal) {
		case 10:
			return 'A';
		case 11:
			return 'B';
		case 12:
			return 'C';
		case 13:
			return 'D';
		case 14:
			return 'E';
		case 15:
			return 'F';
		default:
			return decimal;
	}
};
const decimalToHexadecimal = (decimal) => {
	if (
		typeof decimal !== 'number' ||
		decimal < 0 ||
		!Number.isInteger(decimal)
	) {
		throw new Error('Invalid input. Please enter a positive number.');
	}
	let hexadecimal = '';
	for (let i = decimal; i > 0; i = Math.floor(i / 16)) {
		const remainder = i % 16;
		const char = getHexadecimalDigit(remainder);
		hexadecimal = `${char}${hexadecimal}`;
	}
	return hexadecimal;
};
// Testing:
console.log(decimalToOctal(100)); // Log: 144
console.log(decimalToOctal(500)); // Log: 764
console.log(decimalToHexadecimal(100)); // Log: 64
console.log(decimalToHexadecimal(500)); // Log: 1F4
