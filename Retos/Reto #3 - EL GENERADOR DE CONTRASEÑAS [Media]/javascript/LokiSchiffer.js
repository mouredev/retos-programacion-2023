/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

// Getting all the cahracters for use
let characterSet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
const mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const simbols = ["|", "!", "\"", "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "¡", "¿", "+", "-", "*", "{", "}", "[", "]", ";", ":", "_", "^"];

// Function to determine the size of the password, keeping the restrictions in check
function checkLenght(passwordLength) {
	if (passwordLength < 8) {
		return 8
	} else if (passwordLength > 16) {
		return 16
	}
	return passwordLength
}

// Asking the user for the selected information
let passLength = prompt("Ingresar la longuitud: ")
let hasMayus = prompt("Tiene mayusculas?(y/n) ")
let hasNumbers = prompt("Tiene números?(y/n) ")
let hasSimbols = prompt("tiene símbolos?(y/n) ")
// Cheking the different flags for character use
if (hasMayus === "y") {
	characterSet += mayus
	//console.log(characterSet)
}
if (hasNumbers === "y") {
	characterSet += numbers
}
if (hasSimbols === "y") {
	characterSet += simbols
}
let passLenght = checkLenght(passLength);
password = ""
for ( let i = 0; i <passLenght; i++) {
	// Looping through to obtain the password
	password += characterSet[Math.floor(Math.random()*characterSet.length)]
}
console.log(password)