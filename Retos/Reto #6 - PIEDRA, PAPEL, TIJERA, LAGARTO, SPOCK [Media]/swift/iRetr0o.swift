enum Choice: String {
    case rock = "✂️"
    case paper = "📄"
    case scissors = "🗿"
    case lizard = "🦎"
    case spock = "🖖"
}

let rules: [Choice: Set<Choice>] = [
    .rock: [.scissors, .lizard],
    .paper: [.rock, .spock],
    .scissors: [.paper, .lizard],
    .lizard: [.spock, .paper],
    .spock: [.rock, .scissors]
]

func winner(_ games: [(String, String)]) -> String {
    var player1Wins = 0
    var player2Wins = 0
    
    for game in games {
        guard let choice1 = Choice(rawValue: game.0),
              let choice2 = Choice(rawValue: game.1) else {
            continue
        }
        
        if rules[choice1]?.contains(choice2) ?? false {
            player1Wins += 1
        } else if rules[choice2]?.contains(choice1) ?? false {
            player2Wins += 1
        }
    }
    
    if player1Wins == player2Wins {
        return "Tie"
    } else if player1Wins > player2Wins {
        return "Player 1"
    } else {
        return "Player 2"
    }
}

print(winner([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))