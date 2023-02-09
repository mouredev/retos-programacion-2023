fun main() {

    /*
    * Reto #6 06/02/2023
    *
    * Piedra, Papel, Tijera, Lagarto, Spock
    *
    * Crea un programa que calcule quien gana más partidas al piedra,
    * papel, tijera, lagarto, spock.
    * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    * - La función recibe un listado que contiene pares, representando cada jugada.
    * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
    *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
    * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
    * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
    *
    *   Tijera corta a papel,
    *   papel tapa a piedra,
    *   piedra aplasta a lagarto,
    *   lagarto envenena a Spock,
    *   Spock rompe a tijera,
    *   tijera decapita a lagarto,
    *   lagarto devora a papel,
    *   papel desautoriza a Spock,
    *   Spock vaporiza a piedra,
    *   y como siempre, piedra aplasta a tijera"
    *
    * */

    val opciones = listOf("✂", "📄", "🗿", "🦎", "🖖")
    val reglasGanadoras = mapOf(
        "✂" to setOf("📄", "🦎"),
        "📄" to setOf("🗿", "🖖"),
        "🗿" to setOf("🦎", "✂"),
        "🦎" to setOf("🖖", "📄"),
        "🖖" to setOf("✂", "🗿")
    )

    //
    // Creamos una partida aleatoria de 10 jugadas
    //
    var jugada = Pair("piedra", "piedra")
    val jugadas = mutableListOf(jugada)

    (0 until 10).forEach { numero ->
        jugada = Pair(opciones.random(), opciones.random())
        jugadas.add(jugada)
    }

    var puntosJugador1 = 0
    var puntosJugador2 = 0

    jugadas.forEach { jugada ->
        // print("${jugada.first} contra ${jugada.second} => ")
        if (jugada.first != jugada.second) {
            if (reglasGanadoras.get(jugada.first)?.contains(jugada.second) == true) {
                //println("gana ${jugada.first}")
                puntosJugador1++

            } else {
                //println("gana ${jugada.second}")
                puntosJugador2++

            }

        //} else {
        //    println("empate")
        }

    }

    //println("Jugador 1 : ${puntosJugador1}")
    //println("Jugador 2 : ${puntosJugador2}")

    if (puntosJugador1 > puntosJugador2) {
        println("Player 1")
    } else if (puntosJugador2 > puntosJugador1) {
        println("Player 2")
    } else {
        println("Tie")
    }

}