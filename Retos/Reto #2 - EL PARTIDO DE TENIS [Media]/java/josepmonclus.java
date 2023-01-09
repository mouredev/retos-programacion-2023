import java.util.Scanner;

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

public class josepmonclus {
    
    private static String p1 = "Love";
    private static String p2 = "Love";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String line = null;
        while(sc.hasNextLine()) {
            line = sc.nextLine().toUpperCase();
            
            if(line.equals("P1")){
                addPointP1();
            } else if(line.equals("P2")) {
                addPointP2();
            } else {
                System.out.println("Punto introducido incorrectamente, valores válidos: P1 o P2");
            }

            System.out.println(printResult());
            
            if(p1.equals("WIN") || p2.equals("WIN")) {
                break;
            }
        }
        
        sc.close();
    }

    private static void addPointP1() {
        if(p1.equals("Love")) {
            p1 = "15";
        } else if(p1.equals("15")) {
            p1 = "30";
        } else if(p1.equals("30")) {
            p1 = "40";
        } else if(p1.equals("40")) {
            if(p2.equals("Love") || p2.equals("15") || p2.equals("30")) {
                p1 = "WIN";
            } else if(p2.equals("ADV")) {
                p2 = "40";
            } else if(p2.equals("40")) {
                p1 = "ADV";
            }
        } else if(p1.equals("ADV")) {
            p1 = "WIN";
        }
    }

    private static void addPointP2() {
        if(p2.equals("Love")) {
            p2 = "15";
        } else if(p2.equals("15")) {
            p2 = "30";
        } else if(p2.equals("30")) {
            p2 = "40";
        } else if(p2.equals("40")) {
            if(p1.equals("Love") || p1.equals("15") || p1.equals("30")) {
                p2 = "WIN";
            } else if(p1.equals("ADV")) {
                p1 = "40";
            } else if(p1.equals("40")) {
                p2 = "ADV";
            }
        } else if(p2.equals("ADV")) {
            p2 = "WIN";
        }
    }

    private static String printResult() {
        if (p1.equals("40") && p2.equals("40")) {
            return "Deuce";
        } else if(p1.equals("WIN")) {
            return "Ha ganado el P1";
        } else if(p2.equals("WIN")) {
            return "Ha ganado el P2";
        } else if(p1.equals("ADV")) {
            return "Ventaja P1";
        } else if(p2.equals("ADV")) {
            return "Ventaja P2";
        } else {
            return p1 + " - " + p2;
        }
    }
}
