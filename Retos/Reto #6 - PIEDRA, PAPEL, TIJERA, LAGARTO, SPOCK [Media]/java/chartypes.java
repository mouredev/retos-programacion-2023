
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;

public class chartypes {

  public static void main(String[] args) {
    List<List<String>> game = new ArrayList<>();
    game.add(List.of("rock", "paper"));
    game.add(List.of("lizard", "spock"));
    game.add(List.of("paper", "rock"));
    try {
      Game myGame = new Game(game);
      // myGame.addEntry(List.of("rock", "paper"));
      // myGame.addEntry(List.of("lizard", "spock"));
      // myGame.addEntry(List.of("rock", "paper"));
      myGame.showEntries();
      System.out.println("Winner: " + myGame.winner());

    } catch (Game.IlegalEntries | Game.FullEntriesException e) {
      System.out.println(e.getMessage());
    }

  }

}

class Game {

  public static class FullEntriesException extends Exception {
    public FullEntriesException() {
      super();
    }

    @Override
    public String getMessage() {
      return "Number of entries exceeded";
    }
  }

  public class IlegalEntries extends Exception {
    public IlegalEntries() {
      super();
    }

    @Override
    public String getMessage() {
      return "Please make sure you are inserting correct entries";
    }
  }

  private final String PLAYER1 = "Player 1";
  private final String PLAYER2 = "Player 2";
  private List<List<String>> game;
  private Map<String, List<String>> RULES = new HashMap<>(5);
  private final Set<String> VALID_ENTRIES = RULES.keySet();

  private void rulesBuilder() {
    RULES.put("ROCK", List.of("SCISSORS", "LIZARD"));
    RULES.put("PAPER", List.of("SPOCK", "ROCK"));
    RULES.put("SCISSORS", List.of("PAPER", "LIZARD"));
    RULES.put("SPOCK", List.of("SCISSORS", "ROCK"));
    RULES.put("LIZARD", List.of("PAPER", "SPOCK"));
  }

  public Game(List<List<String>> game) throws IlegalEntries, FullEntriesException {
    rulesBuilder();
    for (List<String> par : game) {
      System.out.println(par);
      if (!validEntries(par))
        throw new IlegalEntries();
    }
    if (game.size() > 3)
      throw new FullEntriesException();
    this.game = game;
  }

  public Game() {
    game = new ArrayList<>();
    rulesBuilder();
  }

  public void addEntry(List<String> par) throws FullEntriesException, IlegalEntries {
    if (game.size() >= 3)
      throw new FullEntriesException();
    if (!validEntries(par))
      throw new IlegalEntries();
    game.add(par);
  }

  private boolean validEntries(List<String> par) {
    String firstEntry = par.getFirst().toUpperCase();
    String secondEntry = par.getLast().toUpperCase();

    if (par.size() < 3 && VALID_ENTRIES.contains(firstEntry) && VALID_ENTRIES.contains(secondEntry))
      return true;
    return false;
  }

  public void showEntries() {
    System.out.println(game);
  }

  public String winner() {
    int pointsP1 = 0;
    int pointsP2 = 0;

    for (List<String> par : game) {
      if (RULES.get(par.getFirst().toUpperCase()).contains(par.getLast().toUpperCase()))
        pointsP1++;
      else
        pointsP2++;
    }
    if (pointsP1 > pointsP2)
      return PLAYER1;
    if (pointsP2 > pointsP1)
      return PLAYER2;
    else
      return "TIE";
  }

}
