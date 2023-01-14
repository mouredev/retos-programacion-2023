/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

const sistemaPuntosTenis = ['Love', '15', '30', '40']
let numeroJuegosGanadosPlayer1 = 0;
let numeroJuegosGanadosPlayer2 = 0;
let ganadorPartido = false
const secuenciaPartido = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

partido(secuenciaPartido)

function partido(secuenciaPartido) {
	try {
		puntuacionJugadores(secuenciaPartido)
	} catch (error) {
		console.error(error);
	}
}

function puntuacionJugadores(secuenciaPartido) {
	secuenciaPartido.forEach(ganadorJuego => {
		if (ganadorPartido) {
			throw 'Ya existe ganador. La secuencia de puntos del partido no es correcta.'
		}
		if (ganadorJuego == "P1") {
			numeroJuegosGanadosPlayer1++
		} else {
			numeroJuegosGanadosPlayer2++
		}
		mostrarPuntuacionDelJuego(numeroJuegosGanadosPlayer1, numeroJuegosGanadosPlayer2)
	});
}

function mostrarPuntuacionDelJuego(numeroJuegosGanadosPlayer1, numeroJuegosGanadosPlayer2) {
	let mensaje = sistemaPuntosTenis[numeroJuegosGanadosPlayer1] + '-' + sistemaPuntosTenis[numeroJuegosGanadosPlayer2]
	if (numeroJuegosGanadosPlayer1 >= '3' && numeroJuegosGanadosPlayer2 >= '3') {
		if (numeroJuegosGanadosPlayer1 == numeroJuegosGanadosPlayer2) {
			mensaje = 'Deuce'
		} else if (numeroJuegosGanadosPlayer1 > numeroJuegosGanadosPlayer2) {
			mensaje = 'Ventaja P1'
		} else if (numeroJuegosGanadosPlayer1 < numeroJuegosGanadosPlayer2) {
			mensaje = 'Ventaja P2'
		}
	}
	if (numeroJuegosGanadosPlayer1 > '3' && numeroJuegosGanadosPlayer1 - numeroJuegosGanadosPlayer2 >= 2) {
		mensaje = 'Ha ganado el P1'
		ganadorPartido = 'P1'
	}
	if (numeroJuegosGanadosPlayer2 > '3' && numeroJuegosGanadosPlayer2 - numeroJuegosGanadosPlayer1 >= 2) {
		mensaje = 'Ha ganado el P2'
		ganadorPartido = 'P2'
	}
	console.log(mensaje);
}
