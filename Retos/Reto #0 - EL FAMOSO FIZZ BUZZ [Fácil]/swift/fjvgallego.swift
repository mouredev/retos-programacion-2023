//
//  fjvgallego.swift
//  
//
//  Created by Francisco Javier Gallego Lahera on 27/12/22.
//

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

import Foundation

// RESULTS

fizzbuzz()

// DATA

struct Constants {
    static let minNumber = 1
    static let maxNumber = 100
}

func fizzbuzz() {
    
    for i in Constants.minNumber...Constants.maxNumber {
        let isMultipleOfThree = i.isMultiple(of: 3)
        let isMultipleOfFive = i.isMultiple(of: 5)
        
        if isMultipleOfThree && isMultipleOfFive {
            print("fizzbuzz")
        } else if isMultipleOfThree {
            print("fizz")
        } else if isMultipleOfFive {
            print("buzz")
        } else {
            print(i)
        }
    }
}
