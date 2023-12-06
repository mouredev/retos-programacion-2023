function tennisGame (secuencia) {  
    let game = ['Love', '15', '30', '40' ]
    let player1 = 0;
    let player2 = 0;
    let error = false;
    let finish = false;

    console.log('Comienza el partido');
    for (let i = 0; i < secuencia.length; i++) {
        if (secuencia[i] === 'P1') {
            player1++;
        } else if (secuencia[i] === 'P2') {
            player2++;
        } else {
            error = true;
            break;
        }
        if (player1 >= 3 && player2 >=3) { 
            if (player1 == player2) {
                console.log('Deuce');
            }else if (player1 > player2) {
                console.log('Ventaja P1');
                finish = true;
            } else if (player1 < player2) {
                console.log('Ventaja P2');
                finish = true;
            } else { 
                console.log('Error');
            }
        } else if ( player1 <= 3 && player2 <= 3 && !finish) {
            console.log(`${game[player1]} - ${game[player2]}`);
        } else { 
            finish = true;
        }

        if (finish) {
            if (player1 > player2) {
                console.log('Ha ganado el P1');
            } else if (player1 < player2) {
                console.log('Ha ganado el P2');
            } else {
                console.log('Error');
            }
            break;
        }
    }
}
tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);



