fun main() {
        print(
                        "¡Felicidades! Según tus respuestas, perteneces a la casa de ${HogwartsHatSelector()}"
        )
}

fun HogwartsHatSelector(): String {
        println("Bienvenido al Test de Clasificación de Casas de Hogwarts!")
        println("Responde las siguientes preguntas para saber a qué casa pertenecerías:")
        val preguntas =
                        arrayOf(
                                        "1. ¿Qué cualidad valoras más en ti mismo?",
                                        "2. ¿Qué criatura mágica te gustaría tener como mascota?",
                                        "3. ¿Cuál es tu asignatura favorita en Hogwarts?",
                                        "4. ¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
                                        "5. ¿Cuál es tu hechizo favorito?",
                                        "6. ¿Qué objeto mágico te gustaría poseer?",
                                        "7. ¿Cuál es tu personaje favorito de Harry Potter?",
                                        "8. ¿Qué harías si te enfrentas a un troll?",
                                        "9. ¿Qué tipo de clima prefieres?",
                                        "10. ¿Cuál es tu forma preferida de transporte mágico?",
                                        "11. ¿Qué color te atrae más?",
                                        "12. ¿Qué criatura mágica te da más miedo?",
                                        "13. ¿Cuál es tu golosina mágica favorita?",
                                        "14. ¿Cuál es tu asignatura menos favorita en Hogwarts?",
                                        "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"
                        )
        val opciones =
                        arrayOf(
                                        arrayOf(
                                                        "a. Coraje",
                                                        "b. Inteligencia",
                                                        "c. Lealtad",
                                                        "d. Astucia"
                                        ),
                                        arrayOf("a. Búho", "b. Gato", "c. Rata", "d. Lechuza"),
                                        arrayOf(
                                                        "a. Pociones",
                                                        "b. Transformaciones",
                                                        "c. Herbología",
                                                        "d. Defensa contra las Artes Oscuras"
                                        ),
                                        arrayOf(
                                                        "a. La Sala Común de mi casa",
                                                        "b. El Gran Comedor",
                                                        "c. La Biblioteca",
                                                        "d. Los terrenos del castillo"
                                        ),
                                        arrayOf(
                                                        "a. Expecto Patronum",
                                                        "b. Wingardium Leviosa",
                                                        "c. Expelliarmus",
                                                        "d. Lumos"
                                        ),
                                        arrayOf(
                                                        "a. La Capa de Invisibilidad",
                                                        "b. La Varita de Saúco",
                                                        "c. El Giratiempo",
                                                        "d. La Piedra Filosofal"
                                        ),
                                        arrayOf(
                                                        "a. Harry Potter",
                                                        "b. Hermione Granger",
                                                        "c. Ron Weasley",
                                                        "d. Neville Longbottom"
                                        ),
                                        arrayOf(
                                                        "a. Huir",
                                                        "b. Atacar",
                                                        "c. Pedir ayuda",
                                                        "d. Intentar razonar con él"
                                        ),
                                        arrayOf("a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"),
                                        arrayOf(
                                                        "a. Escoba voladora",
                                                        "b. El Autobús Noctámbulo",
                                                        "c. El Tren Hogwarts Express",
                                                        "d. Aparición"
                                        ),
                                        arrayOf("a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"),
                                        arrayOf(
                                                        "a. Dementor",
                                                        "b. El Basilisco",
                                                        "c. El Hombre Lobo",
                                                        "d. Las Arpías"
                                        ),
                                        arrayOf(
                                                        "a. Grageas de Todos los Sabores",
                                                        "b. Chocolate de la Caja de Bertie Bott",
                                                        "c. Pastel de Calabaza",
                                                        "d. Caramelos de Menta"
                                        ),
                                        arrayOf(
                                                        "a. Historia de la Magia",
                                                        "b. Adivinación",
                                                        "c. Estudio de los Muggles",
                                                        "d. Runas Antiguas"
                                        ),
                                        arrayOf(
                                                        "a. Jugar al Quidditch",
                                                        "b. Explorar el castillo",
                                                        "c. Leer en la Biblioteca",
                                                        "d. Pasar tiempo con amigos"
                                        )
                        )

        // Elegimos cuatro preguntas al azar
        val random_questions = mutableListOf<Int>()
        while (random_questions.size < 4) {
                val random = (0 until preguntas.size).random()
                if (!random_questions.contains(random)) {
                        random_questions.add(random)
                }
        }

        val respuestas = mutableListOf<String>()
        for (i in random_questions) {
                println(preguntas[i])
                for (opcion in opciones[i]) {
                        println(opcion)
                }
                print("Elige una opción (a, b, c o d): ")
                val respuesta = readLine() ?: ""
                respuestas.add(respuesta)
        }

        val puntuaciones =
                        mutableMapOf(
                                        "Gryffindor" to 0,
                                        "Ravenclaw" to 0,
                                        "Hufflepuff" to 0,
                                        "Slytherin" to 0
                        )
        for (respuesta in respuestas) {
                when (respuesta) {
                        "a" -> puntuaciones["Gryffindor"] = puntuaciones["Gryffindor"]!! + 1
                        "b" -> puntuaciones["Ravenclaw"] = puntuaciones["Ravenclaw"]!! + 1
                        "c" -> puntuaciones["Hufflepuff"] = puntuaciones["Hufflepuff"]!! + 1
                        "d" -> puntuaciones["Slytherin"] = puntuaciones["Slytherin"]!! + 1
                }
        }

        val casa = puntuaciones.maxByOrNull { it.value }?.key ?: ""
        return casa
}
