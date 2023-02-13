
class JuegoPiedraPapelTijera {
    val ganadores = mapOf(
        "piedra:tijera" to "Jugador 1 gana",
        "piedra:lagarto" to "Jugador 1 gana",
        "papel:piedra" to "Jugador 1 gana",
        "papel:spock" to "Jugador 1 gana",
        "tijera:papel" to "Jugador 1 gana",
        "tijera:lagarto" to "Jugador 1 gana",
        "lagarto:papel" to "Jugador 1 gana",
        "lagarto:spock" to "Jugador 1 gana",
        "spock:tijera" to "Jugador 1 gana",
        "spock:piedra" to "Jugador 1 gana",
        "piedra:piedra" to "Empate",
        "papel:papel" to "Empate",
        "tijera:tijera" to "Empate",
        "spock:spock" to "Empate",
        "lagarto:lagarto" to "Empate"
    )

    fun jugar(jugadas: List<String>) = jugadas.map { jugada ->
        jugada.split(":")
        ganadores[jugada] ?: "Jugador 2 gana"
    }
}

fun main() {
    val juego = JuegoPiedraPapelTijera()
    val jugadas = listOf(
        "piedra:spock",
        "tijera:tijera",
        "piedra:tijera",
        "lagarto:piedra",
        "spock:lagarto"
    )
    val resultados = juego.jugar(jugadas)

    var totJugador1 = 0
    var totJugador2 = 0
    for (resultado in resultados) {
        println(resultado)
        if (resultado == "Jugador 1 gana") {
            totJugador1++
        } else if (resultado == "Jugador 2 gana") {
            totJugador2++
        }
    }

    println("--------------")
    if (totJugador1 == totJugador2) {
        println("Empate!")
    } else if (totJugador1 > totJugador2) {
        println("Jugador 1 gana!")
    } else {
        println("Jugador 2 gana!")
    }
}