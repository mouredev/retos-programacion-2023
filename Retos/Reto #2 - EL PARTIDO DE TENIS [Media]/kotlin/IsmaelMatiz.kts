/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

fun SetScore(match: Array<String>){
    //Score for each player
    var p1 = 0
    var p2 = 0
    //Posible scores
    val SCORES = arrayOf("Love","15","30","40")
    //Check the input
    match.forEach { if((it.capitalize().equals("P1") || it.capitalize().equals("P2")) == false) {println("Ingresa un valor valido(P1,P2)"); return;}}
    if (match.size > 8) {println("Ingresa hasta 8 rondas"); return;}


    for(round in match){
        //Plus the points per round
        if (round.capitalize().equals("P1")) p1 ++ else p2++
        //if points are less than 3 print the scores otherwise print the words
        if (p1 <= 3 && p2 <= 3){
            println(SCORES[p1]+" - "+SCORES[p2])
        }else{
            if(p1 == p2) println("Deuce")
            else if(p1 > p2) println("Ventaja P1")
            else if (p1 < p2) println("Ventaja P2")
        }
    }

    //finally print which payer won
    println(if (p1 > p2) "Ha ganado el P1" else if (p1 == p2) "Empate" else "Ha ganado el P2")
}

var game = arrayOf("P1", "P1", "P1","P1", "P2","P2","P2","P2")

SetScore(game)

