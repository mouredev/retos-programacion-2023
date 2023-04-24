@main
def main(): Unit = {
  for (i <- 1 until 100) {
      if ((i % 3 == 0) && (i % 5 == 0)) println("fizzbuzz")
      else if (i % 5 == 0) println("buzz")
      else if (i % 3 == 0) println("fizz")
      else println(i)
    }
}