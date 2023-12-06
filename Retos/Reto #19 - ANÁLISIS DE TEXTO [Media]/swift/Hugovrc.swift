import Foundation

var palabra: [String]
var oraciones: [String]
var palabraLarga = ""
var longitudMedia = 0
let texto = "Swift es un lenguaje rápido y eficiente que proporciona información en tiempo real y puede incorporarse fácilmente al código de Objective-C existente. Así, los desarrolladores no sólo pueden programar de una forma más segura y confiable, sino también ahorrar tiempo y enriquecer la experiencia con las apps."

palabra = texto.components(separatedBy: " ")
oraciones = texto.components(separatedBy: ". ")

for palabraLa in palabra {
    if palabraLa.count > palabraLarga.count {
        palabraLarga = palabraLa
    }
}

longitudMedia = texto.count / palabra.count
print("total de palabras: \(palabra.count)")
print("Longitud media de las palabras: \(longitudMedia)")
print("Numero de oraciones del texto: \(oraciones.count)")
print("palabra mas larga: \(palabraLarga)")