package com.malopezrom.reto6
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

main()

fun main() {


    val game1 = Game(listOf(
                     listOf(Options.ROCK, Options.SCISSORS),
                     listOf(Options.SCISSORS, Options.ROCK),
                     listOf(Options.LIZARD, Options.SCISSORS),
                     listOf(Options.ROCK, Options.PAPER),
                     listOf(Options.PAPER, Options.ROCK),
                     listOf(Options.ROCK, Options.ROCK),
                     listOf(Options.SPOCK, Options.LIZARD),
                     listOf(Options.SPOCK, Options.SCISSORS)), "Player 1", "Player 2")

    println("el resultado es : ${evaluateGame(game1)}")

    val game3 = Game(listOf(
            listOf(Options.ROCK, Options.SCISSORS),
            listOf(Options.LIZARD, Options.SCISSORS),
            listOf(Options.SPOCK, Options.ROCK),
            listOf(Options.SPOCK, Options.SPOCK)), "Player 1", "Player 2")

    println("el resultado es : ${evaluateGame(game3)}")

    val game2 = Game(listOf(
            listOf(Options.SPOCK, Options.LIZARD),
            listOf(Options.LIZARD, Options.SPOCK),
            listOf(Options.SPOCK, Options.SPOCK)), "Player 1", "Player 2")

    println("el resultado es : ${evaluateGame(game2)}")



}

enum class Result {
    Player1, Player2, Tie
}


enum class Options(val icon: String) {
    ROCK("🗿"),
    PAPER("📄"),
    SCISSORS("✂️"),
    LIZARD("🦎"),
    SPOCK("🖖")
}


data class Game(val listOfGame:List<List<Options>>,val player1: String, val player2: String)


fun foundWinner(results : List<Result?>): Result {
    val player1 = results.count { it == Result.Player1 }
    val player2 = results.count { it == Result.Player2 }
    return if (player1 > player2) Result.Player1 else if (player2 > player1) Result.Player2 else Result.Tie
}
fun evaluateGame(game: Game): String {

    val combinations = mapOf(
            //Piedra
            "🗿" to mapOf("🗿" to Result.Tie, "📄" to Result.Player2, "✂️" to Result.Player1, "🦎" to Result.Player1, "🖖" to Result.Player2),
            //Papel
            "📄" to mapOf("🗿" to Result.Player1, "📄" to Result.Tie, "✂️" to Result.Player2, "🦎" to Result.Player2, "🖖" to Result.Player1),
            //Tijera
            "✂️" to mapOf("🗿" to Result.Player2, "📄" to Result.Player1, "✂️" to Result.Tie, "🦎" to  Result.Player1, "🖖" to Result.Player2),
            //Lagarto
            "🦎" to mapOf("🗿" to Result.Player2, "📄" to Result.Player1, "✂️" to Result.Player2, "🦎" to Result.Tie, "🖖" to Result.Player1),
            //Spock
            "🖖" to mapOf("🗿" to Result.Player1, "📄" to Result.Player2, "✂️" to Result.Player1, "🦎" to Result.Player2, "🖖" to Result.Tie)

    )

    val values = game.listOfGame.map {
        val value = combinations[it[0].icon]?.get(it[1].icon)
        value

    }

    return when (foundWinner(values)) {
        Result.Player1 -> game.player1
        Result.Player2 -> game.player2
        Result.Tie -> "Tie"
    }


}