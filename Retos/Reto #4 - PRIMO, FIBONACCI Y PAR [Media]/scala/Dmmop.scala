import scala.annotation.tailrec

def fibonnaci(i: Int) = {
  @tailrec def fib(n: Int, acc1: Int, acc2: Int): Int =
    n match
      case 0 => acc1
      case 1 => acc2
      case _ => fib(n - 1, acc2, acc1 + acc2)

  fib(i, 0, 1)
}

def esPar(n: Int): Boolean = n % 2 == 0
def esPrimo(n: Int): Boolean = !(n - 1 until 1 by -1).exists(n % _ == 0)
def esFib(n: Int): Boolean = LazyList.from(0).map(fibonnaci).takeWhile(_ <= n).contains(n)

def eval(n: Int): String =
  f"""$n ${if esPrimo(n) then "es" else "no es"} primo, ${if esFib(n) then "es" else "no es"} fibonacci y ${if esPar(n) then "es" else "no es"} par"""


@main
def main(): Unit = {
  println(eval(2))
  println(eval(3))
  println(eval(7))
  println(eval(10))
  println(eval(13))
}