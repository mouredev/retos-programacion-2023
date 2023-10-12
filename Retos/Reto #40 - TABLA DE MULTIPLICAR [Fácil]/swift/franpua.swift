import Foundation

func multiplicationTable(num: Int) {
    
    for i in 1...10 {
        print("\(num) x \(i) = \(num * i)" )
    }
}
multiplicationTable(num: 5)