'use strict';

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
// _______________________________________________________________________

function tennisGame(finalResult) {
	// Players:
	let Serena = 0;
	let Venus = 0;
	//_____________________________________________________________
	let scoreSystem = ['Love', 15, 30, 40, 'Advantage', 'Winner'];

	// Define data entry control
	if (Array.isArray(finalResult)) {
		for (let i = 0; i < finalResult.length; i++) {
			finalResult[i] === 'P1'
				? (Serena += 1)
				: finalResult[i] === 'P2'
				? (Venus += 1)
				: console.log('Wrong value');

			//___Deuce Result:______________________________________
			if (scoreSystem[Serena] === 40 && scoreSystem[Venus] === 40) {
				console.log('Deuce'); // Log: Deuce
			}
			//______________________________________________________
			// Case: When Deuce is reached in a game, the player who wins the next point have 'advantage'.
			//If he wins the next point, he wins the game. If the opposite is the case, both return to the Deuce.
			else if (
				scoreSystem[Serena] === 'Advantage' &&
				scoreSystem[Venus] === 'Advantage'
			) {
				console.log('Deuce');
				Serena -= 1;
				Venus -= 1;
			} else if (
				scoreSystem[Serena] === 'Advantage' ||
				scoreSystem[Venus] === 'Advantage'
			) {
				console.log(Serena > Venus ? 'Advantage Serena' : 'Advantage Venus'); // Log: Advantage Serena
			} else if (
				scoreSystem[Serena] === 'Winner' ||
				scoreSystem[Venus] === 'Winner'
			) {
				console.log(Serena > Venus ? 'Serena won' : 'Venus won'); // Log: Serena won
				break;
			} else {
				console.log(
					` ${scoreSystem[Serena]} -  ${scoreSystem[Venus]}`
					/* Log: 15 -  Love 
                            30 -  Love 
                            30 -  15 
                            30 -  30 
                            40 -  30 */
				);
			}
		}
	} else {
		console.log('Enter the final game result');
	}
}

tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']); //* Array to obtain the expected result.

//*tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2']);
//* Reference: @mariovelascodev code
