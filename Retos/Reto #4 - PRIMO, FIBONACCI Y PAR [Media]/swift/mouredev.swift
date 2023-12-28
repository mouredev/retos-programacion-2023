import Foundation

func checkPrimeFibonacciEven(number: Int) {

    var result = "\(number) "

    // Primo
    if number > 1 {
        var prime = true
        for index in 2 ..< number {
            if number % index == 0 {
                result += "no es primo, "
                prime = false
                break
            }
        }
        if prime {
            result += "es primo, "
        }
    } else {
        result += "no es primo, "
    }

    // Fibonacci
    result += (number > 0 && (isPerfectSquare(number: 5 * number * number + 4) || isPerfectSquare(number: 5 * number * number - 4))) ? "es fibonacci " : "no es fibonacci "

    // Par
    result += number % 2 == 0 ? "y es par" : "y es impar"

    print(result)
}


func isPerfectSquare(number: Int) -> Bool {
    let sqrt = Int(sqrt(Double(number)))
    return sqrt * sqrt == number
}

checkPrimeFibonacciEven(number: 2)
checkPrimeFibonacciEven(number: 7)
checkPrimeFibonacciEven(number: 0)
checkPrimeFibonacciEven(number: 1)
checkPrimeFibonacciEven(number: -2)
