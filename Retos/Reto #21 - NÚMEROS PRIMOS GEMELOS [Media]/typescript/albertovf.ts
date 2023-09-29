const esPrimo = (n: number): boolean => {
	if (n <= 2) return true;
	for (let i = 2; i <= n / 2; i++) {
		if (n % i === 0) return false;
	}
	return true;
}

const reto = (n: number): void => {
	let gemelos = new Array();

	for (let j = 2; j <= n; j++) {
		if ((j + 2) <= n && esPrimo(j) && esPrimo(j + 2)) {
			gemelos.push([j, j + 2]);
		}
	}
	console.log(gemelos);
}

reto(14)