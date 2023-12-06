const reto = (abaco: string[]): string => {
	let resultado = '';
	abaco.map(l => {
		resultado += l.split('---')[0].length
	})

	resultado = parseInt(resultado, 10).toLocaleString();
	console.log(resultado);
	return resultado
}

reto(["O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"])