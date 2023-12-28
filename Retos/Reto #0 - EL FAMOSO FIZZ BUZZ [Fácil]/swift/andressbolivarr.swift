//
//  andressbolivarr.swift
//  
//
//  Created by Andres Bolivar on 17/1/23.
//

import Foundation

func FizzbBuzz(){
    for number in 1...100{
        switch(number % 3 == 0, number % 5 == 0){
        case(true,false) :
            print("Fizz")
        case(false, true) :
            print("Buzz")
        case(true, true) :
            print("FizzBuzz")
        case (false, false):
            print(number)
        }
    }
}

FizzbBuzz()
