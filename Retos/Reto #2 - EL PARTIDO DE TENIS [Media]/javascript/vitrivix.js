let partido2 = ['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2']
let partido = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2'];
let points = ['Love', 15, 'Deuce', 'Ventaja => Player 1', 'Ventaja => Player 2', 'Ha ganado Player 1', 'Ha ganado player 2'];

function tenissSofware(date){
    let player1 = 0, player2 = 0 , result = [];
    for (const element of date) {
        if(element === "P1") {
            player1 += points[1]
            if (player1 === 55 && player2 === 55) {
                player1 -= 15;
                player2 -= 15;
            }
            if (player1 === 45) player1 -= 5;
            if (player1 === 40 && player2 === 40 && player1 === player2) result.push(points[4]);
            if (player1 === 55) result.push(points[5]);
            if (player1 === 70) result.push(points[7]);
            if (player1 && !player2) result.push(`${player1} - ${points[0]}`);
            if (player1 && player2){
                if (player1 < 45 && player2 < 40) result.push(`${player1} - ${player2}`);
            };
        };
        if(element === "P2") {
            player2 += points[1];
            if (player1 === 55 && player2 === 55) {
                player1 -= 15;
                player2 -= 15;
            }
            if (player2 === 45) player2 -= 5;
            if (player1 === 40 && player2 === 40 && player1 === player2) result.push(points[4]);
            if (player2 === 55) result.push(points[6]);
            if (player2 === 70) result.push(points[8]);
            if (!player1 && player2) result.push(`${points[0]} - ${player2}`);
            if (player1 && player2){
                if (player1 < 40 && player2 < 45) result.push(`${player1} - ${player2}`);
            };
        };
    } return result;
};
tenissSofware(partido)
tenissSofware(partido2)