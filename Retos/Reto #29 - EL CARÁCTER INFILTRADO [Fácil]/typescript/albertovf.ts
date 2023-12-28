const reto = (cadena1: string, cadena2: string): string[] | Error => {
	let diferencias = new Array<string>();

	try {
		if (cadena1.length != cadena2.length) throw new Error("Las cadenas tienen que ser de la misma longitud")
		if (typeof (cadena1) != typeof (cadena2)) throw new Error("Las cadenas deben ser del mismo tipo");
	} catch (error) {
		console.error(error.message);
		return error;
	}

	for (let i = 0; i < cadena1.length; i++) {
		if (cadena1[i] != cadena2[i]) {
			diferencias.push(cadena2[i])
		}
	}

	console.log(diferencias);
	return diferencias
}

reto("Me llamo mourdev", "Me llemo mouredov")
reto("Me llamo.Brais Moure", "Me llamo brais moure")