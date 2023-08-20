const rules = {
	'🗿': ['✂️', '🦎'],
	'📄': ['🗿', '🖖'],
	'✂️': ['📄', '🦎'],
	'🦎': ['🖖', '📄'],
	'🖖': ['🗿', '✂️'],
};

const game = (gameSequence) => {
	let message = '';
	let player1 = 0;
	let player2 = 0;
	const winningPoints = 3;

	for (const play of gameSequence) {
		if (player1 < winningPoints && player2 < winningPoints) {
			const [inputPlayer1, inputPlayer2] = play;
			console.log(`${inputPlayer1} | ${inputPlayer2}`);
			rules[inputPlayer1].includes(inputPlayer2) ? player1++ : player2++;
		} else {
			break;
		}
	}

	if (player1 === player2) {
		message = 'Tie';
	} else {
		message = player1 > player2 ? 'Winner is player 1' : 'Winner is player 2';
	}

	console.log(message);
};

const gameSequence = [
	['🗿', '✂️'],
	['✂️', '🗿'],
	['📄', '✂️'],
];

game(gameSequence); // Winner is player 2
