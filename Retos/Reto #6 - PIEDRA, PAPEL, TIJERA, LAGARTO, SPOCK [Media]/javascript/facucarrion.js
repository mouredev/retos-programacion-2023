const OPTIONS = ['🪨', '📃', '✂️', '🦎', '🖖🏻']

const RANDOM_ENTRIES = Array.from({ length: 100 }, () => [
  OPTIONS[Math.floor(Math.random() * OPTIONS.length)],
  OPTIONS[Math.floor(Math.random() * OPTIONS.length)],
])

const RESULTS = {
  '🪨': ['✂️', '🦎'],
  '📃': ['🪨', '🖖🏻'],
  '✂️': ['📃', '🦎'],
  '🦎': ['📃', '🖖🏻'],
  '🖖🏻': ['✂️', '🪨'],
}

const rockPaperScissorsLizardSpock = (arr) => {
  let results = {
    player1: 0,
    player2: 0,
    tie: 0,
  }

  arr.forEach(([player1, player2]) => {
    if (player1 === player2) results.tie++
    else if (player1 === '🪨') results[RESULTS[player1].includes(player2) ? 'player1' : 'player2'] += 1
    else if (player1 === '📃') results[RESULTS[player1].includes(player2) ? 'player1' : 'player2'] += 1
    else if (player1 === '✂️') results[RESULTS[player1].includes(player2) ? 'player1' : 'player2'] += 1
    else if (player1 === '🦎') results[RESULTS[player1].includes(player2) ? 'player1' : 'player2'] += 1
    else if (player1 === '🖖🏻') results[RESULTS[player1].includes(player2) ? 'player1' : 'player2'] += 1
    else return
  })

  console.log(results);
  if (results.player1 === results.player2 && (results.player1 + results.player2) > results.tie) return 'Tie'
  else return results.player1 > results.player2 ? 'Player 1' : 'Player 2' ? 'Player 2' : 'Tie'
}

console.log(rockPaperScissorsLizardSpock(RANDOM_ENTRIES))