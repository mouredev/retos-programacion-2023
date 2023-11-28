//*Se crea un array que contiene los números, letras minusculas y mayusculas, y simbolos.
const mixedArray = [
	...Array(10).keys(),
	...Array(26)
		.fill()
		.map((_, i) => String.fromCharCode(97 + i)),
	...Array(26)
		.fill()
		.map((_, i) => String.fromCharCode(65 + i)),
	...["!", "@", "#", "$", "%", "^", "&", "*"],
];

const generatePassword = () => {
	let res = "";

	//*Se crean las variables para crear un valor aletorio,
	//* lengthOfPassword === la longitud aleatoria de cada contraseña
	//* arrLength === longitud del array previamente creado.
	//*Por medio de un bucle for recoremos hasta que se llegue a longitud actual, en cada iteración j crea un numero aleatorio
	//* >= 0 y <= arrLength(que seria 70), luego solamente se le asigna ese valor al Caracter actual.

	let lengthOfPassword = Math.floor(Math.random() * (16 - 8) + 8);
	let arrLength = mixedArray.length;
	let j = 0;

	for (let i = 0; i <= lengthOfPassword; i++) {
		j = Math.floor(Math.random() * arrLength);
		res += `${mixedArray[j]}`;
	}

	return res;
};

console.log(generatePassword());
console.log(generatePassword());
console.log(generatePassword());
console.log(generatePassword());
