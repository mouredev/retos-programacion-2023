fun main() {
    println(rockPaperScissorLizardSpock(arrayOf(Pair(Game.ROCK, Game.ROCK))))
    println(rockPaperScissorLizardSpock(arrayOf(Pair(Game.ROCK, Game.SCISSORS))))
    println(rockPaperScissorLizardSpock(arrayOf(Pair(Game.SCISSORS, Game.ROCK))))
    println(
            rockPaperScissorLizardSpock(
                    arrayOf(
                            Pair(Game.ROCK, Game.ROCK),
                            Pair(Game.ROCK, Game.ROCK),
                            Pair(Game.ROCK, Game.ROCK),
                            Pair(Game.ROCK, Game.ROCK)
                    )
            )
    )
    println(
            rockPaperScissorLizardSpock(
                    arrayOf(
                            Pair(Game.SPOCK, Game.ROCK),
                            Pair(Game.SCISSORS, Game.PAPER),
                            Pair(Game.ROCK, Game.ROCK),
                            Pair(Game.LIZARD, Game.SPOCK)
                    )
            )
    )
}

enum class Game {
    ROCK,
    PAPER,
    SCISSORS,
    LIZARD,
    SPOCK
}

fun rockPaperScissorLizardSpock(games: Array<Pair<Game, Game>>): String {

    val rules: Map<Game, Array<Game>> =
            mapOf(
                    Game.ROCK to arrayOf(Game.SCISSORS, Game.LIZARD),
                    Game.PAPER to arrayOf(Game.ROCK, Game.SPOCK),
                    Game.SCISSORS to arrayOf(Game.PAPER, Game.LIZARD),
                    Game.LIZARD to arrayOf(Game.SPOCK, Game.PAPER),
                    Game.SPOCK to arrayOf(Game.ROCK, Game.SCISSORS)
            )

    var playerOne = 0
    var playerTwo = 0

    for (game in games) {
        if (game.first != game.second) {
            if (rules[game.first]?.contains(game.second) == true) {
                playerOne += 1
            } else {
                playerTwo += 1
            }
        }
    }

    return if (playerOne == playerTwo) "Tie"
    else if (playerOne > playerTwo) "Player 1" else "Player 2"
}

    val rules: Map<Game, Array<Game>> =
            mapOf(
                    Game.ROCK to arrayOf(Game.SCISSORS, Game.LIZARD),
                    Game.PAPER to arrayOf(Game.ROCK, Game.SPOCK),
                    Game.SCISSORS to arrayOf(Game.PAPER, Game.LIZARD),
                    Game.LIZARD to arrayOf(Game.SPOCK, Game.PAPER),
                    Game.SPOCK to arrayOf(Game.ROCK, Game.SCISSORS)
            )

    var playerOne = 0
    var playerTwo = 0

    for (game in games) {
        if (game.first != game.second) {
            if (rules[game.first]?.contains(game.second) == true) {
                playerOne += 1
            } else {
                playerTwo += 1
            }
        }
    }

    return if (playerOne == playerTwo) "Tie"
    else if (playerOne > playerTwo) "Player 1" else "Player 2"
}
