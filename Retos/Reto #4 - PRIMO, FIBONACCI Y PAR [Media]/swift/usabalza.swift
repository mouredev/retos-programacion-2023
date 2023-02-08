import Foundation

func isEven(_ n: Int) -> Bool {
    if n % 2 == 0 {
        return true
    } else {
        return false
    }
}

func isPrime(_ n: Int) -> Bool {
    if n == 0 || n == 1 {
        return false
    } else {
        for i in 2..<n {
            if n % i == 0 {
                return false
            }
        }
        return true
    }
}

func isFibonacci(_ n: Int) -> Bool {
    var c = 0
    var a = 0
    var b = 1
    if n == a || n == b {
        return true
    } else {
        while c < n {
            c = a + b
            b = a
            a = c
        }
        return c == n
    }
}

func evenPrimeFibonacci(_ n: Int) {
    let even = isEven(n) ? "es par" : "es impar"
    let prime = isPrime(n) ? "es primo" : "NO es primo"
    let fibonacci = isFibonacci(n) ? "es fibonacci" : "NO es fibonacci"
    print("\(n) \(even), \(prime) y \(fibonacci)")
}

evenPrimeFibonacci(13)
