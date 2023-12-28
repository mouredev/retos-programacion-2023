/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const lettersLeet: {
	[index: string]: string;
} = {
	A: '4',
	B: 'I3',
	C: '[',
	D: ')',
	E: '3',
	F: '|=',
	G: '&',
	H: '#',
	I: '1',
	J: ',_|',
	K: '>|',
	L: '1',
	M: '/\\/\\',
	N: '^/',
	O: '0',
	P: '|*',
	Q: '(_,)',
	R: 'I2',
	S: '5',
	T: '7',
	U: '(_)',
	V: '\\/',
	W: '\\/\\/',
	X: '><',
	Y: 'j',
	Z: '2',
	1: 'l',
	2: 'z',
	3: 'e',
	4: 'a',
	5: 's',
	6: 'b',
	7: 't',
	8: 'b',
	9: 'g',
	0: 'o',
};

const text = 'hola que tal';
const encryptMessage = (text: string) =>
	text
		.toLocaleUpperCase()
		.split('')
		.reduce((acc, letter) => {
			if (letter === ' ') return acc + ' ';
			return acc + (lettersLeet[letter] || '');
		}, '');

console.log(encryptMessage('hola que tal 541'));
