package Reto_2;

import java.util.Scanner;

public class erosiim {
    /*
     * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
     * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
     * gane cada punto del juego.
     *
     * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
     * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
     *   15 - Love x
     *   30 - Love x
     *   30 - 15 x
     *   30 - 30
     *   40 - 30
     *   Deuce
     *   Ventaja P1
     *   Ha ganado el P1
     * - Si quieres, puedes controlar errores en la entrada de datos.
     * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p1Points=0;
        int p2Points=0;
        var rawMatch = sc.nextLine();
        rawMatch = rawMatch.substring(1, rawMatch.length()-1);
        String[] pointsMatch = rawMatch.split(", ");
        for (int i = 0; i < pointsMatch.length; i++) {
            switch (pointsMatch[i]){
                case ("P1"):
                    if(p1Points==30){
                        p1Points+=10;
                    }else{
                        p1Points+=15;
                    }
                    break;
                case ("P2"):
                    if(p2Points==30){
                        p2Points+=10;
                    }else{
                        p2Points+=15;
                    }
                    break;
                default:
                    break;
            }
            if(p1Points == 0 && (p1Points<p2Points)){
                System.out.println("Love - " + p2Points);
            } else if(p2Points == 0 && (p1Points>p2Points)){
                System.out.println( p1Points + " - Love");
            } else if(p1Points == 40 && p1Points == p2Points ){
                System.out.println("Deuce");
            } else if (p1Points == 55 ) {
                System.out.println("Ventaja P1");
            } else if (p1Points > 55 && p1Points > p2Points) {
                System.out.println("Ha ganado p1");
            } else if (p2Points == 55 ) {
                System.out.println("Ventaja P2");
            } else if (p2Points > 55 && p2Points > p1Points) {
                System.out.println("Ha ganado p2");
            } else {
                System.out.println(p1Points + " - " + p2Points);
            }
        }
    }
}
