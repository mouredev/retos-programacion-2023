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

const scores = ["Love", "15", "30", "40"];

class Player{
    constructor(){
        this.score = "Love";
        this.value = 0;
    }

    updateScore(){
        if(this.value < 4) this.score = scores[this.value];
        else this.score = scores[3];
    }
}

function checkWinner(p1, p2){
    if(p1.value === 3 && p2.value === 3){
        console.log("Deuce");
    } else if(p1.value >= 4 || p2.value >= 4){
        let pointsDifference = p1.value - p2.value;

        if(pointsDifference === 0) console.log("Deuce");
        else if(pointsDifference === 1) console.log("Ventaja P1");
        else if(pointsDifference === -1) console.log("Ventaja P2");

        else if(pointsDifference >= 2){
            console.log("Ha ganado el P1");
            return true;
        }
        else{
            console.log("Ha ganado el P2");
            return true;
        } 
    } else{
        console.log(`${p1.score} - ${p2.score}`);
    }

    return false;
}

function tennisMatch(points){
    const player1 = new Player();
    const player2 = new Player();
    let endMatch = false;

    console.log("\nRESULTADO DEL PARTIDO:\n")
    for(let point of points){
        // por si ya hay ganador pero se han introducido más datos
        if(endMatch){
            console.log("\nYA HAY GANADOR!\nNo se tendrán en cuenta los puntos restantes!\n");
            break;
        }

        try {
            if(point === "P1"){
                player1.value++;
                player1.updateScore();
            } else if(point === "P2"){
                player2.value++;
                player2.updateScore();
            } else{
                throw new Error(`El dato ${point} no es correcto.`)
            }
        } catch (error) {
            console.error(error);
            break;
        }

        endMatch = checkWinner(player1, player2);
    }
}

tennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
tennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2"]);
tennisMatch(["P2", "P3", "P1", "P1", "P2", "P1", "P2", "P2"]);
tennisMatch(["P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2"]);