import Foundation

extension Date {
    var millisecondsSince1970: Int64 {
        Int64((self.timeIntervalSince1970 * 1000.0).rounded())
    }
}

private enum Operations: CaseIterable {
    case MULTIPLICATION, POW, ADDITION
}

private func generateRandomNumber() -> Int {
    var now = String(describing: Date().millisecondsSince1970)
    let nowLength = now.count
    let milli = Int(now.suffix(from: now.index(now.endIndex, offsetBy: -1)))
    var operationsResult: Int64 = 0
    
    
    (0..<nowLength).forEach { index in
        let digit = Int(now.suffix(from: now.index(now.endIndex, offsetBy: -1)))
        switch(Operations.allCases[digit! % Operations.allCases.count]) {
        case Operations.ADDITION: operationsResult += Int64(digit! + milli! + index)
        case Operations.MULTIPLICATION: operationsResult += Int64(digit! * milli! * index)
        case Operations.POW: operationsResult += Int64(pow(Double(max(digit!, max(milli!, index))), 4.0))
        }
        now = String(now.dropLast(1))
    }
    return Int(operationsResult % 100)
}

print(generateRandomNumber())