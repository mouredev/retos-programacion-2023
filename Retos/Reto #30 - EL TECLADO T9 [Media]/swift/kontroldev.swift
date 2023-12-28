/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
import Foundation

func t9ToLetters(_ input: String) -> String {
    let t9Mapping: [Character: String] = [
        "2": "ABC", "3": "DEF", "4": "GHI",
        "5": "JKL", "6": "MNO", "7": "PQRS",
        "8": "TUV", "9": "WXYZ"
    ]
    
    var result = ""
    var currentDigits = [Character]()
    
    for char in input {
        if char.isNumber {
            currentDigits.append(char)
        } else if char == "-" {
            if let digit = currentDigits.first, let letters = t9Mapping[digit] {
                result += String(letters[letters.index(letters.startIndex, offsetBy: currentDigits.count - 1)])
            }
            currentDigits.removeAll()
        }
    }
    
    if let digit = currentDigits.first, let letters = t9Mapping[digit] {
        result += String(letters[letters.index(letters.startIndex, offsetBy: currentDigits.count - 1)])
    }
    
    return result
}


let input = "6-666-88-777-33-3-33-888"
let output = t9ToLetters(input)
print(output) 
