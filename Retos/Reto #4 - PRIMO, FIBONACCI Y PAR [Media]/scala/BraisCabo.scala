import scala.io.StdIn.readLine


def primo(num: Int): String = {
  for (a <- 2 to num - 1) {
    if (num % a == 0)
      return num.toString + " no es primo,"
  }
  num.toString + " es primo,"
}

def par(num: Int): String = {
  if (num % 2 == 0) {
    return " es par."
  }
  " no es par."
}

def fibonacci(num: Int): String = {
  var intFibo1 = 0
  var intFibo2 = 1
  var intAuxiliar = 0
  while (intFibo1 + intFibo2 <= num) {
    intAuxiliar = intFibo1;
    intFibo1 = intFibo2;
    intFibo2 = intAuxiliar + intFibo1;
    if (num == intFibo2) {
      return " es fibonacci,"
    }
  }
  return " no es fibonacci,"
}

@main def reto2 = {
  val num = readLine().toInt
  println(primo(num) + fibonacci(num) + par(num))