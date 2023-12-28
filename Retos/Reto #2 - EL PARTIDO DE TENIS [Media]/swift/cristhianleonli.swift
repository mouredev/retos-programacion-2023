import Foundation

enum Player: String {
    case p1 = "P1"
    case p2 = "P2"
}

enum RoundStatus: CustomStringConvertible {
    case regular(Int, Int)
    case duce
    case advantage(Player)
    case win(Player)
    case none
    
    // This description eases localization, and testing
    var description: String {
        switch self {
        case let .regular(scoreP1, scoreP2):
            return [
                scoreName(for: scoreP1),
                scoreName(for: scoreP2)
            ]
                .map { String($0) }
                .joined(separator: " - ")
        case .duce:
            return "Duce"
        case let .advantage(player):
            return "Ventaja \(player.rawValue)"
        case let .win(player):
            return "Ha ganado \(player.rawValue)"
        case .none:
            return "##"
        }
    }
}

// Iterates over the point list, and simulates each round
func simulateGame(scores: [Player]) {
    var scoreP1 = 0
    var scoreP2 = 0
    
    scores.forEach { player in
        switch player {
        case .p1: scoreP1 += 1
        case .p2: scoreP2 += 1
        }
        
        let status = roundStatus(scoreP1: scoreP1, scoreP2: scoreP2)
        print(status.description)
    }
}

// Given two scores, calculates the round result
func roundStatus(scoreP1: Int, scoreP2: Int) -> RoundStatus {
    // only if both scores are exactly 40, return duce
    if scoreP1 == 3 && scoreP2 == 3 {
        return .duce
    }
    
    // when both scores are less than 40, and 40, replace names
    if scoreP1 < 4 && scoreP2 < 4 {
        return .regular(scoreP1, scoreP2)
    }
    
    // when both scores are greater than 3, can be advantage, duce, or win.
    var difference = 0
    
    if scoreP1 > scoreP2 {
        // Positive difference - P1
        difference = scoreP1 - scoreP2
    }
    
    if scoreP2 > scoreP1 {
        // Negative difference - P2
        difference = (scoreP2 - scoreP1) * -1
    }
    
    switch difference {
    case 0:     return .duce
    // for player 1
    case 1:     return .advantage(.p1)
    case 2:     return .win(.p1)
    // for player 2
    case -1:    return .advantage(.p2)
    case -2:    return .win(.p2)
    // strange result
    default:    return .none
    }
}

// aliases for scores under 4
func scoreName(for points: Int) -> String {
    switch points {
    case 0: return "Love"
    case 1: return "15"
    case 2: return "30"
    case 3: return "40"
    default: return "**"
    }
}

// avoids receiving any non-predefined player name
func sanitizeInput(_ input: [String]) throws -> [Player] {
    var result: [Player] = []
    
    for value in input {
        guard let player = Player(rawValue: value) else {
            throw NSError(domain: "SanitizationError", code: 1)
        }
        
        result.append(player)
    }
    
    return result
}

// == Main ==

let input = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

do {
    let cleanInput = try sanitizeInput(input)
    simulateGame(scores: cleanInput)
} catch {
    print("Impossible to simulate game")
}
