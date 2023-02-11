const PLAYER_ONE = "Player 1"
const PLAYER_TWO = "Player 2"
const ROCK = "🗿"
const PAPER = "📄"
const SCISSORS = "✂️"
const LIZARD = "🦎"
const SPOCK = "🖖"

const wins = {
    [ROCK]: [SCISSORS, LIZARD],
    [PAPER]: [ROCK, SPOCK],
    [SCISSORS]: [PAPER, LIZARD],
    [LIZARD]: [PAPER, SPOCK],
    [SPOCK]: [ROCK, SCISSORS],
}

function getResult(games) {
    function setScore(score, game) {
        const [player1, player2] = game
        const player1Wins = wins[player1].includes(player2)
        const player2Wins = wins[player2].includes(player1)

        if (player1Wins && !player2Wins) {
            score[PLAYER_ONE] += 1
        }
        if (player2Wins && !player1Wins) {
            score[PLAYER_TWO] += 1
        }

        return score
    }
    const { [PLAYER_ONE]: player1Score, [PLAYER_TWO]: player2Score } =
        games.reduce(setScore, {
            [PLAYER_ONE]: 0,
            [PLAYER_TWO]: 0,
        })
    if (player1Score > player2Score) {
        return PLAYER_ONE
    }
    if (player2Score > player1Score) {
        return PLAYER_TWO
    }
    return "Tie"
}

console.table({
    winsPlayer2: getResult([
        ["🗿", "✂️"],
        ["✂️", "🗿"],
        ["🖖", "🦎"],
    ]), // Should print "Player 2"
    winsPlayer1: getResult([
        ["🦎", "📄"],
        ["🗿", "🖖"],
        ["🦎", "🖖"],
        ["🗿", "✂️"],
        ["🗿", "🗿"],
        ["📄", "🗿"],
        ["✂️", "🗿"],
        ["📄", "✂️"],
    ]), // Should print "Player 1"
    tie: getResult([
        ["🖖", "✂️"],
        ["✂️", "🗿"],
        ["🖖", "🖖"],
        ["✂️", "📄"],
        ["🗿", "📄"],
    ]), // Should print "Tie"
})
