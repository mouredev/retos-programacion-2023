import Foundation

enum Player {
    case p1
    case p2
}

var pointDict: [Int:String] = [
    0:"Love",
    1:"15",
    2:"30",
    3:"40"
]

func tennisSet(_ points: [Player]) {
    var p1points: Int = 0
    var p2points: Int = 0
    
    for i in points {
        switch i {
        case .p1:
            p1points += 1
        case .p2:
            p2points += 1
        }
        
        if p1points == p2points && p1points >= 3 {
            print("Deuce")
        } else if p1points > 3 || p2points > 3 {
            switch p1points > p2points {
            case true:
                print(abs(p1points - p2points) >= 2 ? "Ha ganado el P1" : "Ventaja P1")
            case false:
                print(abs(p1points - p2points) >= 2 ? "Ha ganado el P2" : "Ventaja P2")
            }
        } else {
            print("\(pointDict[p1points] ?? "Default") - \(pointDict[p2points] ?? "Default")")
        }
        
    }
    
}

tennisSet([.p1, .p1, .p2, .p2, .p1, .p2, .p1, .p2, .p2, .p1, .p1, .p1])
