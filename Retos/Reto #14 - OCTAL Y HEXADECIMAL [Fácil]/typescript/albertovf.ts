enum Base {
	Decimal = 10,
	Octal = 8,
	Hexadecimal = 16,
	Binario = 2
}


const reto = (numero: number, base: Base): string => {
	const digitos = "0123456789ABCDEF";
	let num_transformacion: string = '';

	if (numero <= 0) {
		num_transformacion = "0";
	}

	while (numero > 0) {
		const digit = numero % base;
		num_transformacion = digitos.charAt(digit) + num_transformacion;
		numero = Math.floor(numero / base);
	}
	console.log(num_transformacion);

	return num_transformacion;

}

reto(15, Base.Hexadecimal)
reto(15, Base.Octal)