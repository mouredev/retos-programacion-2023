const P1 = "P1"
const P2 = "P2"
const sequence = [P1, P1, P2, P2, P1, P2, P1, P1]

enum Scores {
  Love = 0,
  Fifteen = 1,
  Thirty = 2,
  Forty = 3,
  Deuce = 4,
  Advantage = 5,
  Winner = 6,
}

const scores = {
  0: "Love",
  1: 15,
  2: 30,
  3: 40,
  4: "Deuce",
  5: "Advantage",
  6: "Winner",
}

class Player {
  name: string
  score: Scores = Scores.Love

  constructor(name: string) {
    this.name = name
  }
  makePoint() {
    this.score++
  }

  getScore() {
    return this.score
  }
}

class Game {
  player1: Player = new Player(P1)
  player2: Player = new Player(P2)
  scorePlayer1: Scores = Scores.Love
  scorePlayer2: Scores = Scores.Love
  isDeuce: boolean = false

  start(sequence: string[]) {
    for (const iterator of sequence) {
      if (iterator === P1) {
        this.player1.score++
      }
      if (iterator === P2) {
        this.player2.score++
      }
      if (this.changeDeuce()) {
        this.player1.score++
        this.player2.score++
        console.log("Deuce")
        this.isDeuce = true
      } else {
        const player1Score = this.player1.getScore()
        const player2Score = this.player2.getScore()
        if (this.isDeuce && player1Score === Scores.Advantage) {
          console.log(`${scores[this.player1.score]} ${this.player1.name}`)
        } else if (this.isDeuce && player2Score === Scores.Advantage) {
          console.log(`${scores[this.player2.score]} ${this.player2.name}`)
        } else {
          if (player1Score === Scores.Winner) {
            console.log(`The winner is ${this.player1.name}`)
            break
          }
          if (player2Score === Scores.Winner) {
            console.log(`The winner is ${this.player2.name}`)
            break
          }
          console.log(this.getScoreGame())
        }
      }
    }
  }
  changeDeuce() {
    return this.player1.score === Scores.Forty && this.player2.score === Scores.Forty
  }

  getScoreGame() {
    return scores[this.player1.score] + " - " + scores[this.player2.score]
  }
}

new Game().start(sequence)
