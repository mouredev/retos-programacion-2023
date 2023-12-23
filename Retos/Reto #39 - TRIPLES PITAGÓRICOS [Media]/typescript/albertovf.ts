const ternaPitagorica = (n1: number, n2: number, n3: number): boolean => {
	const cuadrado = (n: number): number => n ** 2
	return (cuadrado(n1) + cuadrado(n2) == cuadrado(n3))
}

const reto = (max: number): void => {
	for (let a = 1; a <= max; a++) {
		for (let b = a; b <= max; b++) {
			for (let c = b + 1; c <= max; c++) {
				if (ternaPitagorica(a, b, c)) {
					console.log(`${a},${b},${c}`);
				}
			}
		}
	}
}

reto(100)