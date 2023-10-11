const combinar = (lista: number[]) => {
	const combinaciones: number[][] = [[]];

	for (let i in lista) {
		const value = lista[Number(i)];
		const temp: number[][] = combinaciones.map(
			(combination) => [value, ...combination]
		);
		combinaciones.push(...temp);
	}
	return combinaciones;
};

const sumatorio = (arr: number[]) => arr.reduce((acc, value) => acc + value, 0);

const reto = (numeros: number[], resultado: number) => {
	if (resultado < 1) return [];
	if (numeros.length === 0) return [];
	if (!numeros.every((n) => n >= 0)) return [];


	return combinar(numeros).filter((nms) => sumatorio(nms) === resultado);
}

const list: number[] = [19, 1, 20, 0, 2, 18, 15, 5];
const target: number = 6;

console.log(reto(list, target));