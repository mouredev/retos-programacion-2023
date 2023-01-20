import Foundation

func fizzbuzz() {

    for number in 1...100 {

        if number % 3 == 0 && number % 5 == 0 {
            print("fizzbuzz")
        } else if number % 3 == 0 {
            print("fizz")
        } else if number % 5 == 0 {
            print("buzz")
        } else {
            print(number)
        }
    }
}

fizzbuzz()