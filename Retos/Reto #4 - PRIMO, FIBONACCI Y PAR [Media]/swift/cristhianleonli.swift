import Foundation

extension Int {
    var isEven: Bool {
        self % 2 == 0
    }

    var isFibonacci: Bool {
        // 5 * n^2 + 4 || 5 * n^2 - 4
        isPerfectSquare(5 * self * self + 4) || isPerfectSquare(5 * self * self - 4)
    }

    var isPrime: Bool {
        if self < 2 {
            return false
        }
        
        for i in 2..<self {
            if self % i  == 0 {
                return false
            }
        }
        
        return true
    }
    
    private func isPerfectSquare(_ number: Int) -> Bool {
        let result = Int(sqrt(Double(number)))
        return result * result == number
    }
}

func solve(for number: Int) {
    let primeText = number.isPrime ? "Prime" : "no Prime"
    let fiboText = number.isFibonacci ? "Fibonacci" : "no Fibonacci"
    let evenText = number.isEven ? "and Even" : "and Odd"
    
    let description = [
        primeText,
        fiboText,
        evenText
    ].joined(separator: ", ")
    
    let formattedString = String(format: "%d is %@", number, description)
    print(formattedString)
}

solve(for: 2) // Primo, Fibonacci, Par
solve(for: 7) // Primo, No Fibonacci, Impar
