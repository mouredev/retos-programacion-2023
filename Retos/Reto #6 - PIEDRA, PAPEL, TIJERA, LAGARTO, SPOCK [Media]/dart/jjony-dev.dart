void main(List<String> args) {
  List<List<Play>> matchs = [
    [Play.Rock, Play.Scissors],
    [Play.Scissors, Play.Rock],
    [Play.Paper, Play.Scissors],
    [Play.Spock, Play.Scissors],
    [Play.Spock, Play.Paper],
    [Play.Lizard, Play.Lizard],
  ];

  RPCLSGame game = RPCLSGame();
  int scoreP1 = 0;
  int scoreP2 = 0;

  for (var match in matchs) {
    int round = 0;
    switch (game.checkPlay(match[0], match[1])) {
      case 1:
        // print("Player 1 win");
        scoreP1++;
        break;
      case -1:
        // print("Player 2 win");
        scoreP2++;
        break;
      case 0:
        // print("Tie");
        break;
    }
    round++;
  }

  String result = "";
  if (scoreP1 == scoreP2) {
    result = "Tie";
  } else if (scoreP1 > scoreP2) {
    result = "Player 1";
  } else {
    result = "Player 2";
  }
  print("Resultado: $result");
}

enum Play { Rock, Paper, Scissors, Lizard, Spock }

//Rock, Paper, Scissors, Lizard, Spock (RPCLS)
class RPCLSGame {
  Map<Play, List<Play>> winningRules = {
    Play.Rock: [Play.Scissors, Play.Lizard],
    Play.Paper: [Play.Rock, Play.Spock],
    Play.Scissors: [Play.Paper, Play.Lizard],
    Play.Lizard: [Play.Paper, Play.Spock],
    Play.Spock: [Play.Scissors, Play.Rock],
  };

  int checkPlay(Play p1, Play p2) {
    if (p1 == p2) {
      return 0;
    } else {
      return winningRules[p1]!.contains(p2) ? 1 : -1;
    }
  }
}
