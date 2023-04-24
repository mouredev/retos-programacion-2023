fun main(args: Array<String>) {

    var puntosP1 = 0
    var puntosP2 = 0

    val puntos = listOf<String>("Love","15","30","40","Deuce","Ventaja")

    var ganador = "Nadie"

    var ganadorPunto: String

    while (ganador.equals("Nadie")){
        println("¿Quien ha ganado el punto?")
        ganadorPunto = readln()

        if (ganadorPunto.equals("P1")){
            puntosP1++
            if (puntosP1 == 3 && puntosP2 == 3){
                println(puntos[4])
            }else if (puntosP1 == 4 && puntosP2 == 3){
                println(puntos[5] + " P1")
            }else if (puntosP1 == 4 && puntosP2 == 4){
                puntosP2--
                puntosP1--
                println(puntos[4])
            }else if (puntosP1 - puntosP2 >= 2 && puntosP1 >= 4){
                ganador = "Ganador P1"
                println(ganador)
            }else{
                println(puntos[puntosP1] + " - " + puntos[puntosP2])
            }
        }else if (ganadorPunto.equals("P2")) {
            puntosP2++
            if (puntosP1 == 3 && puntosP2 == 3) {
                println(puntos[4])
            } else if (puntosP2 == 4 && puntosP1 == 3) {
                println(puntos[5] + " P2")
            }else if (puntosP2 == 4 && puntosP1 == 4) {
                puntosP1--
                puntosP2--
                println(puntos[4])
            }else if (puntosP2 - puntosP1 >= 2 && puntosP2 >= 4) {
                ganador = "Ganador P2"
                println(ganador)
            }else{
                println(puntos[puntosP1] + " - " + puntos[puntosP2])
            }
        }else{
            println("Escriba solo P1 o P2")
        }
    }

    println("Partido finalizado")

}