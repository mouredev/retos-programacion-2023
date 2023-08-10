/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
import Foundation

func excelColumnNumber(_ column: String) -> Int {
    var result = 0
    for char in column {
        let value = Int(char.unicodeScalars.first!.value) - Int(UnicodeScalar("A").value) + 1
        result = result * 26 + value
    }
    return result
}

print("Ingrese el nombre de la columna:")
if let columnName = readLine() {
    let columnNumber = excelColumnNumber(columnName)
    print("El número de la columna es: \(columnNumber)")
}

