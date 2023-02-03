/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

// ____________________________________________________________________________
const passwordGenerate = (upper, number, symbol) => {
	// Defining main function, constructors and data.

	const lowerCase = 'abcdefghijklmnñopqrstuvwxyz';
	const upperCase = lowerCase.toUpperCase();
	const numbers = '0123456789';
	const symbols = '()¬%#@"=!¡?¿[-+ç/ª])';
	// ________________________________________________________________________
	// Generating a random integer in a range (our iterative password lenght):

	let min = 8,
		max = 16;
	let passwordLength = Math.floor(Math.random() * (max - min)) + min;
	console.log(passwordLength);
	// ________________________________________________________________________

	let password = '';

	let acumulatorString = lowerCase;

	if (upper) acumulatorString += upperCase;
	if (number) acumulatorString += numbers;
	if (symbol) acumulatorString += symbols;

	for (let i = 0; i < passwordLength; i++) {
		password +=
			acumulatorString[Math.floor(Math.random() * acumulatorString.length)];
	}

	console.log(password);
};

passwordGenerate(); // lowercase
passwordGenerate(true, false, false); // uppercase + lowercase
passwordGenerate(true, false, true); // without numbers
passwordGenerate(false, true, false); // lowercase + numbers
passwordGenerate(false, false, true); // lowercase + symbols
passwordGenerate(true, true, false); // without symbols
passwordGenerate(true, true, true); // lowercase, uppercase, numbers and symbols

// Log:
// 11: nyicziosakr
// 11: eSrtsdHzCXx
// 12: Ld]WJ#Ob(i+p
// 9: ñnybcd56v
// 15: d=¿reg(rh][¬zfp
// 11: eax3oñxdgmI
// 13: vx/QX9kmcmnp¡
