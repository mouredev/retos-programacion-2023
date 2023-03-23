package com.cursosant.android.retosprogramacion2223

import kotlin.system.exitProcess

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

fun main(){
    var primerPartido = arrayOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1") //Partido de ejemplo
    var segundoPartido = arrayOf("P1", "P1", "P1", "sdafas", "P1", "P1", "P1", "P1") //Paliza del P1
    var tercerPartido = arrayOf("P1", "P2", "P1", "sdafas", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P2") //Juego interminable
    //puntuaJuego(primerPartido)
    //puntuaJuego(segundoPartido)
    puntuaJuego(tercerPartido)

}

fun puntuaJuego(puntuacion: Array<String>){

    var scoreP1 = 0
    var scoreP2 = 0
    println()
    println("Jugadores a sus puestos, comienza el partido: ")
    println("_____________________________________________ ")
    for (punto in puntuacion){
        var checkVal = 0
        when(punto){
            "P1"->{
                scoreP1++

            }
            "P2"->{
                scoreP2++
            }else->{
            checkVal = 1
            }

        }
        if(scoreP1>3 || scoreP2>3){ //Deuce, a partir de 40, siempre que empatan es Deuce
            if ( scoreP1 == scoreP2 ) {
                scoreP1 = 3
                scoreP2 = 3
            }
        }


        if ((scoreP1 == 5) || (scoreP1>=4 && scoreP2<=2)){
            println("Ha ganado el P1!!!. Fin del partido, esperamos que vuelvan al próximo Open Moure")
            exitProcess(0)

        }
        if ((scoreP2 == 5)|| (scoreP2>=4 && scoreP1<=2)){
            println("Ha ganado el P2!!!. Fin del partido, esperamos que vuelvan al próximo Open Moure")
            exitProcess(0)

        }
        println(decisionJuez(scoreP1, scoreP2, checkVal))
    }
}

fun decisionJuez(p1: Int, p2: Int, e: Int): String {
    val scoreTable = arrayOf("Love", 15, 30, 40,"Ventaja")
    if(e == 1){
        return("Habrá que revisar el ojo de halcón o repetir el punto...")

    }

    if(p1==3 && p2==3){
        return("Deuce")
    }
    if(p1 == 4){
        return("Ventaja P1")
    }
    if(p2 == 4){
        return("Ventaja P2")
    }
    if(p1<5 && p2<5 ){
        return(scoreTable[p1].toString() + " - " + scoreTable[p2])
    }

    return ""
}

