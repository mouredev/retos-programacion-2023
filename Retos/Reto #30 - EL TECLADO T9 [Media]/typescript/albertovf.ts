
const reto = (pulsaciones: string): string => {
	let resultado = ""
	const teclado = [
		[' ', '.', ',', '0'],
		['A', 'B', 'C', '1'],
		['D', 'E', 'F', '2'],
		['G', 'H', 'I', '3'],
		['J', 'K', 'L', '4'],
		['M', 'N', 'O', '5'],
		['P', 'Q', 'R', 'S', '6'],
		['T', 'U', 'V', '7'],
		['W', 'X', 'Y', 'Z', '8'],
	]

	for (let tecla of pulsaciones.split('-')) {
		let numero = parseInt(tecla.charAt(0))
		let letra = teclado[numero - 1][tecla.length - 1]
		resultado += letra
	}

	console.log(resultado);
	return resultado
}

reto("6-666-88-777-33-3-33-888")