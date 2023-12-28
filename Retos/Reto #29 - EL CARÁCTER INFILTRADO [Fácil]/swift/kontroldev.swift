/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres.
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 *
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
import Foundation

func encontrarCaracteresDiferentes(_ cadena1: String, _ cadena2: String) -> [Character] {
    var caracteresDiferentes: [Character] = []
    
    let cadena1Array = Array(cadena1)
    let cadena2Array = Array(cadena2)
    
    for i in 0..<cadena1.count {
        if cadena1Array[i] != cadena2Array[i] {
            caracteresDiferentes.append(cadena1Array[i])
        }
    }
    
    return caracteresDiferentes
}
let cadena1 = "Me llamo.Brais Moure"
let cadena2 = "Me llamo brais moure"

let caracteresDiferentes = encontrarCaracteresDiferentes(cadena1, cadena2)
print(caracteresDiferentes)     // ["B", "."]
