import java.util
import scala.io.StdIn.readLine


def pregunta(pre: String, lista: java.util.ArrayList[Char], ini: Int, fin : Int): Unit = {
  println(pre)
  if (readLine() == "s") {
    for (n <- ini to fin){
      lista.add((n).toChar)
    }
  }
}

def generatePasswd(): (Int, java.util.ArrayList[Char]) = {
  var lenght = 0
  while (lenght < 8 || lenght > 16) {
    println("Indica la longitud, mínimo 8 máximo 16")
    lenght = readLine().toInt
  }
  var caracteres = new util.ArrayList[Char]()
  for (n <- 97 to 122) {
    caracteres.add((n).toChar)
  }
  pregunta("Quieres que tenga mayusculas? (s/other)", caracteres, 65, 90)

  pregunta("Quieres que tenga numeros? (s/other)", caracteres, 48, 57)

  val aux = List[Char](
    '!'
    , '@'
    , '#'
    , '$'
    , '^'
    , '&'
    , '('
    , ')'
    , '_'
    , '='
    , '+'
    , '-'
    , '*'
    , '/'
    , '%'
    , '<'
    , '>'
    , '?'
    , '['
    , ']'
    , '{'
    , '}'
  )

  println("Quieres que tenga símbolos? (s/other)")
  if (readLine() == "s") {
    for (n <- aux) {
      caracteres.add(n)
    }
  }
  return (lenght, caracteres)
}

@main def reto2 = {
  val resultado = generatePasswd()
  val rand: scala.util.Random = scala.util.Random
  val lenght = resultado._2.size()
  for (i <- 1 to resultado._1){
    print(resultado._2.get(rand.nextInt().abs % lenght))
  }
  println()
}