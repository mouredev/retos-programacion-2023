import chintoz.House.{Gryffindor, House, Hufflepuff, Ravenclaw, Slytherin}

object chintoz {
  def main(args: Array[String]): Unit = {
    println(s"${Console.GREEN}Bienvenido al sombrero seleccionador. ")
    val questions = generateQuestions()

    val result = questions.map(question => solveQuestion(question)).reduce((a, b) => combineMaps(a, b))
    println(s"${Console.RED}¡¡El sombredo seleccionador dice: ${result.maxBy(_._2)._1}!!")
  }

  private def combineMaps(a: collection.mutable.Map[House, Int], b: collection.mutable.Map[House, Int]): collection.mutable.Map[House, Int] = {
    val result: collection.mutable.Map[House, Int] = collection.mutable.Map()
    House.values.foreach(value => result.put(value, a.getOrElse(value, 0) + b.getOrElse(value, 0)))
    result
  }

  private def solveQuestion(question: Question): collection.mutable.Map[House, Int] = {

    println(Console.BLUE + question.description)
    question.options.zip(1 until question.options.size + 1).foreach(option => println(Console.WHITE + option._2 + ". " + option._1.description))
    val selectedValue = readPlayerSelection(question.options.size)
    question.options(selectedValue - 1).points
  }

  private def readPlayerSelection(max: Int): Int = {
    print(s"${Console.GREEN}¿Que opción seleccionas [1..$max]? ")
    val playerInput: Integer = scala.io.StdIn.readLine().toInt
    if (playerInput < 1 || playerInput > max) {
      throw new IllegalArgumentException("Invalid value selected for a question")
    }
    playerInput
  }

  private def generateQuestions(): List[Question] = {
    List(
      Question("¿Cuál es tu clase favorita?",
        List(Option("Pociones", collection.mutable.Map(Slytherin -> 10, Gryffindor -> -3)),
          Option("Tranformaciones", collection.mutable.Map(Ravenclaw -> 10, Hufflepuff -> 7)),
          Option("Adivinación", collection.mutable.Map(Gryffindor -> 3, Hufflepuff -> 7, Ravenclaw -> 1, Slytherin -> -2)),
          Option("Defensa contra las artes oscuras", collection.mutable.Map(Gryffindor -> 10, Ravenclaw -> 5, Hufflepuff -> 5, Slytherin -> -3)),
          Option("Herbologia", collection.mutable.Map(Gryffindor -> 1, Ravenclaw -> 3, Hufflepuff -> 3, Slytherin -> 7)),
          Option("Astronomía", collection.mutable.Map(Gryffindor -> 3, Ravenclaw -> 5, Hufflepuff -> 5, Slytherin -> 2)),
          Option("Encantamientos", collection.mutable.Map(Gryffindor -> 6, Ravenclaw -> 6, Hufflepuff -> 2, Slytherin -> 3)),
          Option("Cuidado de criaturas mágicas", collection.mutable.Map(Gryffindor -> 7, Ravenclaw -> 3, Hufflepuff -> 7, Slytherin -> 3)),
          Option("Clase de Vuelo", collection.mutable.Map(Gryffindor -> 7, Ravenclaw -> 3, Hufflepuff -> 3, Slytherin -> 7)))
      ),
      Question("¿Con qué expresión te sientes más identificado?",
        List(Option("Moriría por ti", collection.mutable.Map(Gryffindor -> 10, Hufflepuff -> 3)),
          Option("Mataría por ti", collection.mutable.Map(Slytherin -> 10, Gryffindor -> 3)),
          Option("Moriría contigo", collection.mutable.Map(Hufflepuff -> 10, Ravenclaw -> 3)),
          Option("Buscaría una solución para que no tengamos que morir", collection.mutable.Map(Ravenclaw -> 10, Slytherin -> 3)))
      ),
      Question("Tienes un amigo muggle que te ha contado un problema que tiene, pero te ha pedido que se quede en secreto. ¿Qué harias?",
        List(Option("Imposible, no tendría amigos muggles", collection.mutable.Map(Slytherin -> 10)),
          Option("Mantendría el secreto e intentaría ayudarle intentando evitar que se hiciera público", collection.mutable.Map(Hufflepuff -> 10)),
          Option("Le diria que le echase valor a la cosa y que lo contara", collection.mutable.Map(Gryffindor -> 10)),
          Option("Trabajaríamos juntos intentando buscar una solución a su problema", collection.mutable.Map(Ravenclaw -> 10)))
      ),
      Question("¿Cuál de estos colores prefieres?",
        List(Option("Naranja", collection.mutable.Map(Hufflepuff -> 5, Gryffindor -> 5)),
          Option("Violeta", collection.mutable.Map(Gryffindor -> 5, Ravenclaw -> 5)),
          Option("Negro", collection.mutable.Map(Slytherin -> 5, Gryffindor -> 5)),
          Option("Verde", collection.mutable.Map(Slytherin -> 5, Hufflepuff -> 3, Ravenclaw -> 3)))
      ),
      Question("¿Cuál es tu hechizo favorito?",
        List(Option("Protego", collection.mutable.Map(Ravenclaw -> 5, Hufflepuff -> 5)),
          Option("Avada Kedavra", collection.mutable.Map(Slytherin -> 15)),
          Option("Expelliarmus", collection.mutable.Map(Hufflepuff -> 3, Ravenclaw -> 3, Gryffindor -> 3)),
          Option("Expecto Patronum", collection.mutable.Map(Gryffindor -> 10, Ravenclaw -> 5, Hufflepuff -> 5)))
      )
    )
  }

  private case class Question(description: String, options: List[Option])

  private case class Option(description: String, points: collection.mutable.Map[House, Int])

  object House extends Enumeration {
    type House = Value
    val Gryffindor, Hufflepuff, Ravenclaw, Slytherin = Value
  }
}
