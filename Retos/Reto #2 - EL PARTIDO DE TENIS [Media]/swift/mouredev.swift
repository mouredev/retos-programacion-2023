import Foundation

enum Player {
    case p1, p2
}

func tenisGame(points: [Player]) {

    let game = ["Love", "15", "30", "40"]
    var p1Points = 0
    var p2Points = 0
    var finished = false
    var error = false

    points.forEach { player in

        error = finished

        p1Points += player == .p1 ? 1 : 0
        p2Points += player == .p2 ? 1 : 0

        if p1Points >= 3 && p2Points >= 3 {
            if !finished && abs(p1Points - p2Points) <= 1 {
                print(p1Points == p2Points ? "Deuce" :
                        p1Points > p2Points ? "Ventaja P1" : "Ventaja P2")
            } else {
                finished = true
            }
        } else {
            if p1Points < 4 && p2Points < 4 {
                print("\(game[p1Points]) - \(game[p2Points])")
            } else {
                finished = true
            }
        }
    }

    print(error || !finished ? "Los puntos jugados no son correctos" :
            p1Points > p2Points ? "Ha ganado el P1" : "Ha ganado el P2")
}

tenisGame(points: [.p1, .p1, .p2, .p2, .p1, .p2, .p1, .p1])

tenisGame(points: [.p1, .p1, .p2, .p2, .p1, .p2, .p1, .p1, .p2, .p1])

tenisGame(points: [.p1, .p1, .p1, .p1, .p1, .p1])

tenisGame(points: [.p1, .p1])
