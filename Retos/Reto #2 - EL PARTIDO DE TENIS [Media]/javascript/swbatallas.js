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

let Jugador1 = 0
let Jugador2 = 0

const SumarPuntos = ({ jugador }) => {
    if (jugador === ("P1" | "P2")) {
    }
};

const CalcularResultado = (jugador) => {
    const ResultadoSegunPuntos = {
        0: "love",
        15: 15,
        30: 30,
        40: 40,
        "empate": "deuce",
        "ventaja": "ventaja"
    }
    for (resultado in ResultadoSegunPuntos) {
        if (jugador === resultado.key) {
        }
        else ("resultado no valido")
    }
}

const JugarSet = (secuencia) => {

    secuencia.map((set) => {
        if (set === "P1") {
            Jugador1 = Jugador1 + 15

        }
        else if (set === "P2") {
            Jugador2 = Jugador2 + 15
        }
        else throw new Error("set no valido")
        CalcularResultado(Jugador1)
    })
}


console.log(JugarSet(["P1", "P1"]))