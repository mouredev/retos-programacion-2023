import Foundation

enum Player {
    case P1
    case P2
}

func playGame(_ points: [Player]) {
    var p1Points = 0
    var p2Points = 0
    
    points.forEach { pointWinner in
        if(pointWinner == Player.P1) {
            p1Points += 1
            if(p1Points > 3) {
                if(p1Points > p2Points + 1) {
                    print("Ha ganado P1")
                } else if(p1Points == p2Points) {
                    print("Empate")
                } else {
                    print("Ventaja P1")
                }
            } else {
                print("\(p1Points == 0 ? "Nada" : String(min(40, p1Points * 15))) - \(p2Points == 0 ? "Nada" : String(min(40, p2Points * 15)))")
            }
        } else {
            p2Points += 1
            if(p2Points > 3) {
                if(p2Points > p1Points + 1) {
                    print("Ha ganado P2")
                } else if(p1Points == p2Points) {
                    print("Empate")
                } else {
                    print("Ventaja P2")
                }
            } else {
                print("\(p1Points == 0 ? "Nada" : String(min(40, p1Points * 15))) - \(p2Points == 0 ? "Nada" : String(min(40, p2Points * 15)))")
            }
        }
    }
}

playGame([Player.P1, Player.P1, Player.P1, Player.P2, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1])