
val jugadores = listOf("P1", "P2")

fun main(){
    var activeGame = true

    val secuencia = listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1", "P1")

    var i = 0
    val marcador= mutableMapOf<String, Int>()
    marcador.put(jugadores[0], 0)
    marcador.put(jugadores[1], 0)

    while (activeGame){
        // Corrobora que no se haya recorrido toda la secuencia
        if (i >= secuencia.size) break

        // Se asigna variable de la secuencia. Esto y la lista secuencia se podría reemplazar
        // por una respuesta del usuario
        val jugador = secuencia[i]
        i++

        // Corrobora que el dato sea correcto
        if (!jugadores.contains(jugador)) {
            println("Ingresa Datos correctos para el juego [P1 / P2]")
            break
        }

        marcador[jugador]?.apply {
            marcador[jugador] = marcador[jugador]!! + 1
        }

        val textoMarcador = marcador(marcador)
        if (textoMarcador.contains("Ha ganado") ){
            activeGame = false
        }
        println(textoMarcador)

    }

}


fun marcador(marcador: MutableMap<String, Int>): String{
    val puntuaciones = listOf("Love", "15", "30", "40")
    var textoMarcador = ""

    val puntuacionP1 = marcador[jugadores[0]] ?: 0
    val puntuacionP2 = marcador[jugadores[1]] ?: 0
    val diference = puntuacionP1 - puntuacionP2

    when {
        diference > 0 -> { // P1 es Mayor
            if (diference >= 2 && puntuacionP1 >= 3){
                textoMarcador = "Ha ganado P1"
            } else if (puntuacionP2 >= 3 && diference == 1){
                textoMarcador = "Ventaja P1"
            } else{
                textoMarcador = "${puntuaciones[puntuacionP1]} - ${puntuaciones[puntuacionP2]}"
            }
        }
        diference < 0 -> { // P2 es Mayor
            if (diference <= -2 && puntuacionP2 >= 3){
                textoMarcador = "Ha ganado P2"
            } else if (puntuacionP1 >= 3 && diference == -1){
                textoMarcador = "Ventaja P2"
            } else {
                textoMarcador = "${puntuaciones[puntuacionP1]} - ${puntuaciones[puntuacionP2]}"
            }
        }
        diference == 0 -> { // P1 es igual a P2
            if (puntuacionP1 >= 3) {
                textoMarcador = "Deuce"
            } else {
                textoMarcador = "${puntuaciones[puntuacionP1]} - ${puntuaciones[puntuacionP2]}"
            }
        }
    }

    return textoMarcador
}

