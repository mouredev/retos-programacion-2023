import Foundation

func printTwinsPrimeNumbers(until: Int) {
    var primes: [Int] = []
    var twins: [(Int, Int)] = []
    
    if until > 1 {
        for n in 2...until {
            var isPrime = true
            let sqrtN = Int(Double(n).squareRoot()) + 1
            
            for m in 2...sqrtN {
                if n % m == 0 {
                    isPrime = false
                    break
                }
            }
            
            if isPrime {
                primes.append(n)
                
                if primes.count >= 2 && primes[primes.count - 1] - primes[primes.count - 2] == 2 {
                    twins.append((primes[primes.count - 2], primes[primes.count - 1]))
                }
            }
        }
        
        if twins.count < 2 {
            print("No hay numeros primos gemelos hasta \(until)")
        }
        
    } else {
        print("El numero tiene que ser mayor a 1")
    }
    
    for t in twins {
        print(t)
    }
}

print("Introduce un numero hasta donde quieres los numeros primos gemelos")

var validInput = false

while !validInput {
    if let input = readLine(), let number = Int(input) {
        printTwinsPrimeNumbers(until: number)
        validInput = true
    } else {
        print("Tienes que introducir un numero")
    }
}
