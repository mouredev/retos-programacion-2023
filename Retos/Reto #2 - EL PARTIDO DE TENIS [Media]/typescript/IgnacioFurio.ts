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

const match: any = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
const points: any = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40",
    4: "Ventaja",
    5: "Winner"
}

const winner = (match: any) => {
    let players: any = {p1: 0, p2: 0}
    let score: any = []

    for (let i = 0; i < match.length; i++) {
        if (players.p1 < 4 && players.p2 < 4) {
            match[i] === "P1" ? players.p1 ++ : players.p2 ++;

        } else if (players.p1 === 4) {
            match[i] === "P1" ? players.p1 ++ : players.p1 --;           
        } else if (players.p2 === 4) {
            match[i] === "P2" ? players.p2 ++ : players.p2 --;           
        };   
        
        if (players.p1 === 3 && players.p2 === 3) {
            score[i] = {P1: "Deuce", P2: "Deuce"};
        } else {
            score[i] = {P1: points[players.p1], P2: points[players.p2]};
        };
    
        if (players.p1 === 5 || players.p2 === 5) {
            score[i] = {P1: points[players.p1], P2: points[players.p2]};
            break;
        }
    };
    
    return score;
};

winner(match);