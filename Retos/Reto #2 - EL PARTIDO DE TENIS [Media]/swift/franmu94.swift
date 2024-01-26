import Foundation

enum P {
    case _1
    case _2
}

func resumenJuego(puntos array:[P]){
    var p1 = 0
    var p2 = 0

    for i in array {
        switch i {
        case ._1:
            p1 += 1
        case ._2:
            p2 += 1
        }
        
        let juegoAvanzado = (p1 > 3) || (p2 > 3) ? true : false
        let diff = abs(p1 - p2)
        
        switch (diff == 0, juegoAvanzado){
        case (false, false):
            print(" \(p1 < 3  ? p1*15 : 40) - \(p2 < 3 ? p2*15 : 40 )".replacing(" 0", with: " Love").trimmingCharacters(in: .whitespaces))
        case (false, true):
            let ganador = p1 >= p2 ? "P1" : "P2"
            print( diff > 1 ? "Ha ganado el \(ganador)" : "Ventaja \(ganador)") // Break
        default:
            print("Deuce")
        }
    }
}

resumenJuego(puntos: [P._1,P._1,P._2,P._1,._2,._2,._2,._2])





