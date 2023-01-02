//
//  3rnestocs-fizzBuzz-solution.swift
//  PlatziTweets
//
//  Created by Ernesto Jose Contreras Lopez on 2/1/23.
//

import Foundation

func fizzBuzz() {

    for n in 1...100 {
        if n % 3 == 0 {
            print("fizz\n")
        } else if n % 5 == 0 {
            print("buzz\n")
        } else if n % 3 == 0 && n % 5 == 0 {
            print("fizzbuzz\n")
        } else {
            print("\(n)\n")
        }
    }
}

fizzBuzz()
