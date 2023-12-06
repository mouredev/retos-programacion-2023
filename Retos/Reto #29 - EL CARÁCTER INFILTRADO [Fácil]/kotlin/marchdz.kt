fun findDistinctChars(firstString: String, secondString: String): Any {
    val distinctChars = mutableListOf<Char>()
    return if (firstString.length == secondString.length) {
        for (index in firstString.indices) {
            if (firstString[index] != secondString[index]) {
                distinctChars += secondString[index]
            }
        }
        distinctChars.ifEmpty { "Las cadenas de texto son iguales" }
    } else {
        distinctChars.ifEmpty { "Las cadenas de texto deben tener la misma longitud" }
    }
}

fun main() {
    println(findDistinctChars("Me llamo mouredev", "Me llemo mouredov"))        // [e, o]
    println(findDistinctChars("Me llamo.Brais Moure", "Me llamo brais moure"))  // [ , b, m]
    println(findDistinctChars("Me llamo.Brais Moure", "Me llamo brais moure ")) // Las cadenas de texto deben tener la misma longitud
    println(findDistinctChars("Me llamo mouredev", "Me llamo mouredev"))        // Las cadenas de texto son iguales
}