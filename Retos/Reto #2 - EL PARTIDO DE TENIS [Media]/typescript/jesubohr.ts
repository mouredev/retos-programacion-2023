const SCORES = {
  0: "Love",
  1: "15",
  2: "30",
  3: "40",
}

function getMatchWinner(wins: string[]) {
  let P1 = 0, P2 = 0
  for (const win of wins) {
    if (win === "P1") P1++
    if (win === "P2") P2++

    if (P1 >= 5 && P2 === P1 - 2) break
    else if (P2 >= 5 && P1 === P2 - 2) break

    if (P1 >= 3 && P2 >= 3) {
      if (P1 === P2) console.log("Deuce")
      if (P1 > P2) console.log(`Advantage P1`)
      if (P2 > P1) console.log(`Advantage P2`)
    } else console.log(`${SCORES[P1]} - ${SCORES[P2]}`)
  }

  if (P1 > P2) console.log("P1 wins")
  if (P2 > P1) console.log("P2 wins")
}

const secuence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
getMatchWinner(secuence)
