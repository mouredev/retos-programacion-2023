import Foundation

let url = "https://retosdeprogramacion.com?year=2023&challenge=0"
//var parameters: [Int] = []


func extractParameters(from url: String) -> [Int] {
    var parameters: [Int] = []
    var currentNumberString = ""
    
    for char in url {
        // Verificamos si el caracter es un dígito numérico
        if char.isNumber {
            // Si es un dígito, lo agregamos al string temporal
            currentNumberString.append(char)
        } else {
            // Si el caracter no es un dígito, verificamos si hay un número en el string temporal
            if !currentNumberString.isEmpty {
                // Si hay un número en el string temporal, lo convertimos a entero y lo agregamos al array
                if let number = Int(currentNumberString) {
                    parameters.append(number)
                }
                // Reiniciamos el string temporal para el próximo número
                currentNumberString = ""
            }
        }
    }
    
    // Verificamos si hay un número pendiente en el string temporal
    if !currentNumberString.isEmpty {
        // Si hay un número pendiente, lo convertimos a entero y lo agregamos al array
        if let number = Int(currentNumberString) {
            parameters.append(number)
        }
    }
    
    return parameters
}

let numbers = extractParameters(from: url)
print("Números encontrados en la URL:", numbers)

