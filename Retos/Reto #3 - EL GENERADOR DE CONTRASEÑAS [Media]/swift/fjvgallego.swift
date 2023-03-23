/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import Foundation


// DATA

struct Constants {
    static let numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    static let letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    static let symbols = ["!", "~", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "\"", "|", "'", "\\", "?", "<", ">", "/"]
}

func generatePassword(length: Int? = nil, useNumbers: Bool = true, useCapitalLetters: Bool = true, useSymbols: Bool = true) -> String {
    
    // Check length is in range [8, 16] or randomly generate it.
    
    var finalLength: Int
    
    if length == nil || (8...16).contains(length ?? 0) == false {
        finalLength = Int.random(in: 8...16)
    } else {
        finalLength = length!
    }
    
    // Letters are always used
    
    var usableParameters = Constants.letters
    
    var finalPassword = ""
    
    // Add any potential additional parameters
    
    if useNumbers { usableParameters += Constants.numbers }
    if useCapitalLetters { usableParameters += Constants.letters.map { $0.uppercased() } }
    if useSymbols { usableParameters += Constants.symbols }
    
    // Generate the password
    
    for _ in 0..<finalLength {
        let character = usableParameters.randomElement() ?? ""
        finalPassword.append(character)
    }
    
    return finalPassword
}

// RESULTS

print(generatePassword())
print(generatePassword(length: 8, useCapitalLetters: false))
print(generatePassword(length: 16, useNumbers: true, useCapitalLetters: true, useSymbols: false))
