
const valor = (palabra: string): number => {
	const LETRAS = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	let letras = palabra.toUpperCase().split("")
	let v = 0
	letras.forEach(e => {
		v += LETRAS.findIndex(l => l == e)
	})
	return (v > 0) ? v : 0
}

const reto = (): void => {
	let puntos = 0
	while (puntos < MAXIMO) {
		let palabra = prompt("Introduce una palabra: ") ?? ""
		puntos = valor(palabra)
		console.log(`La palabra ${palabra} tiene ${puntos} puntos`)
		if (puntos < MAXIMO) {
			console.log("Busca una palabra mas grande")
		} else {
			console.log("Has ganado")
		}
	}
}
const MAXIMO = 100

reto()