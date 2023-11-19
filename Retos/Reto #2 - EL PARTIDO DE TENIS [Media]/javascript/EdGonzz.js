/* Reto #2: EL PARTIDO DE TENIS
Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

Enunciado

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


let marcador = ['Love', 15, 30, 40, 'Deuce', 'Ventaja']

function tenisGame(arr) {
    let p1 = 0
    let p2 = 0

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 'P1') {
            p1++
        } else if (arr[i] === 'P2') {
            p2++
        } else {
            console.log(`Jugadores no Validos`);
            break
        }

        if (marcador[p1] === 40 && marcador[p2] === 40) {
            console.log(marcador[4]);
        } else if (p1 > 3) {
            console.log(`${marcador[5]} P1`);
            break
        } else if (p2 > 3) {
            console.log(`${marcador[5]} P2`);
            break
        }else {
            console.log(`${marcador[p1]} - ${marcador[p2]}`);
        }
    }
    if (p1 > p2) {
        console.log('Ha ganado el P1');
    } else if(p2 > p1) {
        console.log('Ha ganado el P2');
    }
}

tenisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
tenisGame(['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2'])
tenisGame(['P3', 'P4', 'P3', 'P4', 'P4', 'P3', 'P3', 'P4'])