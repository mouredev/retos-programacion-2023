/* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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

const points = {
    0: 'Love',
    1: 15,
    2: 30,
    3: 40,
    4: 50,
    5: 'Ventaja'
}

function tennis(playersPoints){
    let count1 = 0
    let count2 = 0

    for(let i=0; i<playersPoints.length; i++){
        if(playersPoints[i]=='P1') count1++
        else count2++

        if(count1==4 || count2==4){
            const winner = (count1==4)?'P1':'P2'
            console.log(`Ventaja ${winner}`)
            console.log(`Ha ganado el ${winner}`)
            break
        }else{
            console.log(`${(count1==3 && count2==3)? 'Deuce' : points[count1] +' - ' +points[count2]}` )
        }
    }
}

const pointsPlayers = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
tennis(pointsPlayers)