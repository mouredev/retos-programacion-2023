import scala.io.StdIn.readLine
@main def reto1 = {
  val mapa = Map[Char, String]('a' -> "4",
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
    'z' -> "2")
  print(readLine().toLowerCase.toList.map(letra => mapa.get(letra) match {
    case None => letra
    case Some(value) => value
  }).foldLeft("": String) {
    case (acc, e) => acc + e
  })
}