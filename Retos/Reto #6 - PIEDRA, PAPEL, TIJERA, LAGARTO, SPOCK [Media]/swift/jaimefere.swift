import Foundation

enum Move: String {
    case ROCK = "🗿"
    case PAPER = "📄"
    case SCISSORS = "✂️"
    case ALLIGATOR = "🦎"
    case SPOCK = "🖖"
}

func playRockPaperScissorsAlligatorSpock(games: [(first: String, second: String)]) -> String {
    var playerOneWins = 0
    var playerTwoWins = 0

    games.forEach { game in
        let playerOneMove = Move.init(rawValue: game.first)
        let playerTwoMove = Move.init(rawValue: game.second)
        if(playerOneMove != playerTwoMove) {
            if((playerOneMove == Move.SCISSORS && playerTwoMove == Move.PAPER) ||
            (playerOneMove == Move.PAPER && playerTwoMove == Move.ROCK) ||
            (playerOneMove == Move.ROCK && playerTwoMove == Move.ALLIGATOR) ||
            (playerOneMove == Move.ALLIGATOR && playerTwoMove == Move.SPOCK) ||
            (playerOneMove == Move.SPOCK && playerTwoMove == Move.SCISSORS) ||
            (playerOneMove == Move.SCISSORS && playerTwoMove == Move.ALLIGATOR) ||
            (playerOneMove == Move.ALLIGATOR && playerTwoMove == Move.PAPER) ||
            (playerOneMove == Move.PAPER && playerTwoMove == Move.SPOCK) ||
            (playerOneMove == Move.SPOCK && playerTwoMove == Move.ROCK) ||
            (playerOneMove == Move.ROCK && playerTwoMove == Move.SCISSORS)) {
                playerOneWins += 1
            } else {
                playerTwoWins += 1
            }
        }
    }
    return playerOneWins == playerTwoWins ? "Tie" : playerOneWins > playerTwoWins ? "Player 1" : "Player 2"
}

print(playRockPaperScissorsAlligatorSpock(games: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))