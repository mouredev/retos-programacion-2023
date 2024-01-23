/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

import Foundation
// solucion utilizando ternary operator
func fizzbuzz() {
    var str = ""
    for i in 1...100 {
        str += i.isMultiple(of: 3) ? "Fizz" : ""
        str += i.isMultiple(of: 5) ? "Buzz" : ""
        str += str.count == 0 ? "\(i)" : ""
        print(str)
        str = ""
    }
    
}


