/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

class TennisGame {

  public static int p1 = 0, p2 = 0;
  public static boolean won = false;

  public static final String[] POINTS = {"Love", "15", "30", "40", "Ventaja P", "Ha ganado el P"};

  public static void printPair() {
    if (p1 == p2 && p1 >= 3) {
      System.out.printf("Deuce%n");
    } else if(p1 >= 4 && p2 < p1) {
      System.out.printf("%s1%n", POINTS[p1]);
      won = true;
    } else if(p2 >= 4 && p1 < p2) {
      System.out.printf("%s2%n", POINTS[p2]);
      won = true;
    } else {
      System.out.printf("%s - %s%n", POINTS[p1], POINTS[p2]);
    }
  }
  
  public static void printScore(String[] points) {
    while (!won) {
      for (String p : points) {
        if ("P1".equalsIgnoreCase(p)) p1++;
        else if ("P2".equalsIgnoreCase(p)) p2++;
        else {
          System.out.printf("Unkown word `%s` in the input%n", p);
          return;
        }
        if (p1 >= 6 || p2 >= 6) break;
        printPair();
      }
    }
  }

  public static void main(String... s) {
    String[] puntos = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
    printScore(puntos);
  }
}
