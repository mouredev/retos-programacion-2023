fun main() {

    /*
    * Reto #39 02/10/2023  TRIPLES PITAGÓRICOS
    *
    * Crea una función que encuentre todos los triples pitagóricos
    * (ternas) menores o iguales a un número dado.
    * - Debes buscar información sobre qué es un triple pitagórico.
    * - La función únicamente recibe el número máximo que puede
    *   aparecer en el triple.
    * - Ejemplo: Los triples menores o iguales a 10 están
    *   formados por (3, 4, 5) y (6, 8, 10).
    */

    // Tres números enteros a , b , c que satisfacen la ecuación del teorema de Pitágoras
    // ( a 2 + b 2 = c 2 ) son llamados triples Pitagóricos .

    val numMaximo = 10

    println("Los triples pitagoricos menores o iguales a $numMaximo son ${findTriplesPitagoricos(numMaximo)}")


}

fun findTriplesPitagoricos(numMaximo: Int): List<List<Int>> {
    var triplesPitagoricos = mutableListOf<List<Int>>()

    (1..numMaximo).forEach { a ->

        (a..numMaximo).forEach { b ->

            (b..numMaximo).forEach { c ->

                if ((a !== b) && (b !== c) && (a !== c)) {
                    if ((a * a + b * b) == (c * c)) {
                        triplesPitagoricos.add(listOf(a, b, c))

                    }

                }

            } // c

        } // b

    } // a

    return triplesPitagoricos

}
