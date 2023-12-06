//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 14/04/23.
//

import UIKit

func fizzbuzz(_ num: Int) -> String {
    if num.isMultiple(of: 3) && num.isMultiple(of: 5) {
        return "fizzbuzz"
    } else {
        if num.isMultiple(of: 3) {
            return "fizz"
        }
        if num.isMultiple(of: 5) {
            return "buzz"
        }
    }
    return String(format: "%d", num)
}

for i in 1..<100 {
    print(fizzbuzz(i))
}
