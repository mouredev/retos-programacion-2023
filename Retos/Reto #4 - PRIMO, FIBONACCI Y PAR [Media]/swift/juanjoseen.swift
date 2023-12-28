//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 19/04/23.
//

import Foundation

extension Int {
    func isPrime() -> Bool {
        if self == 1 || self == 2 || self == 3 {
            return true
        }
        let sqr: Int = Int(sqrt(Double(self)))
        for i in 2...sqr {
            if self % i == 0 {
                return false
            }
        }
        return true
    }
    
    func isFibonacci() -> Bool {
        if self == 1 || self == 2 {
            return true
        }
        var a = 1
        var b = 2
        var sum = a + b
        while sum <= self {
            if sum == self {
                return true
            }
            a = b
            b = sum
            sum = a + b
        }
        
        return false
    }
    
    func isEven() -> Bool {
        return self % 2 == 0
    }
}

func analize(_ num: Int) {
    var results: [String] = []
    if num.isPrime() {
        results.append("is prime")
    }
    if num.isFibonacci() {
        results.append("is fibonacci")
    }
    results.append(num.isEven() ? "is even" : "is odd")
    print("The number \(num): ",results.joined(separator: ", "))
}

analize(2)
analize(5)
analize(8)
analize(11)
