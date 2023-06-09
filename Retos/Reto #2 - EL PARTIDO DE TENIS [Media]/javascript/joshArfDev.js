const points = {
  0: "Love",
  1: "15",
  2: "30",
  3: "40",
};

const tenisGame = (game) => {
  let p_1Points = 0;
  let p_2Points = 0;

  for (let matches in game) {
    let player = game[matches];

    player === "P1" ? p_1Points++ : player === "P2" ? p_2Points++ : null;

    p_1Points < 3 || p_2Points < 3
      ? console.log(`${points[p_1Points]} - ${points[p_2Points]}`)
      : p_1Points === p_2Points
      ? console.log("Deuce")
      : p_1Points === 3 && p_2Points === 4
      ? console.log(`Advantage ${player}`)
      : p_2Points === 3 && p_1Points === 4
      ? console.log(`Advantage ${player}`)
      : console.log(`Won player: ${player}`)
  }
};

tenisGame(["P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2"]);
          //15    30    15    30    40    40   AD     40