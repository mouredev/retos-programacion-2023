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
