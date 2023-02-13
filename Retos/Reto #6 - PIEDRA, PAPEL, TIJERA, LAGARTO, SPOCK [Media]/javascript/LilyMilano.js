/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🦎" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
// ......................................................

//? Sheldon Game: Rock, Paper, Scissors, Lizard, Spock.
//? Functional requirements:______________________________

//? Sheldon himself explained it as follows:
// " The scissors cut the paper.
// The paper covers the rock.
// The rock crushes the lizard.
// The lizard poisons Spock.
// Spock breaks the scissors.
// The scissors decapitate the lizard.
// The lizard devours the paper.
// The paper disempowers Spock.
// Spock vaporises the rock and, as always,
// the rock crushes the scissors."

const win_moves = {
	'🗿': ['✂️', '🦎'],
	'📄': ['🗿', '🖖'],
	'✂️': ['🦎', '📄'],
	'🦎': ['🖖', '📄'],
	'🖖': ['✂️', '🗿'],
};

//? Scoring Logic_________________________________________

let sheldon_score = 0;
let leonard_score = 0;

function coopersGame(moves) {
	sheldon_score = 0;
	leonard_score = 0;

	moves.forEach(playGame);
	{
		if (sheldon_score === leonard_score) {
			return 'Tie!';
		} else if (sheldon_score > leonard_score) {
			return 'Sheldon won!';
		} else return 'Leonard won!';
	}
	// ___________________________________________________
}

function playGame([sheldon, leonard]) {
	if (win_moves[sheldon].indexOf(leonard) > -1) {
		sheldon_score += 1;
	} else if (win_moves[leonard].indexOf(sheldon) > -1) {
		leonard_score += 1;
	}
}
//? Testing results_________________________________________

console.log(
	coopersGame([
		['🗿', '✂️'],
		['✂️', '🗿'],
		['📄', '✂️'],
	])
); // Log: Leonard won!

console.log(
	coopersGame([
		['🗿', '✂️'],
		['✂️', '🗿'],
		['📄', '📄'],
	])
); // Log: Tie!

console.log(
	coopersGame([
		['🗿', '✂️'],
		['🦎', '📄'],
		['✂️', '🦎'],
	])
); // Log: Sheldon won!
