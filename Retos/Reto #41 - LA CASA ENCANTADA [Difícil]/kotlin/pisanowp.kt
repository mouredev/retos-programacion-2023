import kotlin.random.Random

fun main() {

    /*
    * Reto #41 16/10/2023  LA CASA ENCANTADA
    *
    * Este es un reto especial por Halloween.
    * Te encuentras explorando una mansión abandonada llena de habitaciones.
    * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
    * Tu misión es encontrar la habitación de los dulces.
    *
    * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
    * (Tienes total libertad para ser creativo con los textos)
    *
    * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
    *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
    *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
    *   Esta podría ser una representación:
    *   🚪⬜️⬜️⬜️
    *   ⬜️👻⬜️⬜️
    *   ⬜️⬜️⬜️👻
    *   ⬜️⬜️🍭⬜️
    * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
    *   Si no lo aciertas no podrás desplazarte.
    * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
    *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
    * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
    * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
    *   tengas que responder dos preguntas para salir de ella.
    */

    val casa = CasaEncantada()
    println()
    println()
    casa.pintarCasa()

}

class CasaEncantada() {
    private val filas = 4
    private val columnas = 4

    val puerta = "🚪"
    val sala = "⬜"
    val fantasma = "👻"
    val caramelo = "🍭"

    val casa = Array(filas) { Array(columnas) { sala } }

    var jugadorFila = 0
    var jugadorColumna = 0

    val enigmas = listOf(
        Pair("¿Cuánto suman 1+2?", "3"),
        Pair("¿De qué color es el caballo blanco de Santiago?", "blanco"),
        Pair("Tengo agujas, pero no coso. Tengo números, pero no soy un teléfono. ¿Qué soy?", "reloj"),
        Pair("Si me nombras, desaparezco. ¿Qué soy?", "silencio"),
        Pair("Tengo dientes, pero no puedo masticar. ¿Qué soy?", "peine")
    )


    init {
        crearCasa()
        pintarCasaJugador()
        loopGame()

    }

    private fun crearCasa() {
        // Colocamos la puerta
        var dummyFila = 0
        var dummyColumna = 0

        dummyFila = Random.nextInt(1, filas)

        dummyColumna = if ((dummyFila == 1) || (dummyFila == filas)) {
            Random.nextInt(1, columnas) - 1
        } else {
            listOf(1, columnas)[Random.nextInt(listOf(1, columnas).size)] - 1

        }
        casa[dummyFila][dummyColumna] = puerta
        jugadorFila = dummyFila
        jugadorColumna = dummyColumna

        // Colocamos el caramelo, para ello buscamos una sala libre
        do {
            dummyFila = Random.nextInt(1, filas) - 1
            dummyColumna = Random.nextInt(1, columnas) - 1
            if (casa[dummyFila][dummyColumna] == sala) {
                casa[dummyFila][dummyColumna] = caramelo
            }

        } while (casa[dummyFila][dummyColumna] != caramelo)


        // De forma aleatoria colocamos dos fantasmas
        var numFantasmas = 0
        do {
            dummyFila = Random.nextInt(1, filas) - 1
            dummyColumna = Random.nextInt(1, columnas) - 1
            if (casa[dummyFila][dummyColumna] == sala) {
                casa[dummyFila][dummyColumna] = fantasma
                numFantasmas++
            }

        } while (numFantasmas < 2)

    }

    private fun loopGame() {

        var salida = false
        while (!salida) {

            moverJugador(pideMovimiento()!!)
            pintarCasaJugador()


            when (casa[jugadorFila][jugadorColumna]) {
                sala -> presentarEnigma()
                fantasma -> {

                    println("👻👻👻 DEBERÁS RESOLVER DOS ENGIMAS 👻👻👻")
                    presentarEnigma()
                    presentarEnigma()
                }

                caramelo -> {
                    println("¡¡¡ HAS ENCONTRADO LOS CARAMELOS !!!")
                    salida = true
                }

                puerta -> {
                    println(" ¡¡¡ OTRA VEZ AL PRINCPIO !!! ")
                }

                else -> println("Habitación no contemplada")

            }
        }

    }

    fun moverJugador(mov: String) {
        when (mov) {
            "N" -> if (jugadorFila - 1 >= 0) jugadorFila--
            "S" -> if (jugadorFila + 1 < filas) jugadorFila++
            "O" -> if (jugadorColumna - 1 >= 0) jugadorColumna--
            "E" -> if (jugadorColumna + 1 < columnas) jugadorColumna++
            else -> println("Movimiento no válido")
        }


    }

    fun pintarCasa() {
        casa.forEach {
            it.forEach() {
                print(it)
            }
            println()
        }
    }

    fun pintarCasaJugador() {
        println("Estas en [${jugadorFila + 1}, ${jugadorColumna + 1}]")
        casa.onEachIndexed { i, fila ->
            fila.onEachIndexed { j, sala ->
                if (sala == puerta) {
                    print(sala)
                } else {
                    if ((i == jugadorFila) && (j == jugadorColumna)) {
                        print("🧭")
                    } else {
                        print(this.sala)
                    }
                }

            }
            println()

        }

    }


    fun pideMovimiento(): String? {

        var valido = false
        var input: String? = null
        while (!valido) {
            print("¿Hacia dónde? (N)orte/(S)ur/(E)ste/(O)este >")
            input = readLine()

            if (input != null) {
                if (listOf("N", "n", "S", "s", "E", "e", "O", "o", "Q", "q").contains(input)) {
                    valido = true
                } else {
                    println("Entrada inválida. Debes indicar una dirección válida.")
                }
            }
        }

        return input!!.uppercase()
    }


    fun presentarEnigma() {

        val numPregunta = (0 until enigmas.size).random()
        val pregunta = enigmas[numPregunta].first
        val respuesta = enigmas[numPregunta].second

        var valido = false
        var input: String? = null
        while (!valido) {
            print("$pregunta >")
            input = readLine()

            if (input != null) {
                if (respuesta == input) {
                    valido = true
                } else {
                    println("La respuesta NO es correcta.")
                }
            }
        }

    }
}

