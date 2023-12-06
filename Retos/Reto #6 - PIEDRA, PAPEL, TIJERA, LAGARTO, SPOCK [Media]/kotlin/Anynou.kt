fun main(){
    var P1: Int = 0
    var P2: Int = 0
    var winner: Int
    var data = listOf(
        listOf("spock", "tijera"),
        listOf("papel", "lagarto"),
        listOf("piedra", "papel"),
        listOf("spock", "lagarto"),
        listOf("tijera", "tijera"),
        listOf("papel", "piedra")
    )
    for (play in data){

        winner = check_winner(play[0], play[1])

        if (winner == 1){
            P1 += 1
        } else if (winner == 2){
            P2 += 1
        } else if (winner == 0){
        }

    }

    if (P1 > P2){
        println("Gana P1")
    } else if (P2 > P1){
        println("Gana P2")
    } else {
        println("Empate")
    }
    
}

fun check_winner(word1: String, word2: String): Int {

    var winner: Int = 0


    if (word1 == "tijera"){

        if ((word2 == "papel") || (word2 == "lagarto")){           
            winner = 1
        } else if ((word2 == "spock") || (word2 == "piedra")){
            winner = 2
        } else if (word2 == "tijera"){
            winner = 0
        }

    }
        

    if (word1 == "papel"){

        if ((word2 == "piedra") || (word2 == "spock")){
            winner = 1
        } else if ((word2 == "tijera") || (word2 == "lagarto")){
            winner = 2
        } else if (word2 == "papel"){
            winner = 0
        }

    }

    if (word1 == "piedra"){
        if ((word2 == "lagarto") || (word2 == "tijera")){
            winner = 1
        } else if ((word2 == "spock") || (word2 == "papel")){
            winner = 2
        } else if (word2 == "piedra"){
            winner = 0
        }

    }

    if (word1 == "lagarto"){
        if ((word2 == "papel") || (word2 == "spock")){
            winner = 1
        } else if ((word2 == "tijera") || (word2 == "piedra")){
            winner = 2
        } else if (word2 == "lagarto"){
            winner = 0
        }

    }

    if (word1 == "spock"){
        if ((word2 == "tijera") || (word2 == "piedra")){
            winner = 1
        } else if ((word2 == "papel") || (word2 == "lagarto")){
            winner = 2
        } else if (word2 == "spock"){
            winner = 0
        }
        
    }
    
    return winner


}


// Rules
    // tijera > papel
    // papel > piedra
    // piedra > lagarto
    // lagarto > spock
    // spock > tijera
    // tijera > lagarto
    // lagarto > papel
    // papel > spock
    // spock > piedra
    // piedra > tijera
