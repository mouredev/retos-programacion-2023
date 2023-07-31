/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

const cadena1 = "Me llamo mouredev";
const cadena2 = "Me llemo mouredov";
const cadena3 = "Me llamo.Brais Moure";
const cadena4 = "Me llamo brais moure";

const buscaDif = (str1, str2) => {
	console.log("\n");
	console.log(str1);
	console.log(str2);
	if (str1.length !== str2.length) return "No tienen la misma longitud\n"
	let i = 0;
	let arr = [];
	while (i < str1.length) {
		if (str1.charAt(i) !== str2.charAt(i)) {arr.push(str2.charAt(i))}
		i++;
	}
	return arr
}

console.log(buscaDif(cadena1, cadena2)); //["e","o"]
console.log(buscaDif(cadena3, cadena4)); //[" ", "b", "m"]
console.log(buscaDif(cadena1, cadena4)); //No tienen la misma longitud

