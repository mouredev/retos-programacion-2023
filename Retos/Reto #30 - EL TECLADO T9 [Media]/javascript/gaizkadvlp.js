/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

const TECLADO = [
	[',','.','!','?'],
	['A','B','C'],
	['D','E','F'],
	['G','H','I'],
	['J','K','L'],
	['M','N','O'],
	['P','Q','R','S'],
	['T','U','V'],
	['W','X','Y','Z'],
	[' ']
];

const ENTRADA = "6-666-88-777-33-3-33-888";

function transformaPulsaciones(cadena) {
	console.log("Entrada: ", cadena)

	let posX = posY = '';
	let temp = cadena.split('-');
	let salida = "";

	for (let i=0; i<temp.length; i++){
		posX = (temp[i].charAt(0) - 1);
		posY = (temp[i].length - 1);
		let nuevoCaracter = TECLADO[posX][posY];
		salida = salida + nuevoCaracter;
	}
	return salida
}

console.log("Salida:  ",  transformaPulsaciones(ENTRADA)); //Salida: MOUREDEV

