fun main() {
    result(listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"))
}

fun result(point:List<String>){
    var player1point = 0
    var player2point = 0
    val game = arrayOf("Love", "15", "30", "40")

    point.forEach {player ->
        player1point += if (player == "P1") 1 else 0
        player2point += if (player == "P2") 1 else 0

        if (player1point >= 3 && player2point >= 3){
            if (player1point - player2point <= 1){
                println(
                    if (player1point == player2point)"Deuce"
                    else if (player1point > player2point) "Ventaja P1"
                    else "Ventaja P2")
            }
        }else{
            if (player1point < 4 && player2point < 4){
                println("${game[player1point]} - ${game[player2point]}")
            }
        }
    }
    println(
        if (player1point > player2point) "Ha ganado el P1"
        else "Ha ganado el P2"
    )
}