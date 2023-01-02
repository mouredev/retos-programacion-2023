//
//  juanjoseen.swift
//  UIConfig
//
//  Created by Juan Jose Elias Navarro on 26/12/22.
//

import Foundation

func fizzBuzz(_ index: Int) -> String {
    var str = ""
    if index % 3 == 0 || index % 5 == 0 {
        if index % 3 == 0 {
            str += "fizz"
        }
        if index % 5 == 0 {
            str += "buzz"
        }
        return str
    } else {
        return "\(index)"
    }
}

for i in 1...100 {
    print(fizzBuzz(i))
}
