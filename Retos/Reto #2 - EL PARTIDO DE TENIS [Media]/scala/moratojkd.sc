import scala.collection.mutable.ListBuffer
import scala.util.{Failure, Success, Try}


var puntos: ListBuffer[(Int, Int)] = ListBuffer[(Int, Int)]()
var partidoEnCurso: Boolean = true
var resultados: ListBuffer[String] = ListBuffer[String]()
val descripcionPuntos: List[String] = List("Love", "15", "30", "40")

def ganador(puntosP1: Int, puntosP2: Int): ListBuffer[String] = {
  if(puntosP1 - puntosP2 >= 2) {
    partidoEnCurso = false
    resultados += "Ha ganado el P1"
  }
  if(puntosP2 - puntosP1 >= 2) {
    partidoEnCurso = false
    resultados += "Ha ganado el P2"
  }
  else resultados
}

def ventaja(puntosP1: Int, puntosP2: Int): ListBuffer[String] = {
  if(puntosP1 > puntosP2 && (Math.abs(puntosP1 - puntosP2) < 2)) resultados += s"Ventaja P1"
  if(puntosP2 < puntosP2 && (Math.abs(puntosP2 - puntosP1) < 2)) resultados += s"Ventaja P2"
  else resultados
}

def tranformarAPuntosSistema(punto: (Int, Int)): List[String] = {
  val puntosP1 = punto._1
  val puntosP2 = punto._2
  if (partidoEnCurso) {
    if (puntosP1 >= 3 && puntosP2 >= 3) {
      ganador(puntosP1, puntosP2)
      if (puntosP1 == puntosP2) resultados += "Deuce"
      ventaja(puntosP1, puntosP2)
    } else resultados += s"${descripcionPuntos(puntosP1)} - ${descripcionPuntos(puntosP2)}"
  }
  resultados.toList
}

def asignarPunto(punto: String): ListBuffer[(Int, Int)] =
  punto match {
    case "P1" => puntos += ((1,0))
    case "P2" => puntos += ((0,1))
  }


def mostrarResultado(resultado: List[String]): List[String] = {
    val resultadoAMayuscula = resultado.map(_.toUpperCase)
    resultadoAMayuscula.foreach(asignarPunto(_))
    val result: List[(Int, Int)] = puntos.scanLeft((0, 0)) { case ((a, b), (c, d)) => (a + c, b + d) }.tail.toList
    result.foreach(tranformarAPuntosSistema(_))
    resultados.toList
}

def intentar(resultado: List[String]): Try[List[String]] = Try {
  mostrarResultado(resultado)
}

intentar(List("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")) match {
  case Success(value) => println(value)
  case Failure(exception) => println(s"algo ha ido mal: $exception")
}