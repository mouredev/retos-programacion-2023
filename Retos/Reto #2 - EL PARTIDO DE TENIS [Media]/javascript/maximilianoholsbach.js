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

const valores = [15,30,40,"deuce","love","ventaja","ganador"]
const player1 = [] 
const player2 = [] 

function tennis(P1,P2){
    try {
        for(let i = 0; i < P1.length; i++){
            if(!(valores.includes(P1[i]))){
                throw new Error(`Valores invalidos`);
            }
            player1.push(P1[i])
        }
        for(let j = 0; j < P2.length; j++){
            if(!(valores.includes(P2[j]))){
                throw new Error(`Valores invalidos`);
            }
            player2.push(P2[j])
        }
        return `Player 1 : ${player1}, Player 2 : ${player2}`
    } catch (error) {
        return error.message
    }
}

console.log(tennis([15,30,30,40,"deuce","ventaja","ganador"], ["love","love",15,30,30]))

