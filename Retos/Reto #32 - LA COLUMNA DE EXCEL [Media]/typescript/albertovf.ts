const reto = (columna: string): number => {
	const ASCII_LET_A = "A".charCodeAt(0)
	let column = columna.toUpperCase().split('')

	const valuate = (total, actual, index) => {
		let val = (actual.charCodeAt() - ASCII_LET_A) + 1
		val *= (26 ** index);
		return total + val;
	};

	const numero = column.reverse().reduceRight(valuate, 0);
	console.log(numero);
	return numero
}

reto("A")
reto("Z")
reto("AA")
reto("CA")