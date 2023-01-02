@main def reto0 = {
  def fizzbuff: Unit = {
    for (a <- 1 to 100) {
      a match {
        case num if (num % 3 == 0 && num % 5 == 0) => print("fizzbuzz")
        case num if (num % 3 == 0) => print("fizz")
        case num if (num % 5 == 0) => print("buzz")
        case num => print(num)
      }
      print("\n")
    }
  }

  fizzbuff
}
