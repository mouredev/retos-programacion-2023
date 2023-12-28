import SwiftUI

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

func generatePassword(longLength: Bool = true, withUpperLetters: Bool = true, withNumbers: Bool = true, withSymbols: Bool = true) -> String {
    let letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    let numbers = "0123456789"
    let symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
    let eligibleCharacters = "\(withUpperLetters ? letters : "")\(withNumbers ? numbers : "")\(withSymbols ? symbols : "")"
    var result = ""
    if(!eligibleCharacters.isEmpty) {
        (0..<(longLength ? 16 : 8)).forEach { _ in
            result += String(eligibleCharacters[eligibleCharacters.index(eligibleCharacters.startIndex, offsetBy: Int.random(in: 0..<eligibleCharacters.count))])
        }
    }
    return result
}

print(generatePassword(longLength: true, withUpperLetters: true, withNumbers:true, withSymbols: true))
print(generatePassword(longLength: false, withUpperLetters: true, withNumbers:false, withSymbols: false))
print(generatePassword(longLength: false, withUpperLetters: false, withNumbers:true, withSymbols: false))
print(generatePassword(longLength: false, withUpperLetters: false, withNumbers:false, withSymbols: true))
print(generatePassword(longLength: true, withUpperLetters: false, withNumbers:false, withSymbols: false))
