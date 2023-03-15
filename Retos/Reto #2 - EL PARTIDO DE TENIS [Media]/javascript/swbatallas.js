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

const Resultados = ["love", 15, 30, 40, "deuce", "ventaja"]
let Jugador1 = 0;
let Jugador2 = 0;

const SumarPuntos = (set) => {
    if (secuencia === "P1") {
        Jugador1 = Jugador1 + 15;
    } else if (secuencia === "P2") {
        Jugador2 = Jugador2 + 15;
    }
};

const JugarSet = (secuencia) => {
    secuencia.map((set) => {
        SumarPuntos(set)
    })
    if (jugador)
}