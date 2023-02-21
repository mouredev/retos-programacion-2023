import Foundation

enum Jugada: Int {
    case PIEDRA
    case PAPEL
    case TIJERAS
    case LAGARTO
    case SPOCK
}

func PiedraPapelTijerasLagartoSpock(juegos: [(Jugada, Jugada)]) -> String {
    var p1Points = 0
    var p2Points = 0
    let ganador: [Jugada: [Jugada]] = [
    Jugada.PIEDRA: [Jugada.TIJERAS, Jugada.LAGARTO],
    Jugada.PAPEL: [Jugada.PIEDRA, Jugada.SPOCK],
    Jugada.TIJERAS: [Jugada.PAPEL, Jugada.LAGARTO],
    Jugada.LAGARTO: [Jugada.PAPEL, Jugada.SPOCK],
    Jugada.SPOCK: [Jugada.TIJERAS, Jugada.PIEDRA]
    ]

    for juego in juegos {
        let jugador1 = juego.0
        let jugador2 = juego.1
        if jugador1 == jugador2 {
            p1Points += 1
            p2Points += 1
        } else if ganador[jugador1]?.contains(jugador2) == true {
            p1Points += 1
        } else {
            p2Points += 1
        }
    }

    if p1Points == p2Points {
        return "Empate a \(p1Points) puntos"
    } else if p1Points > p2Points {
        return "Gana el jugador 1 por \(p1Points) a \(p2Points) puntos"
    } else {
        return "Gana el jugador 2 por \(p2Points) a \(p1Points) puntos"
    }

}

print(PiedraPapelTijerasLagartoSpock(juegos: [
    (Jugada.PIEDRA, Jugada.TIJERAS),
    (Jugada.PIEDRA, Jugada.PAPEL),
    (Jugada.LAGARTO, Jugada.SPOCK)
]))

print(PiedraPapelTijerasLagartoSpock(juegos: [
    (Jugada.TIJERAS, Jugada.TIJERAS),
    (Jugada.PIEDRA, Jugada.PAPEL),
    (Jugada.LAGARTO, Jugada.SPOCK),
    (Jugada.PIEDRA, Jugada.PAPEL),
    (Jugada.SPOCK, Jugada.PAPEL),
    (Jugada.LAGARTO, Jugada.LAGARTO),
    (Jugada.SPOCK, Jugada.LAGARTO)
]))

