#!/usr/bin/env node

class Score {
  state = [0, 0];
  gameFinish = false;
  humanPoints = ["Love", "15", "30", "40", "Deuce", "Adventage", "Win"];

  getState() {
    return this.state;
  }

  getHumanState() {
    const pointsDiff = this.state[0] - this.state[1];

    // Player WIN
    if (this.state[0] >= 4 && pointsDiff >= 2) {
      this.gameFinish = true;

      return "Player 1 WIN";
    }
    if (this.state[1] >= 4 && pointsDiff <= -2) {
      this.gameFinish = true;

      return "Player 2 WIN";
    }

    // Player Advendage
    if (this.state[0] >= 4 && pointsDiff == 1) return "Player 1 adventage";
    if (this.state[1] >= 4 && pointsDiff == -1) return "Player 2 adventage";

    // Player Deuce
    if (
      this.state[0] >= 4 &&
      this.state[1] >= 4 &&
      this.state[0] == this.state[1]
    )
      return "Deuce";

    // Normal result
    return `${this.humanPoints[this.state[0]]} - ${this.humanPoints[this.state[1]]}`;
  }

  firstPlayerWin() {
    this.state[0]++;
  }

  secondPlayerWin() {
    this.state[1]++;
  }
}

const checkIfValidGame = (game) => {
  const invalidPoints = game.filter((point) => point == 0 || point > 2);

  return invalidPoints.length == 0 ? true : false;
};

const play = (game) => {
  if (!checkIfValidGame(game)) {
    console.log("Oops! The game data has invalid format!");

    return;
  }

  const score = new Score();

  console.log(`Let's start playing ...`);

  game.map((player) => {
    if (score.gameFinish) {
      return;
    } else if (player == 1) {
      score.firstPlayerWin();
    } else if (player == 2) {
      score.secondPlayerWin();
    }

    console.log(score.getHumanState());
  });

  if (!score.gameFinish) {
    console.log("Oops! You need play more balls to finish the game!");
  }
};

const game = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2];

play(game);
