enum class Options{
    Rock,
    Scissors,
    Paper,
    Lizard,
    Spock
}


fun main(args: Array<String>) {
    var game1 = arrayOf(
        arrayOf(Options.Rock, Options.Scissors),
        arrayOf(Options.Scissors, Options.Rock),
        arrayOf(Options.Paper, Options.Scissors)
    )
    var game2 = arrayOf(
        arrayOf(Options.Rock, Options.Scissors), arrayOf(Options.Scissors, Options.Rock), arrayOf(Options.Paper, Options.Scissors),
        arrayOf(Options.Spock, Options.Scissors), arrayOf(Options.Spock, Options.Rock), arrayOf(Options.Paper, Options.Rock)
    )
    var  pointsP1 = 0
    var  pointsP2 = 0

        for (game in game1){
            if(whoWins(game).equals("Tie")){
                pointsP1++
                pointsP2
            }else if (whoWins(game).equals("P1")){
                pointsP1++
            }else{
                pointsP2++
            }
        }

        println(
            if (pointsP1 == pointsP2) "Tie"
            else if (pointsP1 > pointsP2) "Player 1"
            else "Player 2"
        )
}

fun whoWins(game: Array<Options>): String {

    var chooseP1 = game.get(0)
    var chooseP2 = game.get(1)


    var rules: MutableMap<Options, ArrayList<Options>> = hashMapOf(
        Options.Rock to arrayListOf(Options.Scissors, Options.Lizard),
        Options.Scissors to arrayListOf(Options.Paper, Options.Lizard),
        Options.Lizard to arrayListOf(Options.Spock, Options.Paper),
        Options.Paper to arrayListOf(Options.Spock, Options.Rock),
        Options.Spock to arrayListOf(Options.Scissors, Options.Rock)
    )

    if (chooseP1 == chooseP2) return "Tie"

    rules[chooseP1]?.forEach {
        if (it.equals(chooseP2)) {
            return "P1"
        }
    }
    return "P2"
}