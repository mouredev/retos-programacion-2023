fun main() {
    printRandomNumber(0,100)
}
fun random(): Int {
    /*
    * nanoTime() returns the current value of JVM's time source with nanosecond precision
     */
    return (System.nanoTime() % 101).toInt()
}

fun printRandomNumber(initial:Int, end:Int){
    for (i in (initial..end)) {
        println("Aleatorio N°$i: ${random()}")
    }
}