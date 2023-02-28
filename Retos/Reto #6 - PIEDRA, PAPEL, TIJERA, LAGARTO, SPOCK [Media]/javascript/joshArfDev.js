const gamet = (games) => {
  const rules = {
    "🗿": ["✂️", "🦎"],
    "🧻": ["🗿", "🖐"],
    "✂️": ["🧻", "🦎"],
    "🦎": ["🖐", "🧻"],
    "🖐": ["✂️", "🗿"],
  };

  let playerOne = 0;
  let playerTwo = 0;

  for (const game of games) {
    const playerOneGame = game[0];
    const playerTwoGame = game[1];

    if (rules[playerOneGame].includes(playerTwoGame)) {
        playerOne++;
    } else {
        playerTwo++;
    }
  }

  return playerOne === playerTwo
    ? "Tie"
    : playerOne > playerTwo
    ? "Player 1 Won!! ✔ "
    : "Player 2 Won!! ✔ ";
};

console.log(
  gamet([
    ["🗿", "✂️"],
    ["🖖", "🦎"],
    ["🧻", "🗿"],
  ])
);
