fun main() {
    // Creamos un ábaco de ejemplo para probar la función
    val abaco = abacoPorDefecto()

    // Imprimimos el ábaco, it representa el elemento actual de la iteración.
    representarAbaco(abaco)

    // Calculamos el valor del ábaco
    val numero: Int = calcularValorAbaco(abaco) // numero a representar

    println("El número representado es: $numero")
}

// Función que calcula el valor de un ábaco.
private fun calcularValorAbaco(abaco: List<String>): Int {
    var numero = 0 // numero a representar
    var multiplicador = 1 // multiplicador
    // recorremos el array al reves
    for (i in abaco.size - 1 downTo 0) {
        // contamos cuantos 0 hay en la fila antes de "---"
        val ceros = abaco[i].substring(0, abaco[i].indexOf("-")).length
        // sumamos al numero los ceros por el multiplicador
        numero += ceros * multiplicador
        multiplicador *= 10 // aumentamos el multiplicador
    }
    return numero
}

// Función que imprime un ábaco
private fun representarAbaco(abaco: List<String>) {
    println("El ábaco a representar es:")
    abaco.forEach {
        println(it)
    }
}

// Función que crea un ábaco por defecto
fun abacoPorDefecto(): List<String> {
    return listOf(
        "0---00000000",
        "00---0000000",
        "000---000000",
        "0000---00000",
        "00000---0000",
        "000000---000",
        "0000000---00"
    )
}
