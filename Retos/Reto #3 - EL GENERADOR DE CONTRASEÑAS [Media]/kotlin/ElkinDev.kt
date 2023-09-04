import kotlin.random.Random

fun main(args: Array<String>) {
    generateString()
}

private fun randomValue(): Char {
    val characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=<>?/[]{}|"
    val index = Random.nextInt(characters.length)
    return characters[index]
}

private fun generateString() {
    val list = mutableListOf<Char>()
    for (i in 1..Random.nextInt(8, 17)) {
        list.add(randomValue())
    }
    val exit: String = buildString {
        for (element in list) {
            if (element is Char) {
                append(element)
            }
        }
    }
    println("your generated password is: $exit")
}



