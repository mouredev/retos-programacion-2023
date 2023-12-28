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
 
import java.util.Scanner;

public class kaigue {

    public static void calculadora(int[] players) {
        var Player1 = 0;
        var Player2 = 0;
        boolean p1Ventaja = false;
        boolean p2Ventaja = false;
       
        System.out.println("");
        for (int i = 0; i < players.length; i++) {
            if (players[i] == 1) {
                if (Player1 < 30) {
                    Player1 += 15;
                } else {
                    Player1 += 10;
                }
            } else if (players[i] == 2) {
                if (Player2 < 30) {
                    Player2 += 15;
                } else {
                    Player2 += 10;
                }
            }
            
            //algoritmo en caso de deuce
            if (Player1 >= 40 && Player2 >= 40) {
                if (Player1 == Player2) {
                    System.out.println("Deuce");

                } else if (Player1 > Player2) {
                    if (p1Ventaja == false) {
                        System.out.println("Ventaja P1");
                        p1Ventaja = true;
                    } else {
                        System.out.println("Ha ganado el P1");
                        break;
                    }

                } else if (Player2 > Player1) {
                    if (p2Ventaja == false) {
                        System.out.println("Ventaja P2");
                        p2Ventaja = true;
                    } else {
                        System.out.println("Ha ganado el P2");
                        break;
                    }
                }
                //algoritmo en caso de juego normal(sin deuce)
            } else if (Player1 >= 50 || Player2 >= 50) {
                if (Player1 > Player2) {
                    System.out.println("Ha ganado el P1");
                    break;
                } else {
                    System.out.println("Ha ganado el P2");
                    break;
                }
                //algoritmo para imprimir Love
            } else {
                if (Player1 == 0) {
                    System.out.println("Love" + " - " + Player2);
                } else if (Player2 == 0) {
                    System.out.println(Player1 + " - " + "Love");
                } else {
                    System.out.println(Player1 + " - " + Player2);
                }          
            }
        }
    }
    
    public static void main(String[] args) throws Exception {
        int[] players = new int[8];
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Introducir la secuencia de jugadas del punto [1] " +
            "para Player1 o [2] para Player2: " + 
            "\n0 para terminar" );
            for (int i = 0; i < players.length; i++) {
                System.out.println("1 o 2");
                players[i] = sc.nextInt();
            }

            //Imprimir la secuencia introducida
            System.out.println("\n");
            for (int j = 0; j < players.length; j++) {      
                if (j == 0) {
                    System.out.print("[P" + players[j] + ",");
                } else if (j == (players.length - 1)) {
                    System.out.print(" P" + players[j] + "]");
                } else if (j > 0 && j < players.length) {
                    System.out.print(" P" + players[j] + ",");
                }
            }
            calculadora(players);
            
        }
    }
}
