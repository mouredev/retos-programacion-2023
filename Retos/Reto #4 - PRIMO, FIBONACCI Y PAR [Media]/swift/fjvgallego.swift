//
//  fjvgallego.swift
//  
//
//  Created by Francisco Javier Gallego Lahera on 23/1/23.
//

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import Foundation

// DATA

func checkNumberProps(for number: Int) {
    var checkText = "\(number) es"

    let isPrimeText = numberIsPrime(number) ? "primo" : "no primo"
    checkText.append(" \(isPrimeText)")
    
    let isFibonacciText = numberIsFibonacci(number) ? "fibonacci" : "no es fibonacci"
    checkText.append(", \(isFibonacciText)")
    
    let isEvenText = numberIsEven(number) ? "y par" : "e impar"
    checkText.append(" \(isEvenText)")
    
    print(checkText)
}

func numberIsPrime(_ number: Int) -> Bool {
    
    guard number > 1 else {
        return false
    }
    
    for index in 2..<number {
        if number.isMultiple(of: index) {
            return false
        }
    }
    
    return true
}


func numberIsFibonacci(_ number: Int) -> Bool {
    var numberA = 0
    var numberB = 1

    while numberA < number || numberB < number {
        let fib = numberA + numberB
        numberA = numberB
        numberB = fib
        
        if numberA == number || numberB == number {
            return true
        }
    }
    
    return false
}

func numberIsEven(_ number: Int) -> Bool {
    number % 2 == 0
}

// RESULT

checkNumberProps(for: 2)
checkNumberProps(for: 7)
checkNumberProps(for: 1)
checkNumberProps(for: 22)
checkNumberProps(for: 144)
