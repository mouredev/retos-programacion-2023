import java.util.Scanner;

/**
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo
 * ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player
 * 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce"
 * (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría
 * lo siguiente:
 * 15 - Love
 * 30 - Love
 * 30 - 15
 * 30 - 30
 * 40 - 30
 * Deuce
 * Ventaja P1
 * Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 *
 * @author anmac
 */

public class anmac {

  enum Players {
    P1,
    P2;
  }

  private static final String[] SCORES = { "Love", "15", "30", "40" };
  private static int p1_score = 0;
  private static int p2_score = 0;
  private static boolean finished = false;

  public static void main(String[] args) {
    String[] inputSequence = getInputSequence(args);
    for (String player : inputSequence) {
      if (finished) {
        throw new IllegalArgumentException("Los puntos jugados no son correctos");
      }
      updateScore(player);
      printScore(inputSequence);
    }
    System.exit(0); // Game over
  }

  private static String[] getInputSequence(String[] args) {
    if (args.length > 0)
      return String.join(" ", args).replace(",", "").split("\s+");

    String input = "";
    System.out.println("Enter a sequence like this: P1, P1, P2, P2, P1, P2, P1, P1");
    try (Scanner sc = new Scanner(System.in)) {
      while (true) {
        input = sc.nextLine().trim(); // Make sure there is something else than spaces
        if (!input.isEmpty())
          break;
        System.out.println("Input cannot be empty. Please try again.");
      }
    }
    return input.split(",\s*");
  }

  private static void updateScore(String player) {
    Players currentPlayer = null;
    try {
      currentPlayer = Players.valueOf(player);
    } catch (IllegalArgumentException e) {
      System.out.println(STR."Error: Invalid player input \{player}. Please enter either 'P1' or 'P2'.");
      System.exit(1);
    }

    if (currentPlayer == Players.P1)
      p1_score++;
    else
      p2_score++;
  }

  private static void printScore(String[] list) {
    if (p1_score == p2_score) {
      System.out.println(p1_score >= 3 ? "Deuce" : STR."\{SCORES[p1_score]} - \{SCORES[p2_score]}");
    } else {
      if (p1_score <= 3 && p2_score <= 3)
        System.out.println(STR."\{SCORES[p1_score]} - \{SCORES[p2_score]}");
      else if (Math.abs(p1_score - p2_score) <= 1)
        System.out.println("Advantage " + ((p1_score > p2_score) ? "P1" : "P2"));
      else {
        System.out.println("Player " + ((p1_score > p2_score) ? "P1" : "P2") + " has won");
        finished = true;
      }
    }
  }
}
