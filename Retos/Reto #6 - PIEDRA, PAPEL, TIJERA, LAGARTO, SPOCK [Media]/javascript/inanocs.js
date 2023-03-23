const GameOptions = {
  ROCK: 'rock',
  PAPER: 'paper',
  SCISSORS: 'scissors',
  LIZARD: 'lizard',
  SPOCK: 'spock',
}

const GameResults = {
  PLAYER1: 'Player 1',
  PLAYER2: 'Player 2',
  TIE: 'Tie',
}

class Game {
  constructor(player1, player2) {
    const availableOptions = Object.values(GameOptions)
    if (
      !availableOptions.includes(player1) ||
      !availableOptions.includes(player2)
    )
      throw new Error(
        `Ilegal game option. Available options: ${availableOptions.toString()}`
      )
    this.player1 = player1
    this.player2 = player2
    this.GAME_RULES = {
      [GameOptions.ROCK]: [GameOptions.SCISSORS, GameOptions.LIZARD],
      [GameOptions.PAPER]: [GameOptions.ROCK, GameOptions.SPOCK],
      [GameOptions.SCISSORS]: [GameOptions.PAPER, GameOptions.LIZARD],
      [GameOptions.LIZARD]: [GameOptions.PAPER, GameOptions.SPOCK],
      [GameOptions.SPOCK]: [GameOptions.SCISSORS, GameOptions.ROCK],
    }
  }

  getWinner() {
    if (this.isTie()) return GameResults.TIE
    return this.GAME_RULES[this.player1].includes(this.player2)
      ? GameResults.PLAYER1
      : GameResults.PLAYER2
  }
  isTie() {
    return this.player1 === this.player2
  }
}

const getMaxWinnerGames = (results = []) => {
  const initial = {
    [GameResults.PLAYER1]: 0,
    [GameResults.PLAYER2]: 0,
  }
  const playerPoints = results.reduce((playerPoints, match) => {
    const winner = match?.getWinner()
    if (playerPoints[winner] === undefined) {
      playerPoints[GameResults.PLAYER1] += 1
      playerPoints[GameResults.PLAYER2] += 1
    } else {
      playerPoints[winner] += 1
    }
    return playerPoints
  }, initial)

  const maxCount = Math.max(...Object.values(playerPoints))
  const mostFrequent = Object.keys(playerPoints).filter(
    (key) => playerPoints[key] === maxCount
  )
  return mostFrequent.length === 1 ? mostFrequent.pop() : GameResults.TIE
}

//Test cases
const testSamples = [
  {
    testName: 'Player 1 should win',
    input: [
      new Game(GameOptions.LIZARD, GameOptions.SPOCK),
      new Game(GameOptions.SPOCK, GameOptions.LIZARD),
      new Game(GameOptions.PAPER, GameOptions.ROCK),
    ],
    expectedOutput: GameResults.PLAYER1,
  },
  {
    testName: 'Player 2 should win',
    input: [
      new Game(GameOptions.LIZARD, GameOptions.SPOCK),
      new Game(GameOptions.SPOCK, GameOptions.LIZARD),
      new Game(GameOptions.LIZARD, GameOptions.SCISSORS),
    ],
    expectedOutput: GameResults.PLAYER2,
  },
  {
    testName: 'Should be a Tie',
    input: [
      new Game(GameOptions.LIZARD, GameOptions.SPOCK),
      new Game(GameOptions.SPOCK, GameOptions.LIZARD),
      new Game(GameOptions.PAPER, GameOptions.PAPER),
    ],
    expectedOutput: GameResults.TIE,
  },
]

const runTests = () => {
  const passedTests = testSamples.filter((sample, idx) => {
    const { testName, input, expectedOutput } = sample
    const mappedInput = input.map((game) => game.getWinner())
    const printOutput = getMaxWinnerGames(input)
    const areEquals = expectedOutput === printOutput

    const LOG_TEST_NUMBER = `Test ${idx + 1}: ${testName}`
    const LOG_TEST_RESULT = areEquals ? 'PASSED' : 'FAILED'
    console.log(
      `${LOG_TEST_NUMBER}: ${LOG_TEST_RESULT}\n\tInput: ${mappedInput}\n\tExpected: ${expectedOutput}\n\tGot: ${printOutput}\n`
    )

    return areEquals
  }).length

  console.log(`Tests ${passedTests} of ${testSamples.length} passed`)
}

runTests()
