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
const P1 = "P1"
const P2 = "P2"
let secuenciaDeEj = [P1, P1, P2, P2, P1, P2, P1, P1]
const puntuacionJugador = {
    0: "love",
    1: 15,
    2: 30,
    3: 40,
    4: 50
}
let jugador1 = 0
let jugador2 = 0

const establecerResultados = (resultadoJugador) => {
    let resultado = resultadoJugador.toString()
    for (puntos in puntuacionJugador) {
        if (resultado === puntos) {
            let resultadoValue = puntuacionJugador[puntos]
            return resultadoValue
        }
    }
}

const JugarPartido = (secuencia) => {

    for (let i = 0; i < secuencia.length; i++) {
        let set = secuencia[i]
        set === P1 ? jugador1 += 1 : jugador2 += 1

        let resultadosJ1 = establecerResultados(jugador1)
        let resultadosJ2 = establecerResultados(jugador2)

        if (((jugador1 - jugador2) >= 2) && (i >= 4)) {
            console.log("ganador del partido es P1")
        }
        else if ((jugador2 - jugador1 >= 2) && (i >= 4)) {
            console.log("ganador del partido es P2")
        }

        else if (((resultadosJ1 === 40) && (resultadosJ2 === 50)) | ((resultadosJ1 === 50) && (resultadosJ2 === 40))) {
            let jugadorConVentaja = (Math.max(resultadosJ1, resultadosJ2) === resultadosJ1) ? "P1" : "P2"
            console.log(`el jugador con ventaja es ${jugadorConVentaja}`)
        }
        else if ((resultadosJ1 === 40) && (resultadosJ2 === 40)) {
            console.log("Deuce")
        }
        else {
            console.log(resultadosJ1 + " - " + resultadosJ2)
        }
    }

}


JugarPartido(secuenciaDeEj)