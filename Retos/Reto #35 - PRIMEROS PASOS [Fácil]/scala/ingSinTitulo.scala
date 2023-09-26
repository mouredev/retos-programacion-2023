object Main extends App {
  // Punto 1: Hola, mundo!
  println("Hola, mundo!")

  // Punto 2: Crea una variable de texto o string
  val miTexto: String = "¡Hola desde Scala!"

  // Punto 3: Crea una variable de número entero
  val miEntero: Int = 42

  // Punto 4: Crea una variable de número con decimales
  val miDecimal: Double = 3.14

  // Punto 5: Crea una variable de tipo booleano
  val miBooleano: Boolean = true

  // Punto 6: Crea una constante
  val MI_CONSTANTE: Int = 10

  // Punto 7: Usa un if, else if y else
  if (miEntero > 50) {
    println("El número es mayor que 50")
  } else if (miEntero < 50) {
    println("El número es menor que 50")
  } else {
    println("El número es igual a 50")
  }

  // Punto 8: Crea un Array
  val miArray: Array[Int] = Array(1, 2, 3, 4, 5)

  // Punto 9: Crea una lista (List en Scala)
  val miLista: List[String] = List("Manzana", "Banana", "Naranja")

  // Punto 10: Crea una tupla
  val miTupla: (Int, String, Double) = (1, "dos", 3.14)

  // Punto 11: Crea un set
  val miSet: Set[String] = Set("Rojo", "Verde", "Azul")

  // Punto 12: Crea un diccionario (Map en Scala)
  val miDiccionario: Map[String, String] = Map(
    "clave1" -> "valor1",
    "clave2" -> "valor2"
  )

  // Punto 13: Usa un ciclo for
  for (elemento <- miArray) {
    println(elemento)
  }

  // Punto 14: Usa un ciclo foreach
  for (elemento <- miLista) {
    println(elemento)
  }

  // Punto 15: Usa un ciclo while (menos común en Scala)
  var contador: Int = 0
  while (contador < 3) {
    println(s"Contador: $contador")
    contador += 1
  }

  // Punto 16: Crea una función sin parámetros que no retorne nada
  def funcionSinParametros(): Unit = {
    println("Función sin parámetros")
  }
  funcionSinParametros()

  // Punto 17: Crea una función con parámetros que no retorne nada
  def funcionConParametros(param1: Int, param2: String): Unit = {
    println(s"Parámetro 1: $param1")
    println(s"Parámetro 2: $param2")
  }
  funcionConParametros(1, "dos")

  // Punto 18: Crea una función con parámetros que retorne valor
  def funcionConRetorno(a: Int, b: Int): Int = {
    a + b
  }
  val resultado: Int = funcionConRetorno(3, 4)
  println(s"Resultado: $resultado")

  // Punto 19: Crea una clase
  class Persona(val nombre: String, val edad: Int)

  // Punto 20: Muestra control de excepciones (try-catch en Scala)
  try {
    val division = miEntero / 0
    println(s"Resultado de la división: $division")
  } catch {
    case e: ArithmeticException =>
      println(s"Error: ${e.getMessage}")
  }
}
