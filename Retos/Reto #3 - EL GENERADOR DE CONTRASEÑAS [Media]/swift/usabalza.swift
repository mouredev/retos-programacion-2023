import Foundation

func passwordGenerator(length: Int, withMayus: Bool, withNumbers: Bool, withSpecial: Bool) -> String {
    var letters = "abcdefghijklmnopqrstuvwxyz"
    let numbers = "01234567890"
    let mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let special = "!@#$%^&*+_-=~><.,:'?/"
    if withMayus {
        letters.append(mayus)
    }
    if withNumbers {
        letters.append(numbers)
    }
    if withSpecial {
        letters.append(special)
    }
    
    switch length {
    case 0..<8: return "Contraseña muy corta"
    case 8..<17: return String((0..<length).map{ _ in letters.randomElement()!})
    case 17...: return "Contraseña muy larga"
    default: return "Error inesperado"
    }
}

passwordGenerator(length: 8, withMayus: true, withNumbers: true, withSpecial: true)
