/*
  Reglas:
    Tijeras cortan papel
    Papel cubre piedra
    Piedra aplasta lagarto
    Lagarto envenena Spock
    Spock destruye tijeras
    Tijeras decapitan lagarto
    Lagarto come papel
    Papel desaprueba Spock
    Spock vaporiza piedra
    Piedra aplasta tijeras 
*/

function isArrayInArray(arr, item) {
  let item_as_string = JSON.stringify(item)

  return arr.some(function (ele) {
    return JSON.stringify(ele) === item_as_string
  })
}

function gamePPTLG(games) {
  const combinations = [
    ['✂️', '📄'], ['📄', '🗿'], ['🗿', '🦎'], ['🦎', '🖖'], ['🖖', '✂️'],
    ['✂️', '🦎'], ['🦎', '📄'], ['📄', '🖖'], ['🖖', '🗿'], ['🗿', '✂️']
  ]

  let results = { P1: 0, P2: 0 }

  for (let i = 0;i < games.length;i++) {
    if (games[i].some(n => n !== '✂️' && n !== '📄' && n !== '🗿' && n !== '🦎' && n !== '🖖')) {
      return "Input error"
    }

    if (games[i][1] !== games[i][0]) {
      if (isArrayInArray(combinations, games[i])) {
        results.P1 += 1
      } else {
        results.P2 += 1
      }
    }
  }

  if (results.P1 > results.P2) {
    return "Player 1"
  } else if (results.P1 < results.P2) {
    return "Player 2"
  } else {
    return "Tie"
  }
}


console.log(gamePPTLG([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))   // Player 2
console.log(gamePPTLG([["🖖", "🦎"], ["✂️", "🗿"], ["📄", "✂️"]]))  // Player 2
console.log(gamePPTLG([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "📄"]]))   // Tie
console.log(gamePPTLG([["🗿", "✂️"], ["🦎", "📄"], ["✂️", "🦎"]]))  // Player 1
console.log(gamePPTLG([["🗿", "✂️"], ["🦎", "📄"]]))                 // Player 1
console.log(gamePPTLG([["🗿", "✂️"], ["🦎", "13"], ["✂️", "🦎"]]))  // Input Error
