import UIKit

enum PasswordError: Error {
    case invalidLength
}

enum Constants {
    static let passwordMinLength: Int = 8
    static let passwordMaxLength: Int = 16
}

struct PasswordOption: OptionSet {
    let rawValue: Int
    
    static let lowercase = PasswordOption(rawValue: 1 << 0)
    static let uppercase = PasswordOption(rawValue: 1 << 1)
    static let symbols = PasswordOption(rawValue: 1 << 2)
    static let numbers = PasswordOption(rawValue: 1 << 3)
}

extension String {
    static var lowercaseLetters: String { "abcdefghijklmnopqrstuvwxyz" }
    static var uppercaseLetters: String { lowercaseLetters.uppercased() }
    static var decimalDigits: String { "0123456789" }
    static var symbols: String { "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}" }
    
    static func random(from characters: String, count: Int) -> String {
        String((0..<count).map { _ in characters.randomElement()! })
    }
}

func generatePassword(length: Int, options: PasswordOption = []) -> Result<String, PasswordError> {
    guard length >= Constants.passwordMinLength, length <= Constants.passwordMaxLength else {
        return .failure(.invalidLength)
    }
    
    var allowedChars: String = {
        // When no option was given, the algorithm assumes
        // the password will contain all options
        if options.isEmpty {
            return [
                String.lowercaseLetters,
                String.uppercaseLetters,
                String.symbols,
                String.decimalDigits
            ].joined()
        }
        
        return ""
    }()
    
    if options.contains(.lowercase) {
        allowedChars.append(.lowercaseLetters)
    }
    
    if options.contains(.uppercase) {
        allowedChars.append(.uppercaseLetters)
    }
    
    if options.contains(.symbols) {
        allowedChars.append(.symbols)
    }
    
    if options.contains(.numbers) {
        allowedChars.append(.decimalDigits)
    }
    
    return .success(
        String.random(from: allowedChars, count: length)
    )
}

func main() {
    [
        generatePassword(length: 7),
        generatePassword(length: 17),
        generatePassword(length: 16),
        generatePassword(length: 16, options: [.symbols, .uppercase, .lowercase, .numbers]),
        generatePassword(length: 8, options: .symbols),
        generatePassword(length: 8, options: .uppercase),
        generatePassword(length: 8, options: .lowercase),
        generatePassword(length: 8, options: .numbers),
    ]
        .forEach {
            print($0)
        }
}

main()
