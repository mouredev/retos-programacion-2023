void main() {
  print(rockPaperScissorsLizardSpock([
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"]
  ]));
}

String rockPaperScissorsLizardSpock(List<List<String>> list) {
  int player1 = 0;
  int player2 = 0;
  for (int i = 0; i < list.length; i++) {
    if (list[i][0] == "🗿" && list[i][1] == "✂️") {
      player1++;
    } else if (list[i][0] == "🗿" && list[i][1] == "🦎") {
      player1++;
    } else if (list[i][0] == "📄" && list[i][1] == "🗿") {
      player1++;
    } else if (list[i][0] == "📄" && list[i][1] == "🖖") {
      player1++;
    } else if (list[i][0] == "✂️" && list[i][1] == "📄") {
      player1++;
    } else if (list[i][0] == "✂️" && list[i][1] == "🦎") {
      player1++;
    } else if (list[i][0] == "🦎" && list[i][1] == "📄") {
      player1++;
    } else if (list[i][0] == "🦎" && list[i][1] == "🖖") {
      player1++;
    } else if (list[i][0] == "🖖" && list[i][1] == "🗿") {
      player1++;
    } else if (list[i][0] == "🖖" && list[i][1] == "✂️") {
      player1++;
    } else if (list[i][0] == "✂️" && list[i][1] == "🗿") {
      player2++;
    } else if (list[i][0] == "🦎" && list[i][1] == "🗿") {
      player2++;
    } else if (list[i][0] == "🗿" && list[i][1] == "📄") {
      player2++;
    } else if (list[i][0] == "🖖" && list[i][1] == "📄") {
      player2++;
    } else if (list[i][0] == "📄" && list[i][1] == "✂️") {
      player2++;
    } else if (list[i][0] == "🦎" && list[i][1] == "✂️") {
      player2++;
    } else if (list[i][0] == "📄" && list[i][1] == "🦎") {
      player2++;
    } else if (list[i][0] == "🖖" && list[i][1] == "🦎") {
      player2++;
    } else if (list[i][0] == "🗿" && list[i][1] == "🖖") {
      player2++;
    } else if (list[i][0] == "✂️" && list[i][1] == "🖖") {
      player2++;
    }
  }
  if (player1 > player2) {
    return "Player 1";
  } else if (player1 < player2) {
    return "Player 2";
  } else {
    return "Tie";
  }
}
