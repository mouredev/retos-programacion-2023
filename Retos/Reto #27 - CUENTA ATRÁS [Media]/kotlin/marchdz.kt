fun countdown(seconds: Int, delay: Int) {
    if (seconds >= 0 && delay >= 0) {
        print(seconds)
        for (number in seconds - 1 downTo 0) {
            Thread.sleep((delay * 1000).toLong())
            print(", $number")
        }
    } else println("Sólo se aceptan números enteros positivos")
}

fun main() {
    countdown(10, 1)
}