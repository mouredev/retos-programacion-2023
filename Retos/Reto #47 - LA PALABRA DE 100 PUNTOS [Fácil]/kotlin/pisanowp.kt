fun main() {

    /*
    * Reto #47 04/12/2023  LA PALABRA DE 100 PUNTOS
    *
    * La última semana de 2021 comenzamos la actividad de retos de programación,
    * con la intención de resolver un ejercicio cada semana para mejorar
    * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
    *
    * Crea un programa que calcule los puntos de una palabra.
    * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
    *   español de 27 letras, la A vale 1 y la Z 27.
    * - El programa muestra el valor de los puntos de cada palabra introducida.
    * - El programa finaliza si logras introducir una palabra de 100 puntos.
    * - Puedes usar la terminal para interactuar con el usuario y solicitarle
    *   cada palabra.
    *
    */

    // Inicializamos el abeceraio, añadiendo la Ñ
    val abecedario : MutableList<Char> = mutableListOf()
    ('A'..'N').forEachIndexed(){ indice, letra ->
        abecedario.add(letra)
    }
    abecedario.add('Ñ')
    ('O'..'Z').forEachIndexed(){ indice, letra ->
        abecedario.add(letra)
    }

    var seguirJugando = true
    while (seguirJugando) {
        print("Introduce palabra (EXIT para terminar)> ")
        val palabra = readLine()
        var puntuacion = 0
        if (palabra != null) {
            val pal = palabra.uppercase()
            pal.forEach {
                puntuacion += abecedario.lastIndexOf(it) + 1
            }
        }

        when {
            (puntuacion < 20) -> {
                println("Tu palabra tiene un valor de $puntuacion puntos, aún muy lejos de los 100 esperados :(")
            }
            (puntuacion < 50) -> {
                println("Tu palabra tiene un valor de $puntuacion puntos,más cerca de los 100 :|")

            }
            (puntuacion < 70) -> {
                println("Tu palabra tiene un valor de $puntuacion puntos,has pasado la media pero aún queda para los 100 :)")

            }
            (puntuacion < 99) -> {
                println("Tu palabra tiene un valor de $puntuacion puntos, cada vez estas más cerca de conseguirlo :)")

            } else -> {
            println("¡¡¡ ENHORABUENA !!! Tu palabra tiene un valor de $puntuacion puntos :D ")
            seguirJugando = false
        }
        }
        if (palabra?.uppercase() == "EXIT"){
            seguirJugando = false
        }

    }

}
