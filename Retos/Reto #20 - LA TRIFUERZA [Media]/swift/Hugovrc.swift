import SwiftUI

func trifuerza(n: Int) {
    var fila = n
    var filaMayor = ""
    
    for linea in 1...n {
        filaMayor = String(repeating: " ", count: n - linea + n + 1) + String(repeating: "*", count: 2 * linea - 1)
        print(filaMayor)
    }
    for linea in 1...n {
        filaMayor = String(repeating: " ", count: n - linea + 1 ) + String(repeating: "*", count: 2 * linea - 1) +
        String(repeating: " ", count: 2 * fila - 1) + String(repeating: "*", count: 2 * linea - 1)
        fila -= 1
        print(filaMayor)
    }
}

trifuerza(n:2)
trifuerza(n:5)