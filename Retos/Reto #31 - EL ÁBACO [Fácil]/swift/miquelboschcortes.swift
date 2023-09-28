//
//  miquelboschcortes.swift
//  
//
//  Created by Miguel Bosch Cortés on 02/08/2023.
//

import Foundation

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
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

let firstNumber =  [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

func abaco(number: [String]) -> String {
    
    let splited = Int(number
        .compactMap { String($0.prefix(upTo: $0.firstIndex(of: "-")! )).count }
        .reduce("") { $0 + "\($1)" })
    //.reduce(0) { $0 + }
    
    let numberFormatter = NumberFormatter()
    numberFormatter.numberStyle = .decimal
    
    if
        let splitedTrue = splited,
        let finalNumber = numberFormatter.string(from: NSNumber(value: splitedTrue))
    {
        return finalNumber
    }
    
    return ""
    
}
