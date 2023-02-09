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

enum class JUGADORES {P1,P2}
fun main(){

    val marcador= arrayOf(JUGADORES.P1,JUGADORES.P1,JUGADORES.P2,JUGADORES.P2,JUGADORES.P1,JUGADORES.P2,JUGADORES.P1,JUGADORES.P1)
    val puntuacion= arrayOf("Love","15","30","40","Deuce","Ventaja")
    var jugador1=0
    var jugador2=0

    for (punto in marcador){
        when (punto){
            JUGADORES.P1 -> jugador1++
            JUGADORES.P2 -> jugador2++
        }
        imprimirMarcador(jugador1,jugador2,puntuacion)
    }

}

fun imprimirMarcador(J1:Int, J2:Int,puntuacion:Array<String> ) {

    if(J1<=3 && J2<=3){
        if ( J1==3 && J2==3) println(puntuacion[4])
        else println(puntuacion[J1]+":"+puntuacion[J2])
    }else{
        when(J1-J2){
            -1-> println(puntuacion[5]+" P2")
            -2-> println("Ha gandado P2")
            0-> println(puntuacion[4])
            1-> println(puntuacion[5]+" P1")
            2-> println("Ha gandado P1")
        }
    }
}