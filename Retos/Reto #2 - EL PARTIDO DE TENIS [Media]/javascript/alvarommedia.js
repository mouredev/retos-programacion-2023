const juegos = [];
const puntos = ["Love", "15", "30", "40", "Deuce", "Ventaja", "Ha ganado"];
let player1 = 0;
let player2 = 0;

function partido() {
	juegos.forEach(mostrarPuntuacion);
}

const mostrarPuntuacion = (value, index) => {
	if (value === "P1") {
		player1 += 1;
	} else if (value === "P2") {
		player2 += 1;
	} else {
		console.log("Jugada no Valida");
	}
	if (player1 >= 4 && player2 >= 4 && player1 === player2) {
		console.log(puntos[4]);
	} else if (player1 <= 3 && player2 <= 3) {
		console.log(`${puntos[player1]} - ${puntos[player2]}`);
	} else if (
		(player1 === 3 || player2 === 3) &&
		(player1 === 4 || player2 === 4)
	) {
		console.log(`Ventaja de ${value}`);
	} else {
		console.log(`Ha ganado ${value}`);
	}
};

partido();