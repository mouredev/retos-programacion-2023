/*
 * Crea un programa que calcule quien gana más partidas al juego piedra, papel, tijera, lagarto,
 *  spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

fun main() {

  val results2 =
    arrayOf(
      Round(Option.ROCK, Option.SCISSORS),
      Round(Option.SCISSORS, Option.ROCK),
      Round(Option.PAPER, Option.SCISSORS)
    )

  val results1 =
    arrayOf(
      Round(Option.SPOCK, Option.ROCK),
      Round(Option.LIZARD, Option.SPOCK),
      Round(Option.ROCK, Option.LIZARD)
    )

  val resultsTie =
    arrayOf(
      Round(Option.SPOCK, Option.ROCK),
      Round(Option.LIZARD, Option.SPOCK),
      Round(Option.ROCK, Option.SPOCK),
      Round(Option.SPOCK, Option.LIZARD)
    )

  val game2 = Game(results2)
  game2.displayResult()

  val game1 = Game(results1)
  game1.displayResult()

  val gameTie = Game(resultsTie)
  gameTie.displayResult()
}

enum class Result(val value: String) {
  PLAYER1("Player 1"),
  PLAYER2("Player 2"),
  TIE("Tie"),
}

enum class Option(val value: String) {
  SCISSORS("✂️"),
  ROCK("🗿"),
  PAPER("📄"),
  LIZARD("🦎"),
  SPOCK("🖖")
}

data class Round(val player1: Option, val player2: Option)

class Game(private val results: Array<Round>) {

  private fun calculateResult(): Result {
    var scorePlayer1 = 0
    var scorePlayer2 = 0

    results.forEach {
      when (whoWins(it.player1, it.player2)) {
        Result.PLAYER1 -> scorePlayer1++
        Result.PLAYER2 -> scorePlayer2++
        Result.TIE -> {
          scorePlayer1++
          scorePlayer2++
        }
      }
    }
    return when {
      scorePlayer1 > scorePlayer2 -> Result.PLAYER1
      scorePlayer1 < scorePlayer2 -> Result.PLAYER2
      else -> Result.TIE
    }
  }

  private fun whoWins(player1: Option, player2: Option): Result {
    if (player1 == player2) return Result.TIE
    val roll = "$player1$player2"

    val winningOption =
      when {
        """^(${Option.ROCK}${Option.SCISSORS}|${Option.SCISSORS}${Option.ROCK})$"""
          .toRegex()
          .matches(roll) -> Option.ROCK
        """^(${Option.ROCK}${Option.LIZARD}|${Option.LIZARD}${Option.ROCK})$"""
          .toRegex()
          .matches(roll) -> Option.ROCK
        """^(${Option.PAPER}${Option.SPOCK}|${Option.SPOCK}${Option.PAPER})$"""
          .toRegex()
          .matches(roll) -> Option.PAPER
        """^(${Option.PAPER}${Option.ROCK}|${Option.ROCK}${Option.PAPER})$"""
          .toRegex()
          .matches(roll) -> Option.PAPER
        """^(${Option.SCISSORS}${Option.PAPER}|${Option.PAPER}${Option.SCISSORS})$"""
          .toRegex()
          .matches(roll) -> Option.SCISSORS
        """^(${Option.SCISSORS}${Option.LIZARD}|${Option.LIZARD}${Option.SCISSORS})$"""
          .toRegex()
          .matches(roll) -> Option.SCISSORS
        """^(${Option.LIZARD}${Option.SPOCK}|${Option.SPOCK}${Option.LIZARD})$"""
          .toRegex()
          .matches(roll) -> Option.LIZARD
        """^(${Option.LIZARD}${Option.PAPER}|${Option.PAPER}${Option.LIZARD})$"""
          .toRegex()
          .matches(roll) -> Option.LIZARD
        """^(${Option.SPOCK}${Option.SCISSORS}|${Option.SCISSORS}${Option.SPOCK})$"""
          .toRegex()
          .matches(roll) -> Option.SPOCK
        else -> {
          Option.SPOCK
        }
      }
    return if (winningOption == player1) Result.PLAYER1 else Result.PLAYER2
  }

  fun displayResult() {
    println(calculateResult().value)
  }
}
