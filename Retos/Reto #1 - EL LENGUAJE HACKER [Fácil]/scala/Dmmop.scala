@main
def main(): Unit = {
  val mapa = Map[Char, String](
    'a' -> "4",
    'b' -> "I3",
    'c' -> "[",
    'd' -> ")",
    'e' -> "3",
    'f' -> "|=",
    'g' -> "&",
    'h' -> "#",
    'i' -> "1",
    'j' -> ",_|",
    'k' -> ">|",
    'l' -> "1",
    'm' -> "/\\/\\",
    'n' -> "^/",
    'o' -> "0",
    'p' -> "|*",
    'q' -> "(_,)",
    'r' -> "I2",
    's' -> "5",
    't' -> "7",
    'u' -> "(_)",
    'v' -> "\\/",
    'w' -> "\\/\\/",
    'x' -> "><",
    'y' -> "j",
    'z' -> "2"
  )
  print("Enter clear text: ")
  val clearText = scala.io.StdIn.readLine()
  val cypherText = clearText.toLowerCase()
    .toList
    .map(word => mapa.getOrElse(word, word))
    .mkString
  println(cypherText)
}