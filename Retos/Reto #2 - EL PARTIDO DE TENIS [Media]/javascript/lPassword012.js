// The tennis function generates the game sequence.
let tennis = function( maxRounds ) {

    let game = []; // The full round of the game.
    let option = 0;

        alert('Which player starts the game ?');

        while ( maxRounds > 0 ) {

            // User selects which player starts the game.
            option = parseInt(prompt(' Player 1 or Player 2: '));

            alert('Which player continues next turn ? ');
            
            if (option == 1 || option == 2) {

                if ( option == 1 ) {

                    game.push(option);
    
                } else {
    
                    game.push(option);
    
                }

            }else {

                alert('!Error');
                option = parseInt(prompt('enter only, Player 1 or Player 2: '));
            }

            maxRounds--; // End of loop.
        }

    return game;
}

// The gameScore function generates the game score.
let gameScore = function() {

    // The user enters the number of game rounds.
    let rounds = parseInt(prompt('Enter the number of game rounds: '));
    let point = 0;
    let games = {};

    if (rounds != 0) {

        let game = tennis(rounds); 

        let points = game.map(player => {

            point = parseInt(prompt(`Enter player score: ${player}`));

            return point;
        });

       games = { game, points }; // The game round and the player's points are stored.

    } else {

        alert('Error! enter a number greater than zero.');
    }

    return games;
}

// The winner function gets the final result.
let winner = function() {

    let games = gameScore(); // It calls the function gameScore and this function calls the function tennis.
    let player1 = 0;
    let player2 = 0;

    // Points are accumulated for each player.
    for (let i = 0; i < games.game.length; i++) {
        if (typeof(games.points[i]) == 'number') {
            if (games.game[i] == '1') {
                player1 += games.points[i];
            } else {
                player2 += games.points[i];
            }
        }
    }

    // Gets the end result of the game.
    if (player1 == player2) {
        alert('Duce')
    } else if (player1 > player2) {
        alert('Ha ganado Player 1');
    } else {
        alert('Ha ganado Player 2');
    }
}