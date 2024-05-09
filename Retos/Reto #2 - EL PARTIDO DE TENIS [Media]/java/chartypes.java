public class chartypes {

  public static void main(String[] args) {
    String[] firstGame = { "P1", "P1", "p2", "p2", "p1", "p2", "p1", "p1" };
    String[] secondGame = { "p2", "P2" };
    String[] thirdGame = { "P1", "P1", "p1", "p1", "p1", "p1", "p1", "p1" };
    System.out.println(TennisGame.start(firstGame));
    System.out.println(TennisGame.start(secondGame));
    System.out.println(TennisGame.start(thirdGame));
  }

}

class TennisGame {
  private TennisGame() {
  }

  static final String[] SCORES = { "love", "15", "30", "40" };

  static String start(String[] game) {
    int p1Points = 0;
    int p2Points = 0;

    for (String player : game) {
      switch (player.toUpperCase()) {
        case "P1":
          p1Points++;
          break;
        case "P2":
          p2Points++;
          break;
        default:
          return "Error no valid entry for the players";
      }
    }

    if (p1Points < 4 && p2Points < 4)
      return SCORES[p1Points] + " - " + SCORES[p2Points];
    else if (p1Points == p2Points)
      return "Deuce";
    else {
      if (p1Points > p2Points)
        return "Ventaja Player1";
      else if (p2Points > p1Points)
        return "Ventaja Player2";
    }

    return "";
  }

}
