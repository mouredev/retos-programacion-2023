/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 * API usada:
 * https://github.com/aunyks/newton-api
 */


async function derivar(polinomio) {
	let respuesta = await fetch(`https://newton.now.sh/api/v2/derive/${polinomio}`)
	let json = await respuesta.json();
	return json
}

async function integrar(polinomio) {
	let respuesta = await fetch(`https://newton.now.sh/api/v2/integrate/${polinomio}`)
	let json = await respuesta.json();
	return json
}

(async function () {
	const polinomio = "x^2+2x";
	const derivada = await derivar(polinomio)
	console.log(`Polinomio '${derivada.expression}' y su derivada '${derivada.result}'`)
	const polinomio2 = "2x^3";
	const integral = await integrar(polinomio2)
	console.log(`Polinomio '${integral.expression}' y su integral '${integral.result}'`)
})()
