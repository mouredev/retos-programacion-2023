func fizzBuzz() -> Void {
  let initialNumber: Int = 0
  let finalNumber: Int = 100

  for number in initialNumber...finalNumber{

    if (number % 3 == 0 && number % 5 == 0) {
        print("fizzbuzz")
    }
    else if (number % 3 == 0){
        print("fizz")
    }
    else if (number % 5 == 0){
        print("buzz")
    }
    else {
        print(number)
    }
  }
}

fizzBuzz()