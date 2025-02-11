func isPrime(_ n: Int) -> Bool {
    if n < 2 {
        return false
    }
    for i in 2..<n {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func isFibonacci(_ n: Int) -> Bool {
    guard n >= 0 else {
        return false
    }
    var a = 0, b = 1
    while a < n {
        let temp = a
        a = b
        b += temp
    }
    return a == n
}

func checkNumber(_ n: Int) {
    let prime = isPrime(n) ? "Primo" : "No es primo"
    let fibonacci = isFibonacci(n) ? "Fibonacci" : "No es Fibonacci"
    let even = n.isMultiple(of: 2) ? "Par" : "Impar"
    print("\(n) es \(prime), \(fibonacci) y \(even)")
}

checkNumber(3)
checkNumber(7)