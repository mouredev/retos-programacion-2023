import Foundation

func passwordGenerator(length: Int = 8, capital: Bool = false, number: Bool = false, symbol: Bool = false) -> String {
    var password = ""
    var finalLength: UInt8
    var asciiCodes: [UInt8] = Array(97...122)

    if capital {
        asciiCodes += Array(65...90)
    }

    if number {
        asciiCodes += Array(48...57)
    }

    if symbol {
        asciiCodes += Array(33...47)
    }

    if length < 8 {
        finalLength = 8
    } else if length > 16 {
        finalLength = 16
    } else {
        finalLength = UInt8(length)
    }

    for _ in 0..<finalLength {
        password += UnicodeScalar(asciiCodes.randomElement()!).description
    }

    return password
}

print(passwordGenerator(length: 4))
print(passwordGenerator(length: 8, capital: true))
print(passwordGenerator(length: 16, capital: true, number: true))
print(passwordGenerator(length: 20, capital: true, number: true, symbol: true))