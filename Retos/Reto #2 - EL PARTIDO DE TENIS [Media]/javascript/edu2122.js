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

const Player = {
    P1: 1,
    P2: 2
};

function tenisGame(points) {
    game = ['Love', 15, 30, 40, 'Deuce', 'Ventaja'];
    let p1Points = 0;
    let p2Points = 0;
    let finished = false;
    let error = false;

    for( const player of points) {
        error = finished;

        p1Points = (player == Player.P1) ? p1Points + 1 : p1Points;
        p2Points = (player == Player.P2) ? p2Points + 1 : p2Points;
        
        if (p1Points >= 3 && p2Points >= 3) {

            if (!finished && Math.abs(p1Points - p2Points) <= 1) {
                if (p1Points == p2Points) {
                    console.log(game[4]);
                } else if (p1Points > p2Points) {
                    console.log(game[5], 'P1');
                } else {
                    console.log(game[5], 'P2');
                }
            } else {
                finished = true;
            };
            
        } else{
            if (p1Points < 4 || p2Points < 4) {
                console.log(game[p1Points], '-', game[p2Points]);
            } else{
                finished = true;
            };
        };
    };
    if (error) {
        console.log("Los puntos jugados no son correctos"); 
     } else{
         if (p1Points > p2Points){
             console.log("Ha ganado el P1");
         } else {
             console.log("Ha ganado el P2");
         };
     };
};

tenisGame([Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1]);