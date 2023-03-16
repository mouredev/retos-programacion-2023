object chintoz {
  def main(args: Array[String]): Unit = {
    val input = readStringToCheck()
    val map = mapString(input)
    print(s"${Console.GREEN}La cadena introducida: \"$input\" es Heterograma? ${isHeterogram(map)}, es Isograma? ${isIsogram(map)}, es Pangrama? ${isPangram(map)}  ")
  }

  private def isIsogram(input: Map[Char, Int] ) : Boolean = input.nonEmpty && input.values.max == input.values.min
  private def isHeterogram(input: Map[Char, Int] ) : Boolean = isIsogram(input) && input.values.max == 1
  private def isPangram(input: Map[Char, Int] ) : Boolean = input.nonEmpty && ('a' to 'z').forall(c => input.contains(c))

  private def readStringToCheck(): String = {
    print(s"${Console.BLUE}¿Qué cadena quieres chequear? ")
    scala.io.StdIn.readLine()
  }
  private def mapString(input: String): Map[Char, Int] = {
    input.filter(_.isLetter).toLowerCase().groupBy(_.charValue()).map(tuple => (tuple._1,tuple._2.length))
  }

}
