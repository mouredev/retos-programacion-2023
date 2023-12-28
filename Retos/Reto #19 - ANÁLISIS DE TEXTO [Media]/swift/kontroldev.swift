import Foundation

let texto = "Escribir código puede resultar difícil al principio, pero con la práctica se vuelve más sencillo. En el camino, es importante aprender a analizar y comprender el código de otros programadores."

var numPalabras = 0
var longitudTotal = 0
var numOraciones = 0
var palabraMasLarga = ""

for palabra in texto.split(separator: " ") {
    let longitudPalabra = palabra.count
    numPalabras += 1
    longitudTotal += longitudPalabra
    if longitudPalabra > palabraMasLarga.count {
        palabraMasLarga = String(palabra)
    }
    if palabra.contains(".") {
        numOraciones += 1
    }
}

let longitudMedia = Double(longitudTotal) / Double(numPalabras)

print("Número total de palabras: \(numPalabras)")
print("Longitud media de las palabras: \(longitudMedia)")
print("Número de oraciones del texto: \(numOraciones)")
print("Palabra más larga: \(palabraMasLarga)")
