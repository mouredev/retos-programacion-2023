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

function playtennis(game){
    let adventage = false;
    let score = [0, 0]
    let points = ["Love", 15, 30, 40, "Deuce", "Ventaja"]
    let gameSecuency = [];
    game.forEach(element => {
        if(element !== "P1" && element !== "P2") return;
        let player = element.includes("1") ? 0 : 1;
        score[player] += 1;
        if(score[0] === 3 && score[1] === 3){
            adventage = true;
            gameSecuency.push("Deuce")
        } 
        else if(adventage && score[0] === 4) {
            gameSecuency.push(`Ventaja P${player + 1}`)
        }
        else if(adventage && score[0] === 5){
            gameSecuency.push(`Ha ganado el P${player + 1}`)
        }
        else{
            gameSecuency.push(points[score[0]] + " - " + points[score[1]])
        }
    });

    return gameSecuency;
}

// console.log(playtennis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]));