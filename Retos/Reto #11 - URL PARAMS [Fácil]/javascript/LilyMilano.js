/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const url =
	'https://retosdeprogramacion.com?year=2023&challenge=11&language=javascript';

function retrieveParameters(url) {
	const queryString = url.split('?')[1];
	const paramsKeyValue = queryString.split('&');
	return paramsKeyValue.map((param) => param.split('=')[1]);
}

console.log(retrieveParameters(url));

// Log: [ '2023', '11', 'javascript' ]
