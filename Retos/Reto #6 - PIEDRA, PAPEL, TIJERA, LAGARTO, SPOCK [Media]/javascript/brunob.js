const PLAYER_1 = 0;
const PLAYER_2 = 1;
const TIE = 2;

function solve (player1, player2) {
	let tablet = [
		['', 'paper', 'rock', 'rock', 'spock'],
		['paper', '', 'scissors', 'lizard', 'paper'],
		['rock', 'scissors', '', 'scissors', 'spock'],
		['rock', 'lizard', 'scissors', '', 'lizard'],
		['spock', 'paper', 'spock', 'lizard', '']
	];

	let ref = {
		'rock': 0,
		'paper': 1,
		'scissors': 2,
		'lizard': 3,
		'spock': 4
	};
	
	return tablet[ref[player1]][ref[player2]];
}

function result (game) {
	let scores = [0, 0, 0];

	game.forEach((match) => {
		let res = solve(match[PLAYER_1], match[PLAYER_2]);
		if (res == match[PLAYER_1]) {
			scores[PLAYER_1]++;
		} else {
			if (res == match[PLAYER_2]) {
				scores[PLAYER_2]++;
			} else {
				scores[TIE]++;
			}
		}
		});

	return scores;
}

function who_win (scores) {
	if (scores[PLAYER_1] > scores[PLAYER_2] && scores[PLAYER_1] > scores[TIE]) {
		return "Player 1 win";
	} else {
		if (scores[PLAYER_2] > scores[TIE])
			return "Player 2 win";
		else
			return "Tie";
	}	
}

let game = [
	['scissors', 'scissors'],
	['paper', 'rock'],
	['rock', 'rock'],
	['spock', 'spock'],
	['rock', 'paper']
	];
who_win(result(game));