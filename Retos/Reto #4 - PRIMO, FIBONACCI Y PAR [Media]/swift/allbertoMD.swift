import Foundation

print("Introduce el número que quieras comprobar:")
guard let number = readLine() else {
    fatalError()
}
let numberInput = UInt(number) ?? 1

isPrime(numberIsPrime: numberInput)
isFibonacci(numberIsFibonacci: numberInput)
isEven(numberIsEven: numberInput)


func isPrime(numberIsPrime number: UInt) {
    var counter = 0
    for n in 1...number {
        if number % n == 0 {
            counter += 1
        }
    }
    if counter == 2 {
        print("Es primo.")
    } else {
        print("No es primo.")
    }
}

func isFibonacci(numberIsFibonacci number: UInt) {
    var fibonacciNumbers = [0, 1]
    var lastFibonacci = fibonacciNumbers.last!
    var fNumber = 0
    var sNumber = 0
    var add = 0
    var stteperFNumber = 0
    var stteperSNumber = 1
    
    while number > lastFibonacci {
        
        fNumber = fibonacciNumbers[stteperFNumber]
        sNumber = fibonacciNumbers[stteperSNumber]
        add = fNumber + sNumber
        fibonacciNumbers.append(add)
        stteperFNumber += 1
        stteperSNumber += 1
        lastFibonacci = fibonacciNumbers.last!

    }
    
    if fibonacciNumbers.contains(Int(number)) {
        print("Es fibonacci.")
    } else {
        print("No es fibonacci.")
    }
}

func isEven(numberIsEven number: UInt) {
    if number % 2 == 0 {
        print("Es par.")
    } else {
        print("No es par.")
    }
}

