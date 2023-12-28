fun main() {

  /*
   * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
   * Ejemplos:
   * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
   * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
   */

  println(describeNumber(2))
  println(describeNumber(7))
  println(describeNumber(0))
  println(describeNumber(1))
  println(describeNumber(113))
  println(describeNumber(-8))
  println(describeNumber(89))
}

private fun describeNumber(number: Int): String {
  return "$number " +
      "${if (isPrime(number)) "es primo" else "no es primo"}, " +
      "${if (isFibonacci(number)) "es fibonacci" else "no es fibonacci"} y " +
      if (isEven(number)) "es par" else "es impar"
}

private fun isEven(number: Int) = number % 2 == 0

private fun isPrime(number: Int): Boolean {
  if (number == 0 || number == 1 || number < 0) return false
  for (i in 2 until number) if (number % i == 0) return false
  return true
}

private fun isFibonacci(number: Int): Boolean {
  if (number < 0) return false
  val fibonacciNumbers = mutableListOf(0, 1)
  var count = 2
  while (fibonacciNumbers.last() < number) {
    fibonacciNumbers.add(fibonacciNumbers[count - 1] + fibonacciNumbers[count - 2])
    count++
  }
  return fibonacciNumbers.contains(number)
}
