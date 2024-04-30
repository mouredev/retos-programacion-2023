import Foundation

var P1 = [0, 1]
var P2 = [0, 1]
var pointsP1 = 0
var pointsP2 = 0
var anotationP1: Any = 0
var anotationP2: Any = 0
var deuce = "Deuce"
var flag = false


while true {
    guard var p1 = P1.randomElement() else {
        fatalError()
    }
    guard var p2 = P2.randomElement() else {
        fatalError()
    }

    while p1 == p2 {
        p1 = P1.randomElement()!
        p2 = P2.randomElement()!
    }
    
    if anotationP1 as? Int == 40 && anotationP2 as? Int == 40 {
        print(deuce)

        anotationP1 = 0
        anotationP2 = 0
        pointsP1 = 0
        pointsP2 = 0
        
        while true {
            guard var p1 = P1.randomElement() else {
                fatalError()
            }
            guard var p2 = P2.randomElement() else {
                fatalError()
            }

            while p1 == p2 {
                p1 = P1.randomElement()!
                p2 = P2.randomElement()!
            }
            
            if pointsP1 == 2 || pointsP2 == 2 {
                flag = true
                break
            }
            
            if p1 > p2 {
                pointsP1 += 1
            } else {
                pointsP2 += 1
            }
            
            if anotationP1 as? Int == 1 && anotationP2 as? Int == 1 {
                print(deuce)
            }
            
            if pointsP1 == 1 && pointsP2 == 0 {
                anotationP1 = "Ventaja"
                print("P1 = \(anotationP1) ---- P2 = \(anotationP2)")
                continue
            } else if pointsP2 == 1 && pointsP1 == 0 {
                anotationP2 = "Ventaja"
                print("P1 = \(anotationP1) ---- P2 = \(anotationP2)")
                continue
            }
            
            switch pointsP1 {
            case 0:
                anotationP1 = 0
            case 1:
                anotationP1 = 1
            case 2:
                anotationP1 = "Ha Ganado P1."
            default:
                print("No")
            }
            
            switch pointsP2 {
            case 0:
                anotationP2 = 0
            case 1:
                anotationP2 = 1
            case 2:
                anotationP2 = "Ha Ganado P2."
            default:
                print("No")
            }
            
            print("P1 = \(anotationP1) ---- P2 = \(anotationP2)")
        }
    }
    
    if flag {
        break
    }
    
    if pointsP1 == 4 || pointsP2 == 4 {
        break
    }
    
    if p1 > p2 {
        pointsP1 += 1
    } else {
        pointsP2 += 1
    }

    switch pointsP1 {
    case 0:
        anotationP1 = "Love"
    case 1:
        anotationP1 = 15
    case 2:
        anotationP1 = 30
    case 3:
        anotationP1 = 40
    case 4:
        anotationP1 = "Ha ganado P1."
    default:
        print("No")
    }

    switch pointsP2 {
    case 0:
        anotationP2 = "Love"
    case 1:
        anotationP2 = 15
    case 2:
        anotationP2 = 30
    case 3:
        anotationP2 = 40
    case 4:
        anotationP2 = "Ha ganado P2."
    default:
        print("No")
    }

    print("P1 = \(anotationP1) ---- P2 = \(anotationP2)")

}

