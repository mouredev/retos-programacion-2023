import Foundation

enum Player {
    case p1, p2
}

func tennisGame(points: [Player]) {
    let game = ["Love", "15", "30", "40"]
    var score = (p1Points: 0, p2Points: 0)
    for winner in points {
        score.p1Points += winner == .p1 ? 1 : 0
        score.p2Points += winner == .p2 ? 1 : 0

        if score.p1Points == 4 && score.p2Points == 4 {
            score.p1Points -= 1
            score.p2Points -= 1
        }

        switch score {
            case (3, 3):
                print("Deuce")
            case (4, 3):
                print("Ventaja P1")
            case (3, 4):
                print("Ventaja P2")
            case (5, 3), (4, _):
                print("Ha ganado el P1")
                return
            case (3, 5), (_, 4):
                print("Ha ganado el P2")
                return
            default:
                print("\(game[score.p1Points]) - \(game[score.p2Points])")
        }
    }
    print("Faltan puntos para definir un ganador")
}

tennisGame(points: [.p1, .p1, .p2, .p2, .p1, .p2, .p1, .p1])
print("\n")
tennisGame(points: [.p1, .p2, .p2, .p1, .p1, .p1, .p2, .p2])
print("\n")
tennisGame(points: [.p1, .p1, .p2, .p2, .p1, .p2, .p1, .p2, .p2, .p2])
print("\n")
tennisGame(points: [.p1, .p1, .p2])