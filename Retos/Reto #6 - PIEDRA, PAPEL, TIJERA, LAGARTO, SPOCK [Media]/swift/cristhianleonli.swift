import Foundation

enum GameResult {
    case player1
    case player2
}

enum Move: String {
    case rock = "🗿"
    case paper = "📄"
    case scissors = "✂️"
    case lizzard = "🦎"
    case spock = "🖖"
}

typealias Game = (Move, Move)

func checkForWinner(game: Game) -> GameResult {
    switch game {
        case (.scissors, .paper):   return .player1
        case (.paper, .scissors):   return .player2

        case (.rock, .scissors):    return .player1
        case (.scissors, .rock):    return .player2

        case (.paper, .rock):       return .player1
        case (.rock, .paper):       return .player2

        case (.rock, .lizzard):     return .player1
        case (.lizzard, .rock):     return .player2

        case (.lizzard, .spock):    return .player1
        case (.spock, .lizzard):    return .player2

        case (.spock, .scissors):   return .player1
        case (.scissors, .spock):   return .player2

        case (.scissors, .lizzard): return .player1
        case (.lizzard, .scissors): return .player2

        case (.lizzard, .paper):    return .player1
        case (.paper, .lizzard):    return .player2

        case (.paper, .spock):      return .player1
        case (.spock, .paper):      return .player2

        case (.spock, .rock):       return .player1
        case (.rock, .spock):       return .player2

        default: return .player1
    }
}

func parseInput(_ input: [(String, String)]) -> [Game] {
    return input.compactMap { (m1, m2) -> (Move, Move)? in
        guard 
            let move1 = Move(rawValue: m1), let move2 = Move(rawValue: m2),
            // ignores the same input in both sides, since that won't add any value to the score
            move1 != move2 else {
            return nil
        }

        return (move1, move2)
    }
}

func calculateTotalScore(for winners: [GameResult]) -> String {
    var p1Score = 0
    var p2Score = 0

    for winner in winners {
        switch winner {
            case .player1: p1Score += 1
            case .player2: p2Score += 1
        }
    }
    
    if p1Score > p2Score {
        return "Player 1"
    }

    if p2Score > p1Score {
        return "Player 2"
    }

    return "Tie"
}

func solve(_ input: [(String, String)]) {
    let games = parseInput(input)
    let winners = games.map(checkForWinner)
    let result = calculateTotalScore(for: winners)

    print(result)
}

let games = [
    ("🗿", "✂️"),
    ("✂️" ,"🗿"),
    ("📄", "✂️"),
    ("📄", "📄")
]

solve(games)
