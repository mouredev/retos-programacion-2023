function tenis(game: string[]) {
    const everyArePlayer = game.filter(elem => elem === ('P1' || 'P2'));
    game = game.map(play => play.toUpperCase())

    if (game.length === 8 && everyArePlayer) {
        const scoreMsg = ['Love', '15', '30', '40', 'Ad-In', 'Win !!!'];
        let scoreP1 = 0;
        let scoreP2 = 0;
        
        for (let play of game) {
            // Increment score.
            play === 'P1'
            ? ++scoreP1
            : ++scoreP2;

            // Conditions
            const winner = (scoreP1 || scoreP2) === 5
            const isAddIn = (scoreP1 || scoreP2) === 4
            const isDeuce = (scoreP1 && scoreP2) === 3
            
            if (winner){
                play === 'P1'
                ? console.log(play, scoreMsg[scoreP1])
                : console.log(play, scoreMsg[scoreP2])
                break;
            } else if (isAddIn){
                play === 'P1'
                ? console.log(play, scoreMsg[scoreP1])
                : console.log(play, scoreMsg[scoreP2])
            } else if (isDeuce) {
                console.log('Deuce')
            } else {
                console.log(`${scoreMsg[scoreP1]} - ${scoreMsg[scoreP2]}`)
            }
            
        }
    } else if (game.length < 8) {
        console.log('Not enough input, please introduce exactly 8 inputs to complete the match')
    } else {
        console.log('Inputs must to be "P1" or "P2"')
    }
}

const cases = [
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1',],
    ['P1', 'P1', 'P2', 'P2', 'P1'],
    ['P1', 'P2', 'p1', 'P2', 'p1', 'P2', 'p1', 'P2',],
];

tenis(cases[2])