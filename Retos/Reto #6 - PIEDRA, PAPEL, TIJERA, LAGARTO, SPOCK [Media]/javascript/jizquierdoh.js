const calculateWinner = (plays) => {
  const outcomes = {
    "🗿": {
      "✂️": 1,
      "🦎": 1,
      "📄": 0,
      "🖖": 0
    },
    "📄": {
      "🗿": 1,
      "🖖": 1,
      "✂️": 0,
      "🦎": 0
    },
    "✂️": {
      "📄": 1,
      "🦎": 1,
      "🗿": 0,
      "🖖": 0
    },
    "🦎": {
      "📄": 1,
      "🖖": 1,
      "🗿": 0,
      "✂️": 0
    },
    "🖖": {
      "🗿": 1,
      "✂️": 1,
      "📄": 0,
      "🦎": 0
    }
  };

  let player1Wins = 0;
  let player2Wins = 0;

  for (const play of plays) {
    const player1 = play[0];
    const player2 = play[1];

    if (player1 === player2) {
      continue;
    } else if (outcomes[player1][player2] === 1) {
      player1Wins++;
    } else {
      player2Wins++;
    }
  }

  if (player1Wins > player2Wins) {
    return "Player 1";
  } else if (player2Wins > player1Wins) {
    return "Player 2";
  } else {
    return "Tie";
  }
}
