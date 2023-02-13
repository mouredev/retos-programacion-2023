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

const game: Array<string> = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1","P2", "P1", "P1"];
// const game: Array<string> = ["P2", "P2", "P2", "P2", "P2", "P2", "P2", "P2"];
const points: Array<string> = ["Love", "15", "30", "40", "", "Ventaja"];
var P1: number = 0;
var P2: number = 0;
var deuceMode: boolean = false;

function printResult(P1: number, P2: number): void{
    if (P1 === 4 && P2 === 4) {
        console.log("Deuce");
        deuceMode = true;
        return;
    } else if (deuceMode && (P1 === 6 || P2 === 6) ||
        !deuceMode && (P1 === 4 || P2 === 4)){
        console.log("Ha ganado el " + ((deuceMode && P1 === 6 || !deuceMode && P1 === 5 )? "P1" : "P2"))
        return;
    } 
    if (deuceMode && (P1 === 5 && P2 === 4 || P2 === 5 && P1 === 4)) {
        console.log(points[5] + (P1 > 4 ? " P1" : " P2"));
        return;
    } else {
        console.log(points[P1] + "-" + points[P2]);
    }
}

function startGame(game: Array<string>): void {
    game.some((point, index) => {
        point === "P1" ? P1++ : P2++; 
        if(P1 === 3 && P2 === 3) {
            P1++;
            P2++;
        } 
        if(P1 === 5 && P2 === 5){
            P1--;
            P2--;
        }
        printResult(P1,P2);
        if ((deuceMode && (P1 === 6 || P2 === 6)) ||
        (!deuceMode && (P1 === 4 || P2 === 4)) ||
         (index + 1) === game.length) return true;
    });
}

startGame(game);