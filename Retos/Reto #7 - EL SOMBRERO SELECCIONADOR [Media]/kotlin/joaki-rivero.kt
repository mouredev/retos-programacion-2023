fun main() {
    startCeremony()
}

enum class House {
    Gryffindor, Ravenclaw, Hufflepuff, Slytherin
}

val result = mutableMapOf(House.Gryffindor to 0, House.Ravenclaw to 0, House.Hufflepuff to 0, House.Slytherin to 0)

fun startCeremony() {
    println("----- CEREMONIA DE SELECCIÓN -----\n")
    println(
        "¡Bienvenido a Hogwarts! Conteste a las siguientes preguntas\n" +
                "y el Sombrero Seleccionador le colocará en una de las cuatro grandes casas.\n" +
                "A saber: Gryffindor, Ravenclaw, Hufflepuff y Slytherin\n"
    )

    do {
        val q1Answered = firstQuestion()
    } while (!q1Answered)

    do {
        val q2Answered = secondQuestion()
    } while (!q2Answered)

    do {
        val q3Answered = thirdQuestion()
    } while (!q3Answered)

    do {
        val q4Answered = fourthQuestion()
    } while (!q4Answered)

    do {
        val q5Answered = fifthQuestion()
    } while (!q5Answered)

    val winner = checkResults(result)
    println("\nUhmmm... Interesante... Ya veo...")
    println("Mejor que estés en... ¡${winner.name.uppercase()}!")
}

fun checkResults(result: MutableMap<House, Int>): House {
    val winner = result.maxBy { n -> n.value }
    return winner.key
}

fun firstQuestion(): Boolean {
    println(
        "\nSi dos amigos están peleando por una tarta ¿Cómo actuarías?\n" +
                "1. Divido la tarta.\n" +
                "2. Hago otra tarta.\n" +
                "3. Trato de separarlos.\n" +
                "4. Avada Kedavra a cada uno. La tarta pa'mí.\n"
    )
    print("Respuesta: ")

    when (readln()) {
        "1" -> {
            result[House.Ravenclaw] = result[House.Ravenclaw]!! + 1
            return true
        }

        "2" -> {
            result[House.Hufflepuff] = result[House.Hufflepuff]!! + 1
            return true
        }

        "3" -> {
            result[House.Gryffindor] = result[House.Gryffindor]!! + 1
            return true
        }

        "4" -> {
            result[House.Slytherin] = result[House.Slytherin]!! + 1
            return true
        }

        else -> {
            println("\nOpción no válida")
            return false
        }
    }
}

fun secondQuestion(): Boolean {
    println(
        "\n¿Cuál es tu forma de transporte favorita?\n" +
                "1. Polvos Flu\n" +
                "2. Hipogrifo\n" +
                "3. Traslador\n" +
                "4. Escoba voladora\n"
    )
    print("Respuesta: ")

    when (readln()) {
        "1" -> {
            result[House.Slytherin] = result[House.Slytherin]!! + 1
            return true
        }

        "2" -> {
            result[House.Hufflepuff] = result[House.Hufflepuff]!! + 1
            return true
        }

        "3" -> {
            result[House.Ravenclaw] = result[House.Ravenclaw]!! + 1
            return true
        }

        "4" -> {
            result[House.Gryffindor] = result[House.Gryffindor]!! + 1
            return true
        }

        else -> {
            println("\nOpción no válida")
            return false
        }
    }
}

fun thirdQuestion(): Boolean {
    println(
        "\n¿Qué bebida tomarías un viernes al mediodía?\n" +
                "1. Cerveza de mantequilla\n" +
                "2. Agua\n" +
                "3. Zumo de calabaza\n" +
                "4. Estrella Galicia bien fresquita\n"
    )
    print("Respuesta: ")

    when (readln()) {
        "1" -> {
            result[House.Gryffindor] = result[House.Gryffindor]!! + 1
            return true
        }

        "2" -> {
            result[House.Slytherin] = result[House.Slytherin]!! + 1
            return true
        }

        "3" -> {
            result[House.Hufflepuff] = result[House.Hufflepuff]!! + 1
            return true
        }

        "4" -> {
            result[House.Ravenclaw] = result[House.Ravenclaw]!! + 1
            return true
        }

        else -> {
            println("\nOpción no válida")
            return false
        }
    }
}

fun fourthQuestion(): Boolean {
    println(
        "\n¿Cómo te gustaría ser conocido/a en la historia?\n" +
                "1. El bueno/La buena\n" +
                "2. El/La gran\n" +
                "3. El/La audaz\n" +
                "4. El sabio/La sabia\n"
    )
    print("Respuesta: ")

    when (readln()) {
        "1" -> {
            result[House.Hufflepuff] = result[House.Hufflepuff]!! + 1
            return true
        }

        "2" -> {
            result[House.Gryffindor] = result[House.Gryffindor]!! + 1
            return true
        }

        "3" -> {
            result[House.Slytherin] = result[House.Slytherin]!! + 1
            return true
        }

        "4" -> {
            result[House.Ravenclaw] = result[House.Ravenclaw]!! + 1
            return true
        }

        else -> {
            println("\nOpción no válida")
            return false
        }
    }
}

fun fifthQuestion(): Boolean {
    println(
        "\n¿Despliegas a producción los viernes?\n" +
                "1. Siempre\n" +
                "2. Solo cuando es necesario\n" +
                "3. Nunca\n" +
                "4. A veces\n"
    )
    print("Respuesta: ")

    when (readln()) {
        "1" -> {
            result[House.Gryffindor] = result[House.Gryffindor]!! + 1
            return true
        }

        "2" -> {
            result[House.Ravenclaw] = result[House.Ravenclaw]!! + 1
            return true
        }

        "3" -> {
            result[House.Slytherin] = result[House.Slytherin]!! + 1
            return true
        }

        "4" -> {
            result[House.Hufflepuff] = result[House.Hufflepuff]!! + 1
            return true
        }

        else -> {
            println("\nOpción no válida")
            return false
        }
    }
}