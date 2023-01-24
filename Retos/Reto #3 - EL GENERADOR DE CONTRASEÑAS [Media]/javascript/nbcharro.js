/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const LONGITUDMAXIMA = 16;
const LONGITUDMINIMA = 8;
const LETRASMINUSCULAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const LETRASMAYUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
const SIMBOLOS = ['\\', '!', '\"', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '@', '#', '¡', '-', '<', '>', '_', '.', ':', ',', ';', '{', '}', '[', ']', '^', '*', 'Ç'];


function obtenerPassword() {
	try {
		const passwordCreado = generar();

		return passwordCreado;
	} catch (error) {
		return error.message;
	}
}

function generar() {
	if (longitudUsuarioDentroLimites()) {
		const caracteres = caracteresSegunDatosUsuario();
		const password = crearAleatoriamente(caracteres);

		return password;

	} else {
		throw new Error("La longitud de la contraseña debe estar entre 8 y 16 caracteres.");
	}
}

function longitudUsuarioDentroLimites() {
	let dentroLimite = false;
	if (longitudUsuario >= LONGITUDMINIMA && longitudUsuario <= LONGITUDMAXIMA) {
		dentroLimite = true;
	}
	return dentroLimite;
}

function caracteresSegunDatosUsuario() {
	let caracteres = [...LETRASMINUSCULAS];
	if (conMayusculas) {
		caracteres = [...caracteres, ...LETRASMAYUSCULAS];
	}
	if (conNumeros) {
		caracteres = [...caracteres, ...NUMEROS];
	}
	if (conSimbolos) {
		caracteres = [...caracteres, ...SIMBOLOS];
	}
	return caracteres;
}

function crearAleatoriamente(caracteres) {
	let password = '';
	while (password.length < longitudUsuario) {
		const numeroRandom = Math.floor(Math.random() * (caracteres.length));
		password += caracteres[numeroRandom];
	}
	return password;
}


const longitudUsuario = 16;
const conMayusculas = true;
const conNumeros = true;
const conSimbolos = true;

console.log("El password generado aleatoriamente es: " + obtenerPassword());
