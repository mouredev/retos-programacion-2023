import scala.annotation.unused

object Main {
  def main(args: Array[String]): Unit = {
    print("Selecciona el modo: Interactivo (1) o conjunto de tuplas (2)")
    val mode = scala.io.StdIn.readLine()
    if (mode.trim.equals("1")) {
      val player1 = readPlayerSelection("Player 1")
      val player2 = readPlayerSelection("Player 2")
      printWinner(player1, player2)
    } else {
      List(
        List(PlayerOption.Rock, PlayerOption.Rock),
        List(PlayerOption.Rock, PlayerOption.Paper),
        List(PlayerOption.Rock, PlayerOption.Scissor),
        List(PlayerOption.Rock, PlayerOption.Spock),
        List(PlayerOption.Rock, PlayerOption.Lizard)
      ).foreach(tupleWinner)
    }

  }

  private def readPlayerSelection(player: String): PlayerOption.Value = {
    print(s"Introduce el valor para $player (🗿 ROCK/ 📄 PAPER/ ✂️ SCISSOR/ 🦎 LIZARD/ 🖖 SPOCK): ")
    val playerInput: String = scala.io.StdIn.readLine()
    PlayerOption.values.filter(option => option.value.equals(playerInput.trim.toUpperCase)).firstKey
  }

  private def tupleWinner(round: List[PlayerOption.Value]): Unit = {
    printWinner(round.head, round.tail.head)
  }

  private def printWinner(player1: PlayerOption.Value, player2: PlayerOption.Value): Unit = {
    if (player1.isWinner(player2)) {
      println("Gana player 1")
    } else if (player2.isWinner(player1)) {
      println("Gana player 2")
    } else {
      println("Empate")
    }
  }
}

object PlayerOption extends Enumeration {

  @unused
  protected case class PlayerOptionVal(won: Function[PlayerOptionVal, Boolean], value: String) extends super.Val {
    def isWinner: Function[PlayerOptionVal, Boolean] = won
  }

  import scala.language.implicitConversions

  implicit def valueToPlayerOptionVal(x: Value): PlayerOptionVal = x.asInstanceOf[PlayerOptionVal]

  val Rock: PlayerOptionVal = PlayerOptionVal(option => option == Lizard || option == Scissor, "ROCK")
  val Paper: PlayerOptionVal = PlayerOptionVal(option => option == Rock || option == Spock, "PAPER")
  val Scissor: PlayerOptionVal = PlayerOptionVal(option => option == Paper || option == Lizard, "SCISSOR")
  val Lizard: PlayerOptionVal = PlayerOptionVal(option => option == Spock || option == Paper, "LIZARD")
  val Spock: PlayerOptionVal = PlayerOptionVal(option => option == Scissor || option == Rock, "SPOCK")

}
