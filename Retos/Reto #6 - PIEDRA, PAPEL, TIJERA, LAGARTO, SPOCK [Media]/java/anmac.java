/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️ " (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 *
 * Rules:
 * - Tijeras cortan Papel. ✂️  > 📄
 * - Papel cubre Piedra. 📄 > 🗿
 * - Piedra tritura Lagarto. 🗿 > 🦎
 * - Lagarto envenena Spock. 🦎 > 🖖
 * - Spock rompe Tijeras. 🖖 > ✂️
 * - Tijeras decapitan Lagarto. ✂️ > 🦎
 * - Lagarto come Papel. 🦎 > 📄
 * - Papel desautoriza Spock. 📄 > 🖖
 * - Spock vaporiza Piedra. 🖖 > 🗿
 * - Piedra tritura Tijeras. 🗿 > ✂️
 *
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class anmac {
  private enum Move {
    ROCK("🗿"),
    PAPER("📄"),
    SCISSORS("✂️"),
    LIZARD("🦎"),
    SPOCK("🖖");

    private final String emoji;

    Move(String emoji) {
      this.emoji = emoji;
    }

    public String getEmoji() {
      return emoji;
    }

    public int compareMoves(Move otherMove) {
      if (this == otherMove) return 0;
      return switch (this) {
        case ROCK -> (otherMove == SCISSORS || otherMove == LIZARD) ? 1 : -1;
        case PAPER -> (otherMove == ROCK || otherMove == SPOCK) ? 1 : -1;
        case SCISSORS -> (otherMove == PAPER || otherMove == LIZARD) ? 1 : -1;
        case LIZARD -> (otherMove == SPOCK || otherMove == PAPER) ? 1 : -1;
        case SPOCK -> (otherMove == SCISSORS || otherMove == ROCK) ? 1 : -1;
        default -> throw new IllegalArgumentException("Unknown move: " + this);
      };
    }
  }

  public static void main(String[] args) {
    List<Move[]> rounds =
        new ArrayList<>(
            Arrays.asList(
                new Move[] {Move.ROCK, Move.SPOCK},
                new Move[] {Move.SCISSORS, Move.ROCK},
                new Move[] {Move.PAPER, Move.SCISSORS}));

    int p1Score = 0;
    int p2Score = 0;

    for (Move[] moves : rounds) {
      Move p1Move = moves[0];
      Move p2Move = moves[1];
      if (p1Move == p2Move) {
        System.out.println(p1Move.getEmoji() + " = " + p2Move.getEmoji());
      } else {
        int result = p1Move.compareMoves(p2Move);
        if (result > 0) {
          p1Score++;
        } else {
          p2Score++;
        }
        System.out.println(p1Move.getEmoji() + (result > 0 ? " > " : " < ") + p2Move.getEmoji());
      }
    }

    String winner = (p1Score == p2Score) ? "Tie" : (p1Score > p2Score) ? "Player 1" : "Player 2";
    System.out.println("Winner: " + winner);
  }
}
