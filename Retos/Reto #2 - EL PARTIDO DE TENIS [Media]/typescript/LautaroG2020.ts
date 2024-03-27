/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "player1" (Player 1) o "player2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [player1, player1, player2, player2, player1, player2, player1, player1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja player1
 *   Ha ganado el player1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

const scores: { [key: number]: string } = {
  0: "Love",
  1: "15",
  2: "30",
  3: "40",
};

const TennisMach = (match: number, matchPoints : String[]) => {
    let player1Points = 0;
    let player2Points = 0;

    if(matchPoints.length < 3) return console.log("Partido finalizado por falta de datos: Faltan registros para completar el partido.")
    
    for (const win of matchPoints) { 
        if (win == "P1") player1Points++; 
        if (win == "P2") player2Points++; 
        
        if (player1Points >= 4 && player2Points < player1Points - 2) break;
        else if (player2Points >= 4 && player1Points < player2Points - 2) break;

        if(player1Points >= 3 && player2Points >= 3){
            if (IsDeuce(player1Points,player2Points)) console.log("Deuce");
            if (player1Points > player2Points) {
                if (IsWinnerWithAdvantage(player1Points, player2Points)) break;
                else console.log("Ventaja player1");
            };
            if (player2Points > player1Points) {
                if (IsWinnerWithAdvantage(player1Points, player2Points)) break;
                else console.log("Ventaja player2");
            };
        }
        else console.log(`${scores[player1Points]} - ${scores[player2Points]}`)
    }

    if (player1Points > player2Points) console.log(`Partido ${match}: Ha ganado el P1`);
    if (player2Points > player1Points) console.log(`Partido ${match}: Ha ganado el P2`);

    console.log("*********************************Fin Del Partido*********************************");
};

const IsWinnerWithAdvantage  = (player1: number, player2: number) =>{
    if(player1 >= 5){
        if(player1 - 1 > player2) return true;
        else return false;
    }

    if(player2 >= 5){
        if(player2 - 1 > player1) return true;
        return false;
    }

    return false;
};

const IsDeuce = (player1: number, player2: number) => {
    return player1 === player2;
};

//Posibles resultados...
TennisMach(1,["P1", "P1", "P1", "P1", "P1", "P1", "P1", "P1"]);
TennisMach(2,["P2", "P2", "P2", "P2", "P2", "P2", "P2"]);
TennisMach(3,["P1", "P1", "P1", "P2", "P1", "P1", "P1", "P1"]);
TennisMach(4,["P1", "P1", "P1", "P2", "P2", "P2", "P2", "P2"]);
TennisMach(5, ["P1", "P1", "P1", "P2", "P2", "P2", "P2", "P1", "P2", "P2"]);
TennisMach(6, ["P1", "P1", "P1", "P2", "P2", "P2", "P2", "P1", "P2", "P1", "P1", "P1"]);
