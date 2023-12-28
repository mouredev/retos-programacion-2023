/*
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
 */


fun main() {
    val letterValues: Map<String, Int> = mapOf(
        "a" to 1,
        "b" to 2,
        "c" to 3,
        "d" to 4,
        "e" to 5,
        "f" to 6,
        "g" to 7,
        "h" to 8,
        "i" to 9,
        "j" to 10,
        "k" to 11,
        "l" to 12,
        "m" to 13,
        "n" to 14,
        "ñ" to 15,
        "o" to 16,
        "p" to 17,
        "q" to 18,
        "r" to 19,
        "s" to 20,
        "t" to 21,
        "u" to 22,
        "v" to 23,
        "w" to 24,
        "x" to 25,
        "y" to 26,
        "z" to 27
    )

    var points = 0

    while (points < 100) {
        print("Tu palabra: ")
        val word = readln()

        for (i in word) {
            val point = letterValues[i.toString()] ?: 0
            points += point
            println("$i - $point")
        }

        println("TOTAL: $points puntos")

        if (points < 100) {
            println("Prueba otra vez")
            points = 0
        } else {
            println("GANASTE!!!")
        }
    }
}
