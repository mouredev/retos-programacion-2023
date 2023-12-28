function getVictor(game) {
  let pointsPlayerOne = 0, pointsPlayerTwo = 0;

  for (let playersChoice of game) {
    let resultOfGettingThePoint = getPoint(playersChoice);

    if (resultOfGettingThePoint === undefined || playersChoice[0] === playersChoice[1])
        continue;

    if (resultOfGettingThePoint) {
      pointsPlayerOne++;
    } else {
      pointsPlayerTwo++;
    }
  }
  
  if (pointsPlayerOne === pointsPlayerTwo) return "Tie";
  if (pointsPlayerOne > pointsPlayerTwo) return "Player 1";
  if (pointsPlayerOne < pointsPlayerTwo) return "Player 2";
}

function getPoint(playersChoice) {
  let validValues = ["✂️", "📄", "🗿", "🦎", "🖖"];
  let winningCombinations = {
    "✂️": ["📄", "🦎"],
    "📄": ["🗿", "🖖"],
    "🗿": ["🦎", "✂️"],
    "🦎": ["🖖", "📄"],
    "🖖": ["✂️", "🗿"],
  };

  if (!validValues.includes(playersChoice[0]) || !validValues.includes(playersChoice[1]))
    return undefined;

  return winningCombinations[playersChoice[0]].includes(playersChoice[1]);
}

let game = [["🗿", "✂️"],["✂️", "🗿"],["📄", "✂️"],["🦎","🖖"],["🦎","📄"],["✂️","🖖"]];

console.log("Result:", getVictor(game));