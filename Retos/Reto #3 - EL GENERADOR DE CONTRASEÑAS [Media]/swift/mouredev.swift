func passwordGenerator(length: Int = 8,
                       capital: Bool = false,
                       numbers: Bool = false,
                       symbols: Bool = false) -> String {

    // Fuente: https://www.ascii-code.com

    var characters = Array(97...122)

    if capital {
        characters += Array(65...90)
    }

    if numbers {
        characters += Array(48...57)
    }

    if symbols {
        characters += Array(33...47) + Array(58...64) + Array(91...96)
    }

    var password = ""

    let finalLength = length < 8 ? 8 : length > 16 ? 16 : length

    while password.count < finalLength {
        if let unicode = characters.randomElement(), let scalar = UnicodeScalar(unicode) {
            password += Character(scalar).description
        }
    }

    return password
}

print(passwordGenerator())
print(passwordGenerator(length: 16))
print(passwordGenerator(length: 1))
print(passwordGenerator(length: 22))
print(passwordGenerator(length: 12, capital: true))
print(passwordGenerator(length: 12, capital: true, numbers: true))
print(passwordGenerator(length: 12, capital: true, numbers: true, symbols: true))
print(passwordGenerator(length: 12, capital: true, symbols: true))