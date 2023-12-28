enum class Jugada {
    PIEDRA,
    PAPEL,
    TIJERAS,
    LAGARTO,
    SPOCK
}

private fun PiedraPapelTijerasLagartoSpock(juegos: List<Pair<Jugada, Jugada>>): String {
    var p1Points = 0
    var p2Points = 0
    val ganador =
            mapOf(
                    Jugada.PIEDRA to listOf(Jugada.TIJERAS, Jugada.LAGARTO),
                    Jugada.PAPEL to listOf(Jugada.PIEDRA, Jugada.SPOCK),
                    Jugada.TIJERAS to listOf(Jugada.PAPEL, Jugada.LAGARTO),
                    Jugada.LAGARTO to listOf(Jugada.PAPEL, Jugada.SPOCK),
                    Jugada.SPOCK to listOf(Jugada.TIJERAS, Jugada.PIEDRA)
            )

    for (juego in juegos) {
        val jugador1 = juego.first
        val jugador2 = juego.second
        if (jugador1 == jugador2) {
            p1Points++
            p2Points++
        } else if (jugador1 in ganador[jugador2]!!) {
            p1Points++
        } else {
            p2Points++
        }
    }

    return if (p1Points == p2Points) "Empate a $p1Points puntos"
    else if (p1Points > p2Points) "Gana el jugador 1 por $p1Points a $p2Points puntos"
    else "Gana el jugador 2 por $p2Points a $p1Points puntos"
}

fun main() {
    println(
            PiedraPapelTijerasLagartoSpock(
                    listOf(
                            Jugada.PIEDRA to Jugada.TIJERAS,
                            Jugada.PIEDRA to Jugada.PAPEL,
                            Jugada.LAGARTO to Jugada.SPOCK
                    )
            )
    )

    println(
            PiedraPapelTijerasLagartoSpock(
                    listOf(
                            Jugada.TIJERAS to Jugada.TIJERAS,
                            Jugada.PIEDRA to Jugada.PAPEL,
                            Jugada.LAGARTO to Jugada.SPOCK,
                            Jugada.PIEDRA to Jugada.PAPEL,
                            Jugada.SPOCK to Jugada.PAPEL,
                            Jugada.LAGARTO to Jugada.LAGARTO,
                            Jugada.SPOCK to Jugada.LAGARTO
                    )
            )
    )
}
