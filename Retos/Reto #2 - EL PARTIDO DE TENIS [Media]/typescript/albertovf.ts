const puntoPartido = (points: number):String => {
	const PUNT = ['Love', '15', '30', '40', 'Deuce']
	return PUNT[points]
}

const partido = (sets: String[]) => {
	let p1 = 0, p2 = 0;

	sets.forEach(function (punto) {
		if (punto == 'P1') p1++;
		else if (punto == 'P2') p2++;

		if (p1 == p2 && p1 == 3) {
			console.log(puntoPartido(4))
		}
		else if (p1 <= 3 && p2 <= 3) {
			console.log(`${puntoPartido(p1)} - ${puntoPartido(p2)}`)
		} else {
			if (p1 - 1 == p2) {
				console.log('Ventaja P1')
			} else if (p2 - 1 == p1) {
				console.log('Ventaja P2')
			} else {
				if (p1 > p2) console.log('Ha ganado el P1')
				else if (p2 > p1) console.log('Ha ganado el P2')
				else console.log(puntoPartido(4));
			}
		}
	});

}

const checkJugadores = (sets: String[]) => {
	if (new Set(sets).size != 2) {
		throw new Error('Invasion de pista. Hay demasiados jugadores')
	}
}


const reto = () => {
	try {
		let sets = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
		checkJugadores(sets)
		partido(sets);
	} catch (error) {
		console.error(error.message);
	}
};

reto();