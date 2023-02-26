package com.malopezrom.reto7
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */


/**
 * Interface que representa una respuesta y sus puntos
 */
data class Question(private val question: String, private val answers: List<Answer>) {
    fun ask(): Answer {
        println(question)
        println("")
        answers.forEachIndexed { index, answer -> println("${index + 1}. ${answer.answer}") }

        var answer: Int
        do {
            print("\nElige una opción: ")
            answer = readLine()?.toIntOrNull() ?: 0
        } while (answer !in 1..4)

        return answers[answer - 1]
    }
}

/**
 * Interface que representa una respuesta y sus puntos
 */
data class Answer(val answer: String, val points: List<Point>) {
    fun getPoints(team: Team): Int {
        return points.firstOrNull { it.name == team }?.points ?: 0
    }
}

/**
 * Interface que representa los puntos de cada equipo
 */
data class Point(val name: Team, val points: Int)

/**
 * Enumerado que representa los equipos
 */
enum class Team(val team: String){
    Celtic("Celtic de Pulianas"),
    Farsa("Farsa el equipo de los culerdos"),
    GranadaCF("Vamos mi grana"),
    RMadrid("Central Lechera")
}

/**
 * Array de preguntas y respuestas y sus puntos correspondientes a cada equipo
 */
val quizz = listOf(
        Question(
        "Se acerca la fecha del próximo partido de tu equipo, ¿cómo te sientes?",
        listOf(
             Answer("Nervioso/a, todos los partidos de mi equipo los siento con pasión.", listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2))),
             Answer("No es relevante, cuando llegue la hora ya me sentaré a verlo tranquilamente.",listOf(Point(Team.Celtic, 0), Point(Team.Farsa, 7), Point(Team.GranadaCF,2), Point(Team.RMadrid, 7))),
             Answer("Los vecinos hablan sobre el partido los días previos, se nota el ambiente en la calle.",listOf(Point(Team.Celtic, 4), Point(Team.Farsa, 10), Point(Team.GranadaCF,1), Point(Team.RMadrid, 9))),
             Answer("No como ni duermo los días previos de los nervios. Da igual que sean dieciseisavos de Copa o la última jornada de Liga, lo vivo.",listOf(Point(Team.Celtic, 8), Point(Team.Farsa, 1), Point(Team.GranadaCF,10), Point(Team.RMadrid, 0)))
        )),
        Question(
       "Estás en un bar y te das cuenta de que nadie es del mismo equipo que tú, ¿qué piensas?",
        listOf(
               Answer("Joder, mira que es raro.", listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 3), Point(Team.RMadrid, 2))),
               Answer("Ya está esto lleno de borregos, míralos, todos viendo el Chirincirco.",listOf(Point(Team.Celtic, 1), Point(Team.Farsa, 7), Point(Team.GranadaCF,4), Point(Team.RMadrid, 9))),
               Answer("Normal, si somos 4 gatos. Eh, pero con orgullo, coño.",listOf(Point(Team.Celtic, 2), Point(Team.Farsa, 10), Point(Team.GranadaCF,1), Point(Team.RMadrid, 2))),
               Answer("Ups, igual tenía que haber ido al de dos calles más abajo...",listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 1), Point(Team.GranadaCF,4), Point(Team.RMadrid, 1)))
                )),
        Question(
       "Penalti a favor del Madrid/Barcelona. En la repetición se ve que no era. ¿Cómo reaccionas?",
        listOf(
                Answer("Ya están robando estos perros.", listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2))),
                Answer("Esto es una puta vergüenza! Soy el entrenador y los saco del campo, que se rían de su madre.",listOf(Point(Team.Celtic, 3), Point(Team.Farsa, 10), Point(Team.GranadaCF,3), Point(Team.RMadrid, 9))),
                Answer("Ya la tenemos liada, ahora a aguantar a la prensa toda la semana...",listOf(Point(Team.Celtic, 4), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2))),
                Answer("Ya estamos con la prensa mamadora del movimiento",listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2)))
                )),
        Question(
       "Caso contrario: última jornada de liga y una victoria de tu equipo hace que supere el objetivo marcado al principio del año.",
        listOf(
                Answer("Coño, coño, coño, coño, coño, coño. Como les dé por ganar me desnudo en la fuente del pueblo.", listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2))),
                Answer("Yaya, enséñame unos rezos de esos, que es para una cosa del finde.",listOf(Point(Team.Celtic, 1), Point(Team.Farsa, 9), Point(Team.GranadaCF,2), Point(Team.RMadrid, 6))),
                Answer("Pase lo que pase ha sido un temporadón, ¡qué orgullo de equipo!",listOf(Point(Team.Celtic, 6), Point(Team.Farsa, 5), Point(Team.GranadaCF,4), Point(Team.RMadrid, 4))),
                Answer("Con lo bien que vivía yo cuando éramos mediocres, qué ganas de matarnos con los nervios.",listOf(Point(Team.Celtic, 10), Point(Team.Farsa, 1), Point(Team.GranadaCF,9), Point(Team.RMadrid, 4)))
                )),
        Question(
        "Final de la temporada, tu equipo desciende a Segunda División. Vaya veranito te vas a pegar...",
        listOf(
                Answer("JAJAJAJAJAJAJAJAJA EN SEGUNDA DICE, ¡QUE SOY DEL MADRID/BARÇA, TOLAI!", listOf(Point(Team.Celtic, 0), Point(Team.Farsa, 10), Point(Team.GranadaCF, 0), Point(Team.RMadrid, 10))),
                Answer("Lloro, me enfado, durante las primeras semanas va a ser una auténtica pesadilla. No puede pasarnos a nosotros...",listOf(Point(Team.Celtic, 5), Point(Team.Farsa, 7), Point(Team.GranadaCF,3), Point(Team.RMadrid, 4))),
                Answer("No pudo ser, nos vino grande la categoría. Volveremos con más fuerza, ¡seguro!",listOf(Point(Team.Celtic, 7), Point(Team.Farsa, 2), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2))),
                Answer("Otra vez al hoyo. El año que viene mi abono se lo pueden meter por el...",listOf(Point(Team.Celtic, 4), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 0)))
                )),
        )



/**
 * Función que calcula el equipo al que perteneces
 */
fun yourTeamsIs(points:MutableMap<Team,Int>){
    val teamWithMaxPoints = points.maxBy { it.value }.key
    println("Tu equipo es: ${teamWithMaxPoints.team}")



}

/**
 * Función principal que llama a la función que muestra las preguntas
 */
fun quizGame(){
    val points = mutableMapOf<Team, Int>()
    points[Team.Celtic] = 0
    points[Team.Farsa] = 0
    points[Team.GranadaCF] = 0
    points[Team.RMadrid] = 0


    println("Bienvenido al test de fútbol. Responde a las siguientes preguntas y averigua qué equipo eres:\n")
    quizz.forEach { question ->
        val answer = question.ask()
        answer.points.forEach { point ->
            //points[point.name] = (points[point.name] ?: 0) + point.points
            points[point.name] = (answer.getPoints(point.name) + (points[point.name] ?: 0))
        }
    }

    yourTeamsIs(points)
}
/**
 * Llamada a la función principal
 */
quizGame()

