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

function tennis(arr) {
    const points = ["Love", 15, 30, 40, "Deuce", "Ventaja"]

    let P1 = 0
    let P2 = 0

    arr.forEach(Punto => {
        if (Punto === 'P1') P1 += 1
        else if (Punto === 'P2') P2 += 1

        if (P1 >= 3 && P2 >= 3) {
            if (P1 === 3 && P2 === 3) console.log('Deuce')
            else if (Math.abs(P1 - P2) === 1) console.log(`Ventaja para ${P1 > P2 ? 'P1' : 'P2'}`)
            else if (Math.abs(P1 - P2) === 2) console.log(`Ha ganado ${P1 > P2 ? 'P1' : 'P2'}`)
        }
        else if (P1 > 3 || P2 > 3) console.log(`Ha ganado ${P1 > P2 ? 'P1' : 'P2'}`)
        else if (P1 == P2) console.log(`Empate`)
        else console.log(`${points[P1]}/${points[P2]}`)
    })

}

console.log(tennis(['P1', 'P1', 'P1', 'P1']))
console.log(tennis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']))