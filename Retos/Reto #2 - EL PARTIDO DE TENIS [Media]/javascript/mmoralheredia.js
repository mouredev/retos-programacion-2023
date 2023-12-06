
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
 *  */

function gameResult(pointSequences) {
    const points = { 0: 'love', 1: '15', 2: '30', 3: '40' } //Sistema de puntos del tenis
    let playerOne = 0
    let playerTwo = 0

    for (let point in pointSequences) {
        // Sistema de suma de puntos
        if (pointSequences[point].toUpperCase() === 'P1') {
            playerOne++
        } else if (pointSequences[point].toUpperCase() === 'P2') {
            playerTwo++
        } else if (pointSequences[point].toUpperCase() != 'P1' || pointSequences[point].toUpperCase() != 'P2') {
            // Muestra un mensaje de error en la entrada y sale de la ejecución
            console.log('Error en entrada\n')
            break
        }

        // Sistema de anotación del marcador
        if (playerOne > 3 && playerOne - 2 >= playerTwo || playerTwo > 3 && playerTwo - 2 >= playerOne) {
            // Definiendo si existe un ganador
            console.log(`Punto de ${pointSequences[point].toUpperCase()}\nResultado: Gana ${pointSequences[point].toUpperCase()}\n`)
            break
        } else if (playerOne >= 3 && playerOne === playerTwo) {
            // Definiendo si están en deuce
            console.log(`Punto de ${pointSequences[point].toUpperCase()}\nMarcador: Deuce\n`)
        } else if (playerOne > 3 && playerOne - 1 === playerTwo || playerTwo > 3 && playerTwo - 1 === playerOne) {
            // Definiendo si están en ventajas de definición
            console.log(`Punto de ${pointSequences[point].toUpperCase()}\nMarcador: Ventaja ${pointSequences[point].toUpperCase()}\n`)
        } else {
            // Anotación intermedia de partido
            console.log(`Punto de ${pointSequences[point].toUpperCase()} \nMarcador: ${points[playerOne]} - ${points[playerTwo]}\n`)
        }
    }
}

gameResult(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
