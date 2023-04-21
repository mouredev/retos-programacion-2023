//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 16/04/23.
//

import Foundation

class PasswordGenerator {
    
    var longitude: Int {
        didSet {
            longitude = max(min(longitude, 16), 8)
        }
    }
    var hasUppercase: Bool
    var hasLowercase: Bool
    var hasNumbers: Bool
    var hasSymbols: Bool
    
    init(longitude: Int = 8, hasUppercase: Bool = true, hasLowercase: Bool = true, hasNumbers: Bool = true, hasSymbols: Bool = true) {
        self.longitude = max(min(longitude, 16), 8)
        self.hasUppercase = hasUppercase
        self.hasLowercase = hasLowercase
        self.hasNumbers = hasNumbers
        self.hasSymbols = hasSymbols
    }
    
    func generate() -> String {
        let uppercased: [String] = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ").map({ String($0) })
        let lowercased: [String] = Array("abcdefghijklmnopqrstuvwxyz").map({ String($0) })
        let numbers: [String] = Array("1234567890").map({ String($0) })
        let symbols: [String] = Array("º|!#$%&/()=+¿?¡'+*{}[]-.,;:_").map({ String($0) })
        
        if !hasUppercase && !hasLowercase && !hasNumbers && !hasSymbols {
            print("You must to select at least one category")
        } else {
            var categories: [[String]] = []
            var password: String = ""
            if hasUppercase {
                categories.append(uppercased)
            }
            if hasLowercase {
                categories.append(lowercased)
            }
            if hasNumbers {
                categories.append(numbers)
            }
            if hasSymbols {
                categories.append(symbols)
            }
            while password.count < longitude {
                let catIndex: Int = Int.random(in: 0..<categories.count)
                let category: [String] = categories[catIndex]
                let index: Int = Int.random(in: 0..<category.count)
                let element: String = category[index]
                password = password + element
            }
            return password
        }
        return ""
    }
}

let generator: PasswordGenerator = PasswordGenerator()
// Longitude: 8, Uppercased, lowercased, numbers & symbols
print(generator.generate())
generator.longitude = 15
// Longitude: 15, Uppercased, lowercased, numbers & symbols
print(generator.generate())
generator.hasNumbers = false
// Longitude: 15, Uppercased, lowercased & symbols
print(generator.generate())
generator.longitude = 2 // minimum: 8
generator.hasSymbols = false
// Longitude: 8, Uppercased & lowercased
print(generator.generate())
