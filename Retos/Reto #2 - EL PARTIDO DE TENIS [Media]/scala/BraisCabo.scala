import scala.io.StdIn.readLine
val points = List("Love", 15, 30, 40, "Game")

def printScoreBoard(p1 : Int, p2: Int): (Boolean, String) = {
  (p1, p2) match{
    case (e1, e2) if (e1 == e2 && e1 >= 3) => (false, "Deuce")
    case (e1, e2) if (e1 > 3 && e1 > e2) =>
      if (e1 - 1 > e2)
        (true, "Ha ganado el P1")
      else
        (false, "Ventaja P1")
    case (e1, e2) if (e2 > 3) =>
      if (e2 - 1 > e1)
        (true, "Ha ganado el P2")
      else
        (false, "Ventaja P2")
    case (e1, e2) => (false, points(e1).toString + " - " + points(e2).toString)
  }
}

@main def reto2 = {
  var p1 = 0
  var p2 = 0
  var score = (false, "")
  while(!score._1){
    readLine().toLowerCase match {
      case "p1" => p1 += 1
      case "p2" => p2 += 1
      case _ =>{
        print("Ha habido un error en el input, inténtalo de nuevo\n")
        throw new RuntimeException
      }
    }
    score = printScoreBoard(p1, p2)
    print(score._2)
  }
}