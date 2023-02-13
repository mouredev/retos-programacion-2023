val optionsPlay: Array[String] = Array("Rock", "Paper", "Scissors", "Lizard", "Spock")

val winArray: Array[Array[Int]] = Array(
  Array(0, -1, 1, 1, -1),
  Array(1, 0, -1, -1, 1),
  Array(-1, 1, 0, 1, -1),
  Array(-1, 1, -1, 0, 1),
  Array(1, -1, 1, -1, 0)
)

def eval(player1: String, player2: String): Int = {
  val player1Index = optionsPlay.indexOf(player1)
  val player2Index = optionsPlay.indexOf(player2)
  winArray(player1Index)(player2Index)
}

@main
def main(): Unit =
  Array(("Rock", "Scissors"), ("Rock", "Spock"), ("Rock", "Rock"), ("Rock", "Paper"), ("Rock", "Lizard"), ("Paper", "Scissors"), ("Paper", "Rock"), ("Paper", "Paper"), ("Paper", "Lizard"), ("Scissors", "Scissors"), ("Scissors", "Spock"), ("Scissors", "Rock"), ("Scissors", "Paper"), ("Scissors", "Lizard"), ("Lizard", "Scissors"), ("Lizard", "Spock"), ("Lizard", "Rock"), ("Lizard", "Paper"), ("Lizard", "Lizard"), ("Spock", "Scissors"), ("Spock", "Spock"), ("Spock", "Rock"), ("Spock", "Paper"), ("Spock", "Lizard")).map(eval.tupled)
    .sum match
      case 0 => println("Draw")
      case x if x > 0 => println("Player 1 wins")
      case _ => println("Player 2 wins")
