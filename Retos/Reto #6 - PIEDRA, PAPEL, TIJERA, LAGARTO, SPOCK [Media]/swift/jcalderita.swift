import Foundation

enum Option: String, CaseIterable {
    case rock = "🗿"
    case paper = "📄"
    case scissors = "✂️"
    case lizard = "🦎"
    case spock = "🖖"
}

let winsAgainst: [Option: [Option]] = [
    .rock: [.scissors, .lizard],
    .paper: [.rock, .spock],
    .scissors: [.paper, .lizard],
    .lizard: [.spock, .paper],
    .spock: [.scissors, .rock]
]

final class Player {
    let name: String
    var option: Option
    var score: Int = 0
    
    init(name: String) {
        self.name = name
        self.option = Option.allCases.randomElement()!
    }
}

func playGame(bestOf: Int, player1: Player, player2: Player) {
    guard bestOf % 2 == 1 else {
        print("It's necessary a odd number.")
        return
    }
    
    if bestOf / 2 >= bestOf - player1.score || bestOf / 2 >= bestOf - player2.score  {
        print("\(player1.score > player2.score ? player1.name: player2.name) win")
    } else {
        let playerNewGame: (Player) -> String = { player in
            let result = "\(player.name) play \(player.option.rawValue)"
            player.option = Option.allCases.randomElement()!
            return result
        }
        
        let playerWin: ((Player, Player)) -> Bool = { whoWin in
            winsAgainst[whoWin.0.option]?.contains(whoWin.1.option) ?? false
        }
        
        var win: String = "Tie"
        let win1 = playerWin((player1, player2))
        let win2 = playerWin((player2, player1))
        
        if win1 && !win2 {
            player1.score += 1
            win = "\(player1.name) win"
        } else if win2 && !win1 {
            player2.score += 1
            win = "\(player2.name) win"
        }
        print("\(playerNewGame(player1)) \(playerNewGame(player2)) \(win)")
        playGame(bestOf: bestOf, player1: player1, player2: player2)
    }
}

let p1 = Player(name:"Player 1")
let p2 = Player(name:"Player 2")

playGame(bestOf: 7, player1: p1, player2: p2)