import UIKit

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

func randomPassword(lenght: Int, uppercase: Bool, numbers: Bool, symbols: Bool) -> String {
    
    var passwordLenght = lenght
    
    let letters = "abcdefghijklmnñopqrstuvwxyz"
    //let uppercaseLetters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    let allNumbers = "1234567890"
    let allSymbols = "!·$%&/()=?¿^+Ç_:;"
    
    var password: String = ""
    
    while passwordLenght > 0 {
        
        // fff
        if uppercase == false && numbers == false && symbols == false {
            let passwordLetter: Character = letters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
          
            // ttt
        } else if uppercase == true && numbers == true && symbols == true {
            let availableCharacters = "\(letters.uppercased())\(allNumbers)\(allSymbols)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // tff
        } else if uppercase == true && numbers == false && symbols == false {
            let passwordLetter: Character = letters.uppercased().randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // ftf
        } else if uppercase == false && numbers == true && symbols == false {
            let availableCharacters = "\(letters)\(allNumbers)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // fft
        } else if uppercase == false && numbers == false && symbols == true {
            let availableCharacters = "\(letters)\(allSymbols)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // ftt
        } else if uppercase == false && numbers == true && symbols == true {
            let availableCharacters = "\(letters)\(allNumbers)\(allSymbols)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // ttf
        } else if uppercase == true && numbers == true && symbols == false {
            let availableCharacters = "\(letters.uppercased())\(allNumbers)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
            
            // tft
        } else if uppercase == true && numbers == false && symbols == true {
            let availableCharacters = "\(letters.uppercased())\(allSymbols)"
            let passwordLetter: Character = availableCharacters.randomElement()!
            password.insert(passwordLetter, at: password.endIndex)
            passwordLenght -= 1
        }
        
    }
    
    return password
    
}

// TESTS
randomPassword(lenght: 16, uppercase: false, numbers: false, symbols: false) // fff (lowercase, NO numbers, NO symbols)
randomPassword(lenght: 16, uppercase: true, numbers: true, symbols: true) // ttt (uppercase, numbers, symbols)
randomPassword(lenght: 8, uppercase: true, numbers: false, symbols: false) // tff (uppercase, NO numbers, NO symbols)
randomPassword(lenght: 8, uppercase: false, numbers: true, symbols: false) // ftf (lowercase, numbers, NO symbols)
randomPassword(lenght: 8, uppercase: false, numbers: false, symbols: true) // fft (lowercase, NO numbers, symbols)
randomPassword(lenght: 8, uppercase: false, numbers: true, symbols: true) // ftt (lowercase, numbers, symbols)
randomPassword(lenght: 8, uppercase: true, numbers: true, symbols: false) // ttf (uppercase, numbers, NO symbols)
randomPassword(lenght: 8, uppercase: true, numbers: false, symbols: true) // tft (uppercase, NO numbers, symbols)

