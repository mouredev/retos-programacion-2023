def genPassword(lenght: Int, containsMayus: Boolean, containsNumbers: Boolean, containsSymbols: Boolean): String = {
  val leters = if (containsMayus) LazyList.range(65, 91) ++ LazyList.range(97, 123) else LazyList.range(97, 123)
  val numbers = if (containsNumbers) LazyList.range(48, 58) else LazyList.empty
  val symbols = if (containsSymbols) LazyList.range(33, 48) ++ LazyList.range(58, 65) else LazyList.empty

  val all = leters ++ numbers ++ symbols
  LazyList.tabulate(lenght)(_ => all(Random.nextInt(all.size)).toChar).mkString
}

@main
def main(): Unit = {
  println(genPassword(16, true, true, true))
}
