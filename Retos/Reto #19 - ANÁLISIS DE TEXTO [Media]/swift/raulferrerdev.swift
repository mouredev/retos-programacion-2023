import Foundation

func analisisDeTexto(_ texto: String) {
    var numeroTotalDePalabras = 0
    var numeroTotalDeLetras = 0
    var numeroTotalDeOraciones = 0
    var palabraMasLarga = ""
    
    var palabraRevisada = ""
    
    // Bucle para cada caracter del texto
    for caracter in texto {
        // Comprobamos si se trata de una letra
        // Se añade el caracter para ir generando la palabra
        // Se añade al número todal de caracteres (para el calculo de la media)
        if caracter.isLetter {
            palabraRevisada.append(caracter)
            numeroTotalDeLetras += 1
        }
        // Comprobamos si es una oración completa comparando el caracter con el de un punto final de oración.
        // En ese caso, aumentamos en 1 el número de oraciones y comparamos la palabra que se acaba de reisar con la más larga hasta el momento
        else if caracter == "." {
            if !palabraRevisada.isEmpty {
                numeroTotalDePalabras += 1
                palabraMasLarga = palabraRevisada.count > palabraMasLarga.count ? palabraRevisada : palabraMasLarga
                palabraRevisada = ""
            }
            
            numeroTotalDeOraciones += 1
        } else { // Si no es una letra o un '.', será otro caracter separador de palabras: espacio, punto y coma...
            if !palabraRevisada.isEmpty {
                numeroTotalDePalabras += 1
                palabraMasLarga = palabraRevisada.count > palabraMasLarga.count ? palabraRevisada : palabraMasLarga
                palabraRevisada = ""
            }
        }
    }
    
    // Se puede dar el caso de que la última frase no acabe en '.' y por lo tanto no la hubiéramos contabilizado.
    if !palabraRevisada.isEmpty {
        numeroTotalDePalabras += 1
        numeroTotalDeOraciones += 1
        palabraMasLarga = palabraRevisada.count > palabraMasLarga.count ? palabraRevisada : palabraMasLarga
    }
    
    let longitudMedia = Double(numeroTotalDeLetras) / Double(numeroTotalDePalabras)
    
    print("Número total de palabras: \(numeroTotalDePalabras)")
    print("Longitud media de las palabras: \(longitudMedia)")
    print("Número de oraciones del texto: \(numeroTotalDeOraciones)")
    print("Palabra más larga: \(palabraMasLarga)")
}

var texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

analisisDeTexto(texto)


/* Versión sin bucle
func analizarTextoSinBucle(_ texto: String) {
    let palabras = texto.split { !$0.isLetter }
    let numeroTotalDePalabras = palabras.count
    let numeroTotalDeLetras = palabras.reduce(0) { $0 + $1.count }
    let longitudMedia = Double(numeroTotalDeLetras) / Double(numeroTotalDePalabras)
    let numeroTotalDeOraciones = texto.split(separator: ".").count
    let palabraMasLarga = palabras.max(by: { $0.count < $1.count }) ?? ""
    
    print("Número total de palabras: \(numeroTotalDePalabras)")
    print("Longitud media de las palabras: \(longitudMedia)")
    print("Número de oraciones del texto: \(numeroTotalDeOraciones)")
    print("Palabra más larga: \(palabraMasLarga)")
}
*/
