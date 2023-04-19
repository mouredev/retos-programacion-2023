const playItems = {
  "🗿": ["🦎", "✂️"],
  "📄": ["🗿", "🖖"],
  "✂️": ["📄", "🦎"],
  "🦎": ["🖖", "📄"],
  "🖖": ["✂️", "🗿"],
};

function rockPaperScissorsLizardSpock(games) {
  let playerOnePoints = 0;
  let playerTwoPoints = 0;

  games.forEach((game) => {
    const playerOne = game[0];
    const playerTwo = game[1];

    if (playItems[playerOne].includes(playerTwo)) {
      playerOnePoints++;
      // necesito chequear en el false tb que no sean iguales, si no nunca entraría al Tie
    } else if (playItems[playerOne] !== playItems[playerTwo]) {
      playerTwoPoints++;
    }
  });

  if (playerOnePoints === playerTwoPoints) {
    return "Tie";
  } else if (playerOnePoints > playerTwoPoints) {
    return "Player 1";
  } else {
    return "Player 2";
  }
}

console.log(
  rockPaperScissorsLizardSpock([
    ["✂️", "✂️"],
    ["📄", "📄"],
    ["📄", "📄"],
  ])
);
