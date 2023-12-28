import Foundation

func multiplicationTable(_ number: Int) {
    
    for n in 0...10 {
        print("\(number) x \(n) = \(n * number)")
    }
}

multiplicationTable(5)
