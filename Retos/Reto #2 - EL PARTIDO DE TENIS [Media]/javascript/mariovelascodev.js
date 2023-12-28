'use strict'
function matchTennis(arr) {

    //Crear variables y array de puntuaciones
    let player1 = 0;
    let player2 = 0;
    let score = ['Love', 15, 30, 40, 'Advantage', 'Winner'];

    //Comprobar que se ha introducido un array  y si no pedirlo para realizar el juego
    if (Array.isArray(arr)) {

        //Recorrer array de juego de tenis
        for (let i = 0; i < arr.length; i++) {

            //Si el jugador existe sumar 1
            arr[i] === 'P1' ? player1 += 1 : arr[i] === 'P2' ? player2 += 1 : console.log('Valor erroneo');

            //Si ambos jugadores empatan a 40 mostrar el mensaje Deuce
            if (score[player1] === 40 && score[player2] === 40) {
                console.log('Deuce');
                /*Si ambos jugadores tienen la ventaja volver a mostrar el mensaje Deuce
                y retrocer una posición la puntuación de cada jugador*/
            } else if (score[player1] === 'Advantage' && score[player2] === 'Advantage') {
                console.log('Deuce');
                player1 -= 1;
                player2 -= 1;
                //Si cualquiera de los dos jugadores tiene la ventaja mostrar mensaje indicandolo
            } else if (score[player1] === 'Advantage' || score[player2] === 'Advantage') {
                console.log(player1 > player2 ? 'Ventaja P1' : 'Ventaja P2');
                //Si cualquiera de los dos jugadores llega al final del array de score gana el partido
            } else if (score[player1] === 'Winner' || score[player2] === 'Winner') {
                console.log(player1 > player2 ? 'Ha ganado P1' : 'Ha ganado P2');
                break;
                //Mostrar el marcador del partido
            } else {
                console.log(`${score[player1]} - ${score[player2]}`);
            }
        }
    }else {
        console.log('Introduce un array');
    }
}

//matchTennis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
matchTennis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2']);
