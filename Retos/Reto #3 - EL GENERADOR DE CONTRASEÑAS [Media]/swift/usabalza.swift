import Foundation

enum PasswordLength: Int {
    case short = 8
    case long = 16
}

func passwordGenerator(length: PasswordLength, withMayus: Bool, withNumbers: Bool, withSpecial: Bool) -> String {
    var letters = "abcdefghijklmnopqrstuvwxyz"
    let numbers = "01234567890"
    let mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let special = "!@#$%^&*+_-=~"
    if withMayus {
        letters.append(mayus)
    }
    if withNumbers {
        letters.append(numbers)
    }
    if withSpecial {
        letters.append(special)
    }
    return String((0..<length.rawValue).map{ _ in letters.randomElement()!})
}

passwordGenerator(length: .long, withMayus: true, withNumbers: true, withSpecial: true)
