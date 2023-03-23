package EjercicioKotlin.Mouredev

/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

fun main() {
    val pregunta = Question().getQuestions()
    val repuestas = arrayOf(0, 0, 0, 0)

    println("EL SOMBRERO SELECCIONADOR")

    var contador = 0
    while (contador < pregunta.size) {

        printQuestion(pregunta.get(contador))
        print("Selecciones una respuesta:")
        val select = readLine()!!.toInt()

        when (select) {
            1 ->{
                repuestas[0]++
                contador++
            }

            2 ->{
                repuestas[1]++
                contador++
            }

            3 ->{
                repuestas[2]++
                contador++
            }

            4 ->{
                repuestas[3]++
                contador++
            }

            else->{
                print("\nlas respuestas son del 1 al 4")
                print("\ndigite un numero del 1 al 4\n")
            }
        }
    }

    sortingHat(repuestas)
}

fun printQuestion(pregunta: Question){

    println(pregunta.enuciado)
    println(pregunta.opcion1)
    println(pregunta.opcion2)
    println(pregunta.opcion3)
    println(pregunta.opcion4)
}

fun sortingHat(answer :Array<Int>){
    var positionmayor = 0
    var mayor = 0

    for (item in 0..answer.size - 1){
        if (answer[item] > mayor){
            mayor = answer[item]
            positionmayor = item
        }
    }

    println("\n-----------------------------")
    when(positionmayor){
        0->{
            println("Tu casa es la Gryffindor")
        }
        1->{
            println("Tu casa es la Slytherin ")
        }
        2->{
            println("Tu casa es la Hufflepuff ")
        }
        3->{
            println("Tu casa es la Ravenclaw")
        }
    }
    println("-----------------------------")
}

class Question(
    var enuciado: String = "",
    var opcion1: String = "",
    var opcion2: String = "",
    var opcion3: String = "",
    var opcion4: String = ""
) {
    fun getQuestions(): Array<Question> {
        return arrayOf(
            Question(
                "\n¿Qué color le gusta mas?",
                "1.Rojo",
                "2.Verde",
                "3.Amarillo",
                "4.Azul"
            ),
            Question(
                "\n¿Qué animal le gusta mas",
                "1.Leon",
                "2.Serpiente",
                "3.Tejón",
                "4.Águila"
            ),
            Question(
                "\n¿Qué mago le gusta mas?",
                "1.Hermione Granger",
                "2.Draco Malfoy",
                "3.Nymphadora Tonks",
                "4.Luna Lovegood"
            ),
            Question(
                "\n¿Qué especialidad lo indentifica mas?",
                "1.Fuerza",
                "2.Determinacion",
                "3.Lealtad",
                "4.Erudicion"
            ),
            Question(
                "\n¿A que le das mas valor?",
                "1.lealtad",
                "2.ambicion",
                "3.honor",
                "4.valentia"
            )
        )
    }
}

