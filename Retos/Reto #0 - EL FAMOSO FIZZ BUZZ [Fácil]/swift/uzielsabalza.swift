import UIKit

func fizzBuzz() {
    for i in 1...100 {
        if moduleThree(i) || moduleFive(i) {
            var string = ""
            if moduleThree(i) {
                string.append("fizz")
            }
            if moduleFive(i) {
                string.append("buzz")
            }
            print(string)
        } else {
            print(i)
        }
    }
}

func moduleThree(_ n: Int) -> Bool {
    return n % 3 == 0
}

func moduleFive(_ n: Int) -> Bool {
    return n % 5 == 0
}

fizzBuzz()
