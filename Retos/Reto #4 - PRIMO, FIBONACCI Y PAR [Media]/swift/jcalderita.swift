import Foundation

func isPrime(_ num: Int) -> Bool {
    guard num > 1 else {
        return false
    }
    
    return (1 ... num)
        .filter { num % $0 == 0 }
        .count == 2
}

func isFibonacci(_ num: Int) -> Bool {
    let numberPart = 5 * num * num
    
    let isPerfectSquare: (Int) -> Bool = { n in
        let total = numberPart + n
        let result = Int(sqrt(Double(total)))
        
        return result * result == total
    }
    
    return isPerfectSquare(4) || isPerfectSquare(-4)
}

func isPrimeFibonacciEven(_ num: Int) -> String {
    var msg: String = num.description
    
    if isPrime(num) {
        msg.append(" es primo,")
    } else {
        msg.append(" no es primo,")
    }
    
    if isFibonacci(num) {
        msg.append(" fibonacci ")
    } else {
        msg.append(" no es fibonacci ")
    }
    
    if num % 2 == 0 {
        msg.append("y es par.")
    } else {
        msg.append("y es impar.")
    }
    
    return msg
}

print(isPrimeFibonacciEven(2))
print(isPrimeFibonacciEven(7))