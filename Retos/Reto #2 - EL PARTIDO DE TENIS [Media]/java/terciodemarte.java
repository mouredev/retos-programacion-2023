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
 * Hecho por Albano Díez el 02/01/2023
 */

import java.util.Scanner;

public class reto2 {

    public static void main(String[] args) {
        Scanner lectura = new Scanner(System.in);
        byte p1 = 0, p2 = 0;
        String player;
        boolean control = true;
        System.out.println("EMPIEZA EL PARTIDO");
        do {

            System.out.println("\n Dime quien jugador ha ganado");
            player = lectura.nextLine();
            
            if (player.equals("P1")) {

                if (p1 == 3 && p2 == 4) {
                    p2 -= 1;
                } else {
                    p1 += 1;
                }
                control = marcador(p1, p2);
            } else if (player.equals("P2")) {

                if (p1 == 4 && p2 == 3) {
                    p1 -= 1;
                } else {
                    p2 += 1;
                }
                control = marcador(p1, p2);
            } else {
                System.out.println("Jugador no valido");
            }

            

        } while (control);

    }

    public static boolean marcador(byte p1, byte p2) {
        String puntuacion[] = new String[]{"Love", "15", "30", "40", "Deuce", "Ventaja"};
        if (p1 == 3 && p2 == 3) {
            System.out.println(puntuacion[4]);
            return true;
        } else if (p1 == 4 && p2 == 3) {
            System.out.println(puntuacion[5] + " P1");
            return true;
        } else if (p1 == 3 && p2 == 4) {
            System.out.println(puntuacion[5] + " P2");
            return true;
        }else if(p1==5||(p1==4&&p2<3)){
            System.out.println("Ha ganado el P1");
            return false;
        }else if(p2==5||(p2==4&&p1<3)){
            System.out.println("Ha ganado el P2");
            return false;
        }else{
            System.out.println(puntuacion[p1]+" - "+puntuacion[p2]);
            return true;
        }
    }

}
