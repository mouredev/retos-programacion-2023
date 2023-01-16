void main() {
  calculateWinner(winnerList: ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
}

void calculateWinner({winnerList = List<String>}) {
  List<String> scores = ["Love", "15", "30", "40"];

  var player1 = "p1";
  var player2 = "p2";

  var player1Points = 0;
  var player2Points = 0;

  print("P1 - P2");
  print("-------");

  for (var player in winnerList) {
    var winner = player.toLowerCase();

    if (winner == player1)
      player1Points += 1;
    else if (winner == player2)
      player2Points += 1;
    else
      continue;

    if (player1Points == player2Points && player1Points == 3)
      print("Deuce");
    else if (player1Points == 4)
      print("ventaja P1");
    else if (player2Points == 4)
      print("ventaja P2");
    else if (player1Points == 5) {
      print("Ha ganado el P1");
      return;
    } else if (player2Points == 5) {
      print("Ha ganado el P2");
      return;
    } else if (player1Points > 5 || player2Points > 5)
      return;
    else
      print("${scores[player1Points]} - ${scores[player2Points]}");
  }
}
