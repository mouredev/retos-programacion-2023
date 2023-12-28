fun main() {
    var seed = System.currentTimeMillis() % 100 // Semilla inicial basada en el tiempo actual
    repeat(10) {
        seed = (seed * 1103515245 + 12345) % (1 shl 31) // Algoritmo lineal congruencial
        val random = seed % 101 // Número pseudoaleatorio entre 0 y 100
        println(random)
    }
}
