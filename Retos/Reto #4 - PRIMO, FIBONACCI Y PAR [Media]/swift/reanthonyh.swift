import Foundation

evaluateNumber(3)
evaluateNumber(7)
evaluateNumber(11)
evaluateNumber(13)
evaluateNumber(34)

func evaluateNumber(_ number: Int) {
  let isPrime = number.isPrime() ? "es primo" : "no es primo"
  let isFibonacci = number.isFibonacci() ? "es fibonacci" : "no es fibonacci"
  let isEven = number.isEven() ? "es par" : "es impar"
  print("\(number) \(isPrime), \(isFibonacci) y \(isEven)")
}

extension Int {
  func isPrime() -> Bool {
    if self <= 1 {
      return false
    }

    let limit = Int(Double(self).squareRoot())
    if limit > 2 {
      for index in 2..<limit {
        if self % index == 0 {
          return false
        }
      }
    }
    return true
  }

  func isFibonacci() -> Bool {
    if self == 0 || self == 1 || self == 2 {
      return true
    }
    var fibonacciList: [Int] = [0, 1]
    for i in 2..<15 {
      let number = fibonacciList[i - 2] + fibonacciList[i - 1]

      if self == number { return true }
      if self < number { return false }

      fibonacciList.append(number)
    }
    print("fibo: \(fibonacciList)")
    return false
  }

  func isEven() -> Bool {
    return self.isMultiple(of: 2)

  }
}
