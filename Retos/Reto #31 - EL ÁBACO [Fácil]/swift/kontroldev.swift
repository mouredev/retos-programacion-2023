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
/*
 * Esta función es capaz de leer el número representado por el ábaco.
 *
 * El ábaco se representa por un array con 7 elementos.
 * Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 * para las cuentas y una secuencia de "---" para el alambre.
 * El primer elemento del array representa los millones, y el último las unidades.
 * El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */

import Foundation

func readNumberFromAbacus(_ abacus: [String]) -> String {
    // Variable para almacenar el número resultante
    var number = 0
    
    // Valor posicional para cada elemento del ábaco
    let positionalValues = [1000000, 100000, 10000, 1000, 100, 10, 1]
    
    // Recorremos el array en orden inverso
    for i in (0..<abacus.count).reversed() {
        let element = abacus[i]
        
        // Buscamos el índice del alambre en el elemento actual
        if let index = element.firstIndex(of: "-") {
            // Obtenemos las cuentas a la izquierda del alambre
            let countString = String(element.prefix(upTo: index))
            // Interpretamos el número representado por las cuentas
            let countValue = countString.count
            // Multiplicamos el valor posicional por el número representado
            number += countValue * positionalValues[i]
        }
    }
    
    // Devolvemos el número resultante en formato de cadena con puntos como separadores de miles
    let numberFormatter = NumberFormatter()
    numberFormatter.numberStyle = .decimal
    return numberFormatter.string(from: NSNumber(value: number)) ?? ""
}

// Ejemplo de uso
let abacusArray = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

let result = readNumberFromAbacus(abacusArray)
print(result) // Output: "1,302,790"
