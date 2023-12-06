/*
  Crea una función que reciba una expresión matemática (String)
      y compruebe si es correcta. Retornará true o false.
  - Para que una expresión matemática sea correcta debe poseer
    un número, una operación y otro número separados por espacios.
    Tantos números y operaciones como queramos.
  - Números positivos, negativos, enteros o decimales.
  - Operaciones soportadas: + - * / %
 
  Ejemplos:
  "5 + 6 / 7 - 4" -> true
  "5 a 6" -> false
 */

import Foundation

func verificarExpresionMatematica(_ expresion: String) -> Bool {
    let operaciones: Set<Character> = ["+", "-", "*", "/", "%"]
    let componentes = expresion.components(separatedBy: .whitespaces)
    
    if componentes.count % 2 == 0 {
        return false          // La cantidad de componentes debe ser impar (número-op- número-op-...- número)
    }
    
    for (indice, componente) in componentes.enumerated() {
        if indice % 2 == 0 {
            if let _ = Double(componente) {
                continue      // Componente es un número válido, continuar al siguiente
            } else {
                return false        // Componente no es un número válido
            }
        } else {
            if operaciones.contains(componente.first ?? Character("")) {
                continue      // Componente es una operación válida, continuar al siguiente
            } else {
                return false        // Componente no es una operación válida
            }
        }
    }
    
    return true // La expresión es correcta
}

let expresion1 = "5 + 6 / 7 - 4"
let expresion2 = "5 a 6"

print(verificarExpresionMatematica(expresion1)) // true
print(verificarExpresionMatematica(expresion2)) // false
