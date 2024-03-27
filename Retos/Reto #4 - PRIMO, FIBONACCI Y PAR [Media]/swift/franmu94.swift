import Foundation

var greeting = "Hello, playground"

//: [Next](@next)

func esPrimo(n: Int) -> Bool {
    guard n >= 3 else {
        return true
    }
    
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    
    var i = 5
    
    while i * i <= n {
        if n % i == 0 || n % (i+2) == 0{
            return false
        }
        
        i += 6
    }
    
    return true
}


func esFibonacci(n : Int) -> Bool {
    var a = 0
    var b = 1
    
    
    while b < n {
        var temp = b
        b += a
        a = temp
        
        if n == b {
            return true
        }
    }
    
    return false
}

func comprobaciones(n: Int) {
    print("\(n) \(esPrimo(n: n) ? "" : "no") es primo, \(esFibonacci(n: n) ? "" : "no ")es fibonacci y es \(n%2 == 0 ? "" : "im")par")
}


comprobaciones(n: 7)
comprobaciones(n: 8)
comprobaciones(n: 111)


