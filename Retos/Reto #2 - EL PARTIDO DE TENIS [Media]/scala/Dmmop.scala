val points = List("Love", 15, 30, 40, "Game")

def parseSome(score: Int): String =
  points.lift(score) match
    case Some(s: String) => s
    case Some(s: Int) => s.toString
    case _ => ""

def printScoreBoard(scoreBoard: (Int, Int)): Unit =
  scoreBoard match
    case (p1, p2) if Iterator(p1, p2).max < 3 => println(s"${parseSome(p1)} - ${parseSome(p2)}")
    case (p1, p2) if p1 == p2 => println("Deuce")
    case (p1, p2) if (p1 - p2).abs >= 2 => println(s"Player ${if (p1 > p2) 1 else 2} wins")
    case (p1, p2) if p1 != p2 => println(s"Advantage P${if (p1 > p2) 1 else 2}")

@main
def main(): Unit = {
  val input = List("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P2")
  input.scanLeft((0, 0))((score, point) =>
    point match
      case "P1" => (score._1 + 1, score._2)
      case "P2" => (score._1, score._2 + 1)
  ).foreach(printScoreBoard)
}