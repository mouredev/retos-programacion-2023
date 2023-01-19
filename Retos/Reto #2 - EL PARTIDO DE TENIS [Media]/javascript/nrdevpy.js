function tenis(game) {
    const everyArePlayer = game.filter(elem => elem === ('P1' || 'P2'));
    game = game.map(play => play.toUpperCase());
    if (everyArePlayer) {
        const scoreMsg = ['Love', '15', '30', '40', 'Ad-In', 'Win !!!'];
        let scoreP1 = 0;
        let scoreP2 = 0;
        for (let play of game) {
            // Increment score.
            play === 'P1'
                ? ++scoreP1
                : ++scoreP2;
            // Conditions
            const winner = (scoreP1 || scoreP2) === 5;
            const isAddIn = (scoreP1 || scoreP2) === 4;
            const isDeuce = (scoreP1 && scoreP2) === 3;
            if (winner) {
                play === 'P1'
                    ? console.log(play, scoreMsg[scoreP1])
                    : console.log(play, scoreMsg[scoreP2]);
                break;
            }
            else if (isAddIn) {
                play === 'P1'
                    ? console.log(play, scoreMsg[scoreP1])
                    : console.log(play, scoreMsg[scoreP2]);
            }
            else if (isDeuce) {
                console.log('Deuce');
            }
            else if (scoreP1 + scoreP2 === game.length && (scoreP1 || scoreP2) !== 5) {
                console.log('Not enough rounds to have a winner. Try again!');
            }
            else {
                console.log(`${scoreMsg[scoreP1]} - ${scoreMsg[scoreP2]}`);
            }
        }
    }
    else {
        console.log('Inputs must to be "P1" or "P2"');
    }
}
const situations = [
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1',],
    ['P1', 'P1', 'P2', 'P2', 'P1'],
    ['P1', 'P2', 'p1', 'P2', 'p1', 'P2', 'p1', 'P2', 'p2'],
];
for (let situation of situations.entries()) {
    console.log(`\nGame: ${situation[0] + 1}`);
    tenis(situation[1]);
}
