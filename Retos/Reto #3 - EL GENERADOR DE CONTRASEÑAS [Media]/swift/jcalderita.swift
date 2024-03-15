import Foundation

func generatePassword() -> String {
    let characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}|:<>?"
    let length = Int.random(in: 8 ... 16)
    
    return String((1 ... length).compactMap { _ in
        characters.randomElement()
        })
    }
    
print(generatePassword())
print(generatePassword())
print(generatePassword())
print(generatePassword())