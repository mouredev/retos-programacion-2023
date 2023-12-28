const TEMPERATURA = 27;
const LLUVIA = 35;

const aleatorio = (): number => {
	let r: number = Math.random() * 100;
	return r
}

const reto = (nDias, T_INICIAL: number = TEMPERATURA, P_LLUVIA: number = LLUVIA) => {
	let temperatura = T_INICIAL;
	let lluvia = P_LLUVIA;
	let t_maxima = T_INICIAL;
	let t_minima = T_INICIAL;
	let dias_lluviosos = 0;
	for (let dia = 0; dia < nDias; dia++) {
		console.log(`${dia + 1}: ${temperatura}ºC ; ${lluvia}%`);
		if (temperatura > t_maxima) {
			t_maxima = temperatura;
		} else if (temperatura < t_minima) {
			t_minima = temperatura;
		}

		if (aleatorio() >= 90) {
			temperatura += 2;
		} else if (aleatorio() <= 10) {
			temperatura -= 2;
		}

		if (temperatura > 25) {
			lluvia *= 1.2;
		} else if (temperatura < 5) {
			lluvia *= 0.8;
		}
		if (lluvia >= 100) {
			dias_lluviosos++;
			temperatura--;
			lluvia = 100;
		}
		lluvia = Math.round(lluvia);
	}
	console.log({ dias_lluviosos, t_maxima, t_minima });
}

reto(365);