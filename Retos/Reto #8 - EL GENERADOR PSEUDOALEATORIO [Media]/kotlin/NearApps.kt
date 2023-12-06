/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

fun main() {
    /*
        * El fin del aplicativo es NO usar ninguna importación en el archivo
        * desarrollando el problema planteado.
     */
    
    
    //genera 10 números randoms entre 0 y 100
    println(":: Genera 10 números randoms entre 0 y 100 ::")
    for (i in 1..10) {
        println("Random #"+i+": " + generateRandomIntImpl(start = 0, end = 100))
    }

    //::Extra
    //genera 10 números randoms entre 0 y 100 con 4 decimales
    println("\n:: Genera 10 números randoms entre 0 y 100 con 4 decimales ::")
    for (i in 1..10) {
        println("Random Decimal #"+i+": " + generateRandomDecimalImpl(start = 0.0, end = 100.0, round = 4))
    }
}

fun generateRandomIntImpl(
    start: Int   = 0,
    end: Int     = 1
): Int {
    return if(start <= end) {
        val intRange = start..end
        val randomNumber = generateRandomNumber() % intRange.count()
        intRange.first + randomNumber
    } else {
        0
    }
}
fun generateRandomDecimalImpl(
    start: Double   = 0.0,
    end: Double     = 1.0,
    round: Int      = 2
): Double {
    return if(start <= end) {
        val randomInteger = generateRandomIntImpl(
            start = start.toInt(),
            end = (end.toInt() - 1)
        )
        val randomDecimal = generateRandomIntImpl(
            start = 0,
            end = (round * 10)
        )
        return ("$randomInteger.$randomDecimal").toDouble()
    } else {
        0.0
    }
}

//region funciones_auxiliares
fun generateRandomNumber(
    seed: Int = System.nanoTime().toString().takeLast(5).toInt(),
    constant: Int = System.nanoTime().toString().takeLast(4).toInt()
): Int {
    val modulus = System.nanoTime().toString().takeLast(6).toInt()
    val random = (((seed * constant) % modulus) / 100).toString().replace("-","").toInt()
    return random
}
//endregion
