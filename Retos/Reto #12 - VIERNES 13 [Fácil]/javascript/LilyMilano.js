/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

function isFriday13(month, year) {
	try {
		const date = new Date(year, month - 1, 13);
		if (date.getDay() === 5) {
			return true;
		} else return false;
	} catch (error) {
		console.log(error);
	}
}

// Testing______________________________________
console.log(isFriday13(5, 2016)); // true
console.log(isFriday13(5, 2022)); // true
console.log(isFriday13(10, 2023)); // true
console.log(isFriday13(4, 2023)); // false
