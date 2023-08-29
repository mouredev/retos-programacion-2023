fun main() {
    // Hola, mundo!
    println("Hola, mundo!")

    // Variables
    val myString = "Hola, soy un string"
    val myInteger = 69
    val myFloat = 3.14159
    val myBoolean = false

    // Constante
    val PI = 3.14159

    // Estructuras de datos
    val myArray = arrayOf(1, 2, 3, 4, 5, 6, 7, 8)
    val myList = listOf("lima", "limon", "mandarina")
    val myTuple = Triple(1, 2, 3)
    val mySet = setOf(1, 2, 3, 4, 5, 6)
    val myDictionary = mapOf("nombre" to "Juan", "edad" to 30, "ciudad" to "Barcelona")

    // Condiciones
    val myNumber = 1
    if (myNumber > 1) {
        println("El número es mayor que 1")
    } else if (myNumber == 1) {
        println("El número es igual a 1")
    } else {
        println("El número es menor que 1")
    }

    // Bucles
    // For Each (a través de un bucle for)
    for (num in myArray) {
        println(num)
    }

    // While
    var count = 0
    while (count < 5) {
        println("Contador: $count")
        count++
    }

    // Funciones
    fun add(a: Int, b: Int): Int {
        return a + b
    }

    fun hello(nombre: String) {
        println("Hola, $nombre")
    }

    fun isEven(number: Int): Boolean {
        return number % 2 == 0
    }

    // Clase
    class Person(val name: String, val age: Int) {
        fun hello() {
            println("Hola, soy $name")
        }
    }

    // Control de excepciones
    try {
        val result = 5 / 0
    } catch (e: ArithmeticException) {
        println("Error: división por cero")
    }
}
