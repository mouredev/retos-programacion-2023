fun main() {
    print(randomNumber())
}

fun randomNumber(): Int {
    val time = System.currentTimeMillis().toString()
    var number = time.substring(time.length - 3, time.length).toInt()

    if (number > 100) {
        number %= 100
    }
    return number
}