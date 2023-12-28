fun main() {
    val preguntas = arrayOf(
        "¿Cuál es tu asignatura favorita?",
        "¿Qué cualidad valoras más en una persona?",
        "¿Qué lugar prefieres para estudiar?",
        "¿Cuál es tu mayor miedo?",
        "¿Qué cualidad te define mejor?"
    )

    val respuestas = arrayOf(
        arrayOf("Astronomía", "Historia de la Magia", "Herbología", "Encantamientos"),
        arrayOf("Valentía", "Astucia", "Lealtad", "Inteligencia"),
        arrayOf("La biblioteca", "La sala común", "El invernadero", "El lago negro"),
        arrayOf("Las arañas", "El fracaso", "El rechazo", "La oscuridad"),
        arrayOf("Valentía", "Astucia", "Lealtad", "Inteligencia")
    )

    val casas = arrayOf("Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw")
    val puntajes = IntArray(casas.size)

    for (i in preguntas.indices) {
        println(preguntas[i])
        for (j in respuestas[i].indices) {
            println("${j+1}. ${respuestas[i][j]}")
        }
        print("Respuesta: ")
        val respuesta = readLine()?.toIntOrNull() ?: 0
        for (j in casas.indices) {
            puntajes[j] += if (respuesta == j+1) 2 else 0
            puntajes[j] += if (respuesta == (j+1) % 4 + 1) 1 else 0
            puntajes[j] -= if (respuesta == (j+2) % 4 + 1) 1 else 0
            puntajes[j] -= if (respuesta == (j+3) % 4 + 1) 2 else 0
        }
    }

    val casaGanadora = casas[puntajes.indices.maxByOrNull { puntajes[it] } ?: 0]
    println("¡Felicidades! Has sido seleccionado para la casa de $casaGanadora.")
}
