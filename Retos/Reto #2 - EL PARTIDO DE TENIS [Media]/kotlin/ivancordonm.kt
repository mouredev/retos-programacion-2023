fun main() {

    var score = 0 to 0
    val points = listOf("Love", "15", "30", "40")

    fun String.score() =
        when (this) {
            ("P1") ->
                score = score.first + 1 to score.second

            ("P2") ->
                score = score.first to score.second + 1

            else -> println("undefined player")
        }

    fun List<String>.play() {
        for (p in this) {
            p.score()
            when (true) {
                (score.first == score.second && score.first == 3) -> println("Deuce")
                (score.first == score.second && score.first == 4) -> {
                    score = 3 to 3
                    println("Deuce")
                }

                (score.first == 4) -> println("Ventaja P1")
                (score.second == 4) -> println("Ventaja P2")
                (score.first == 5) -> {
                    println("Ha ganado el P1")
                    break
                }

                (score.second == 5) -> {
                    println("Ha ganado el  P2")
                    break
                }

                else -> println("${points[score.first]} - ${points[score.second]}")
            }
        }
    }

    listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1").play()
    println()
    score = 0 to 0
    listOf("P2", "P1", "P2", "P2", "P2", "P2", "P2", "P1").play()
    println()
    score = 0 to 0
    listOf("P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1","P2", "P1","P2", "P2").play()
}
