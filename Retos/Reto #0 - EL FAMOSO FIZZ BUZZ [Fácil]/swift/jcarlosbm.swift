//
//  main.swift
//  FizzBuzz
//
//  Created by Juan Carlos Bonilla on 12/15/23.
//

import Foundation

for i in 1...100{
    if i%3 == 0 && i%5 == 0 {print("fizzbuzz")}
    else if i%3 == 0 {print("fizz")}
    else if i%5 == 0 {print("buzz")}
    else {print(i)}
}

