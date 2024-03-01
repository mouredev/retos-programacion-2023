import Foundation

let points: [Int: String] = [
    0: "Love",
    1: "15",
    2: "30",
    3: "40"
]

final class Player {
    let name: String
    var point: Int
    
    init(name: String, point: Int) {
        self.name = name
        self.point = point
    }
}

func score(l: Player, r: Player) {
    let diff = l.point - r.point
    
    switch diff {
    case 2... where l.point > 3:
        print("\(l.name) wins")
    case ..<(-1) where r.point > 3:
        print("\(r.name) wins")
    case 1 where l.point > 3:
        print("\(l.name) Advantage")
    case -1 where r.point > 3:
        print("\(r.name) Advantage")
    case 0:
        print("Deuce")
    default:
        print("\(points[l.point, default: ""]) - \(points[r.point, default: ""])")
    }
}

var p1 = Player(name: "Player 1", point: 0)
var p2 = Player(name: "Player 2", point: 0)

let set = [p1, p1, p2, p2, p1, p2, p1, p2, p1, p2, p2, p2]

set.forEach { player in
    player.point += 1
    score(l: p1, r: p2)
}