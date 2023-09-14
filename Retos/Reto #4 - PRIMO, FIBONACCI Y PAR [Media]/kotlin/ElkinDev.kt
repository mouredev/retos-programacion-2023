/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
fun nPrimo(numero: Int): Boolean {
   if (numero <= 1) return false

   for (i in 2 until numero) {
       if (numero % i == 0) {
           return false
       }
   }
   return true
}

fun nFibonacci(numero: Int): Boolean {
   var a = 0
   var b = 1
   while (b < numero) {
       val siguiente = a + b
       a = b
       b = siguiente
   }
   return b == numero || numero == 0
}

fun nPar(numero: Int): Boolean {
   return numero % 2 == 0
}

fun ejecuta(n: Int) {
   val esPrimo = nPrimo(n)
   val esFibonacci = nFibonacci(n)
   val esPar = nPar(n)

   val mensaje = buildString {
       append("$n es")
       if (esPrimo) append(" primo")
       if (esFibonacci) append(" fibonacci")
       if (esPar) append(" par")

       if (!esPrimo && !esFibonacci && !esPar) {
           append(" no cumple con ninguna de las condiciones anteriores")
       }
   }
   println(mensaje)
}

fun main() {
   ejecuta(7)
}
