fun main() {
    println("Introduce un nuevo numero para empezar el juego")
    execute(readLine() ?: "")
}

var sum : Int = 0
fun execute(letters: String) {
    if (!containsOnlyLetters(letters) || letters.isEmpty()) {
        println("Introduce un valor correcto")
        execute(readLine() ?: "")
        return
    }
    val result = calculate(letters)
    println("current result: $result")
    sum += result
    println("total sum: $sum")

    if (sum < 100) {
        println("Introduce un nuevo valor")
        execute(readLine() ?: "")
        return
    }
    if (sum > 100) {
        println("Te has pasado :( vuelve a intentarlo")
        sum = 0
        return
    }
    sum = 0
    println("Has ganado!!!")
}

fun calculate(letters: String) : Int {
    return letters.toList().mapNotNull {
        letter -> alphabet[letter]
    }.sum()
}

fun containsOnlyLetters(input: String): Boolean {
    return input.all { it.isLetter() }
}

val alphabet: Map<Char, Int> = mapOf(
        'a' to 1,
        'b' to 2,
        'c' to 3,
        'd' to 4,
        'e' to 5,
        'f' to 6,
        'g' to 7,
        'h' to 8,
        'i' to 9,
        'j' to 10,
        'k' to 11,
        'l' to 12,
        'm' to 13,
        'n' to 14,
        'ñ' to 15,
        'o' to 16,
        'p' to 17,
        'q' to 18,
        'r' to 19,
        's' to 20,
        't' to 21,
        'u' to 22,
        'v' to 23,
        'w' to 24,
        'x' to 25,
        'y' to 26,
        'z' to 27
)
