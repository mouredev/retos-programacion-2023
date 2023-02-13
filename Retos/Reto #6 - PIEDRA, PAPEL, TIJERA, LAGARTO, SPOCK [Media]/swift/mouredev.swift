import Foundation

enum Game {
    case rock, paper, scissors, lizard, spock
}

func rockPaperScissorLizardSpock(games: [(playerOneGame: Game, playerTwoGame: Game)]) -> String {
    
    let rules: [Game: [Game]] = [.rock: [.scissors, .lizard],
                                 .paper: [.rock, .spock],
                                 .scissors: [.paper, .lizard],
                                 .lizard: [.spock, .paper],
                                 .spock: [.rock, .scissors]]

    var playerOne = 0
    var playerTwo = 0

    for game in games {
        if game.playerOneGame != game.playerTwoGame {
            if let winGame = rules[game.playerOneGame], winGame.contains(game.playerTwoGame) {
                playerOne += 1
            } else {
                playerTwo += 1
            }
        }
    }
    
    return playerOne == playerTwo ? "Tie" : playerOne > playerTwo ? "Player 1" : "Player 2"
}


print(rockPaperScissorLizardSpock(games: [(playerOneGame: .rock, playerTwoGame: .rock)]))
print(rockPaperScissorLizardSpock(games: [(playerOneGame: .rock, playerTwoGame: .scissors)]))
print(rockPaperScissorLizardSpock(games: [(playerOneGame: .scissors, playerTwoGame: .rock)]))
print(rockPaperScissorLizardSpock(games: [(playerOneGame: .rock, playerTwoGame: .rock), (playerOneGame: .rock, playerTwoGame: .rock), (playerOneGame: .rock, playerTwoGame: .rock), (playerOneGame: .rock, playerTwoGame: .rock)]))
print(rockPaperScissorLizardSpock(games: [(playerOneGame: .spock, playerTwoGame: .rock), (playerOneGame: .scissors, playerTwoGame: .paper), (playerOneGame: .rock, playerTwoGame: .rock), (playerOneGame: .lizard, playerTwoGame: .spock)]))