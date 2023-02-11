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
    function updateScore(score, game) {
        const [player1, player2] = game
        const player1Wins = wins[player1].includes(player2)
        const player2Wins = wins[player2].includes(player1)

        if (player1Wins && !player2Wins) {
            score[0] += 1
        }
        if (player2Wins && !player1Wins) {
            score[1] += 1
        }

        return score
    }
    const [player1Score, player2Score] = games.reduce(updateScore, [0, 0])
    if (player1Score > player2Score) {
        return "Player 1"
    }
    if (player2Score > player1Score) {
        return "Player 2"
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
