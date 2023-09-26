import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)
    print("Ingrese una cadena de texto: ")
    val str = scanner.nextLine()

    if (isHeterogram(str)) {
        println("La cadena es un heterograma.")
    } else {
        println("La cadena no es un heterograma.")
    }

    if (isIsogram(str)) {
        println("La cadena es un isograma.")
    } else {
        println("La cadena no es un isograma.")
    }

    if (isPangram(str)) {
        println("La cadena es un pangrama.")
    } else {
        println("La cadena no es un pangrama.")
    }
}

// Función para detectar si una cadena es un heterograma
fun isHeterogram(str: String): Boolean {
    val charCount = IntArray(26)
    for (c in str) {
        if (c.isLetter()) {
            val index = c.toLowerCase() - 'a'
            if (charCount[index] > 0) {
                return false
            }
            charCount[index]++
        }
    }
    return true
}

// Función para detectar si una cadena es un isograma
fun isIsogram(str: String): Boolean {
    val charCount = IntArray(26)
    for (c in str) {
        if (c.isLetter()) {
            val index = c.toLowerCase() - 'a'
            if (charCount[index] > 0) {
                return false
            }
            charCount[index]++
        }
    }
    return true
}

// Función para detectar si una cadena es un pangrama
fun isPangram(str: String): Boolean {
    val charSet = HashSet<Char>()
    for (c in str) {
        if (c.isLetter()) {
            charSet.add(c.toLowerCase())
        }
    }
    return charSet.size == 26
}
