enum Bloque {
	ESD = "╗"
	, EID = "╝"
	, ESI = "╔"
	, EII = "╚"
	, LAT = "║"
	, BAS = "═"
}

const reto = (n: number) => {
	const medio = Math.ceil(n / 2);
	let espiral = `${Bloque.BAS.repeat(n - 1)}${Bloque.ESD}\n`;

	for (let y = 1; y < medio; y++) {
		espiral += Bloque.LAT.repeat(y - 1)
		espiral += `${Bloque.ESI}${Bloque.BAS.repeat(n - (2 * y) - 1)}${Bloque.ESD}`
		espiral += `${Bloque.LAT.repeat(y)}\n`
	}
	for (let y = medio; y < n; y++) {
		espiral += Bloque.LAT.repeat(n - y - 1)
		espiral += `${Bloque.EII}${Bloque.BAS.repeat((2 * y) - n)}${Bloque.EID}`
		espiral += `${Bloque.LAT.repeat(n - y - 1)}\n`;
	}
	console.log(espiral);
	// console.log(espiral.slice(0, -1).split('\n').map(l => l.split('')))
};
reto(5);