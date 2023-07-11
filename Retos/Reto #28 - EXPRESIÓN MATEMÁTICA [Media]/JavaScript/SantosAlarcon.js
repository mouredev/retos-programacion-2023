import { describe, test } from "node:test";
import assert from "node:assert/strict";

const funcionMatematica = (expresion) => {
	const arrayOperadores = ["+", "-", "*", "/", "%"];
	
    // Se inicia el número de válidos a 0.
    let valido = 0;

	// Se comprueba si la expresión contiene los operadores aritméticos
	if (
		expresion.includes("+") ||
		expresion.includes("-") ||
		expresion.includes("*") ||
		expresion.includes("/") ||
		expresion.includes("%")
	) {
		// Se crea un array con los elementos de la expresión divididos por el
		// espacio.
		const arrayOperacion = expresion.split(" ");

		// Se itera por cada elemento del array
		for (let i = 0; i < arrayOperacion.length; i++) {
			// Se aumenta el número de validos si:
			// 1. El índice es impar y el valor dentro del array es un operador.
			// 2. El índice es par y el valor dentro del array no es un operador, si
			// no un "número".
			if (
				(i % 2 === 1 && arrayOperadores.includes(arrayOperacion[i])) ||
				(i % 2 === 0 && arrayOperadores.includes(arrayOperacion[i]) === false)
			) {
				valido++;
			}

		}

		// Si la cantidad de validos es igual que la longitud del array de operación,
		// se devuelve true.
		if (valido === arrayOperacion.length) {
			return true;
		}
		// En caso de que la expresión no contenga ningún operador, se devuelve
		// falso.
	} else {
		return false;
	}
};

/* TESTS */
describe("Tests de la función matemática", () => {
	test("5 + 6 debería dar válido", () => {
		const resultado = funcionMatematica("5 + 6");
		assert.equal(resultado, true);
	});
	test("8 % 4 - 5 debería dar válido", () => {
		const resultado = funcionMatematica("8 % 4 - 5");
		assert.equal(resultado, true);
	});
	test("8 % 4 debería dar válido", () => {
		const resultado = funcionMatematica("8 % 4");
		assert.equal(resultado, true);
	});
    test("12.5 % 10.0 debería dar válido", () => {
		const resultado = funcionMatematica("12.5 % 10.0");
		assert.equal(resultado, true);
	});
	test("15 + -6 debería dar válido", () => {
		const resultado = funcionMatematica("15 + -6");
		assert.equal(resultado, true);
	});
    test("15 + -6 / 4 * 5 debería dar válido", () => {
		const resultado = funcionMatematica("15 + -6 / 4 * 5");
		assert.equal(resultado, true);
	});
	test("2 o 3 debería dar falso", () => {
		const resultado = funcionMatematica("2 o 3");
		assert.equal(resultado, false);
	});
});
