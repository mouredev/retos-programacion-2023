import Foundation

func isPrime(_ number: Int) -> Bool {
    if(number < 2) {
        return false
    } else {
        var result = true
        (2..<number).forEach { partialNumber in
            if(number % partialNumber == 0) {
                result = false
            }
        }
        return result
    }
}

func isFibonacci(_ number: Int) -> Bool {
    var penultimate = 0
    var ultimate = 1
    while(ultimate < number) {
        ultimate += penultimate
        penultimate = ultimate - penultimate
    }
    return number == penultimate || number == ultimate
}

func isEven(_ number: Int) -> Bool {
    return number % 2 == 0
}

func getKindOf(_ number: Int) -> String {
    return "\(number) \(isPrime(number) ? "es" : "no es") primo, \(isFibonacci(number) ? "es" : "no es") fibonacci y \(isEven(number) ? "es par" : "es impar")"
}

print(getKindOf(0))
print(getKindOf(1))
print(getKindOf(2))
print(getKindOf(7))
