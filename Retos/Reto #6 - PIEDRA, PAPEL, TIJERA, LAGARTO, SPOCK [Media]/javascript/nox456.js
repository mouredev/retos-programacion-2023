function sheldonsGame(pairs) {
    let p1Score = 0
    let p2Score = 0

    const rules = {
        "🗿": ["📄","🖖"],
        "📄": ["✂️","🦎"],
        "✂️": ["🗿","🖖"],
        "🖖": ["📄","🦎"],
        "🦎": ["✂️","🗿"]
    }

    pairs.forEach(pair => {
        if (rules[pair[0]].includes(pair[1])) {
            p2Score++
        } else if (rules[pair[1]].includes(pair[0])) {
            p1Score++
        }
    })
    if (p1Score > p2Score) return "Player 1"
    if (p2Score > p1Score) return "Player 2"
    if (p1Score == p2Score) return "Tie"
}

const pairs = [
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"],
    ["🦎","🖖"],
    ["🖖","🗿"]
];

console.log((sheldonsGame(pairs)))
