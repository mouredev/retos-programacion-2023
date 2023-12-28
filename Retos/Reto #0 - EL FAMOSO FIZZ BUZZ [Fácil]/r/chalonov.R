#FzzBuzz

fizzbuzz <- function() {
  numbers <- c(1:100)
  for (number in numbers) {
    if (number %% 3 == 0 & number %% 5 == 0) {
      print("FizzBuzz")
    }
    else if (number %% 3 == 0) {
      print("Fizz")
    }
    else if (number %% 5 == 0) {
      print("Buzz")
    }
    else
      print(number)
  }
}

fizzbuzz()