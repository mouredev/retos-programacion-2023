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


puntuaciones = ["Love", "15", "30", "40"]
jugador_actual = ""

function jugar_tenis(secuencia){
    score_p1 = 0
    score_p2 = 0
    for (let i = 0; i < secuencia.length; i++){
        let jugada = secuencia[i];
        if (jugada === "P1") {
            score_p1 += 1
        }else if(jugada === "P2") {
            score_p2 += 1
        } else {
            console.error("Error: Entrada inválida")
            return
        }
        puntuacion_actual = mostrar_puntuacion(score_p1, score_p2)
        console.log(puntuacion_actual)
        if ("Ha ganado" === puntuacion_actual)
            break
    }
    return
}

function mostrar_puntuacion (score_p1, score_p2){
    if (score_p1 === score_p2){
        if(score_p1 < 3)
            return puntuaciones[score_p1] +" -All";
        else 
            return "Deuce"  
    }else if(score_p1 >= 4 || score_p2 >= 4){
        diff = Math.abs(score_p1 - score_p2)
        if(diff == 1)
            return "Ventaja"
        else
            return "Ha ganado "
    }else{
        return puntuaciones[score_p1] + " - " +puntuaciones[score_p2]
    }   
}



secuencia_juego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]


jugar_tenis(secuencia_juego)