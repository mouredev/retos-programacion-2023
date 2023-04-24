class Player(){
    var score = 0;
}


val posibilidades = listOf("Love", "15", "30", "40")

val P1 = Player()
val P2 = Player()



fun Match(partido:List<Player>){
    for(i in partido){
        if(i == P1){P1.score += 1} else {P2.score += 1}
        if(P1.score == 4){
            println("Ventaja ${P1.score - P2.score}")
            println("Gana el P1")
        } else if( P2.score == 4){
            println("Ventaja ${P2.score - P1.score}")
            println("Gana el P2")
        }
        if(P1.score == P2.score){println("Deuce")} else {println("${posibilidades[P1.score]} - ${posibilidades[P2.score]}")}
        
                
    }
}

fun main() {
   Match(listOf(P1, P1, P2, P2, P1, P2, P1, P1))
}