/* Hola Moure, Soy perroMandril en Twitch. 
 * Este año me he propuesto aprender a programar aplicaciones android y tus retos semanales me parecen una buena forma de coger ritmo,
 * asi que aqui va mi primer reto semanal. 
 * Espero que no sea un desastre.
 * P.D: agradecería cualquier crítica para mejorar las buenas prácticas y demás
 * Un saludo!package
 */

//Empieza el partido (los puntos se pasan como argumentos de entrada del programa: separados por espacios)
fun main(puntos: Array<String>) {
	var jugador1 = 0
	var jugador2 = 0
    val puntosIterator = puntos.iterator()

	while (puntosIterator.hasNext()) {
		when (puntosIterator.next()) {
            "P1" -> jugador1++
            "P2" -> jugador2++
            else -> {
                println("Parámetros de entrada incorrectos: Solo se admiten los valores 'P1' o 'P2'. Vuelve a intentarlo")
                break
            }
        }
        var estadoPartido = actualizarMarcador(jugador1, jugador2) //esta variable se usa para controlar la situación del partido (Deuce o Juego ganado)
        println(estadoPartido)
        if (estadoPartido.equals("Deuce")){
        	jugador1 = 3
            jugador2 = 3
        }
        if (estadoPartido.startsWith("Ha ganado"))
            break
    }
}

fun actualizarMarcador(jugador1: Int, jugador2: Int): String {

        val puntuacion = mutableMapOf(
            0 to "Love",
            1 to "15",
            2 to "30",
            3 to "40",
        )

        if ((kotlin.math.abs(jugador1 - jugador2) > 1) && (jugador1 > 3 || jugador2> 3)){
            if (jugador1 > jugador2) {
                return "Ha ganado P1"
            } else return "Ha ganado P2"
        }
        else{
            if ((jugador1 == jugador2)) {
                if (jugador1 > 2) {
                    return "Deuce"
                }
            }
            else{
                if (jugador1 == 4)
                    return "Ventaja para P1"
                else if (jugador2 == 4)
                    return "Ventaja para P2"
            }
        }
        return (puntuacion[jugador1] + "-" + puntuacion[jugador2])
}