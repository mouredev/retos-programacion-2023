void main() {
  print(rockPaperScissorLizardSpock([Round(Play.ROCK, Play.ROCK)]));
  print(rockPaperScissorLizardSpock([Round(Play.ROCK, Play.SCISSORS)]));
  print(rockPaperScissorLizardSpock([Round(Play.SCISSORS, Play.ROCK)]));
  print(rockPaperScissorLizardSpock([
    Round(Play.ROCK, Play.ROCK),
    Round(Play.ROCK, Play.ROCK),
    Round(Play.ROCK, Play.ROCK),
    Round(Play.ROCK, Play.ROCK),
  ]));
  print(rockPaperScissorLizardSpock([
    Round(Play.ROCK, Play.ROCK),
    Round(Play.SCISSORS, Play.PAPER),
    Round(Play.ROCK, Play.ROCK),
    Round(Play.LIZARD, Play.SPOCK),
  ]));
}

enum Play {
  ROCK,
  PAPER,
  SCISSORS,
  LIZARD,
  SPOCK,
}

class Round {
  Play player1;
  Play player2;

  Round(this.player1, this.player2);
}

Map<Play, List<Play>> rules = {
  Play.ROCK: [Play.SCISSORS, Play.LIZARD],
  Play.PAPER: [Play.ROCK, Play.SPOCK],
  Play.SCISSORS: [Play.PAPER, Play.SPOCK],
  Play.LIZARD: [Play.SPOCK, Play.PAPER],
  Play.SPOCK: [Play.ROCK, Play.SCISSORS],
};

String rockPaperScissorLizardSpock(List<Round> game) {
  int playerOne = 0;
  int playerTwo = 0;

  for (Round i in game) {
    if (i.player1 != i.player2) {
      rules[i.player1]!.contains(i.player2) ? playerOne += 1 : playerTwo += 1;
    }
  }

  if (playerOne == playerTwo)
    return "Tie";
  else if (playerOne > playerTwo)
    return "Player 1";
  else
    return "Player 2";
}
