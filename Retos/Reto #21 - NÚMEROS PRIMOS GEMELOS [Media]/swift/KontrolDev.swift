import UIKit

func isPrime(_ number: Int) -> Bool {
    if number <= 1 {
        return false
    }
    
    for i in 2..<number {
        if number % i == 0 {
            return false
        }
    }
    
    return true
}

func findTwinPrimes(inRange range: Int) {
    for i in 2..<(range - 1) {
        if isPrime(i) && isPrime(i + 2) {
            print("(\(i), \(i + 2))")
        }
    }
}

let range = 14
findTwinPrimes(inRange: range)
