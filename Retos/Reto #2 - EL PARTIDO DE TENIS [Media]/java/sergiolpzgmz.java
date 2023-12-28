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
public class sergiolpzgmz {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int puntosP1=0;
        int puntosP2=0;
        boolean salir = false;

        while (salir != true) {
            System.out.print("Quien gana el punto de juego P1 o P2?: ");
            String ganadorPunto = entrada.nextLine().toLowerCase();

            switch (ganadorPunto) {
                case "p1":
                    if (puntosP1 < 30) puntosP1 += 15;
                    else if (puntosP1 >= 30) puntosP1 += 10;
                    break;
                case "p2":
                    if (puntosP2 < 30) puntosP2 += 15;
                    else if (puntosP2 >= 30) puntosP2 += 10;
                    break;
                default:
                    System.out.println("Error, introduzca P1 o P2");
            }
            
            if (puntosP1>40 && puntosP2<40){
                System.out.println("Gana P1");
                salir=true;
            }
            if (puntosP2>40 && puntosP1<40){
                System.out.println("Gana P2");
                salir=true;
            }
            if(puntosP1>=40 && puntosP2>=40){
                if (puntosP1 == puntosP2) System.out.println("Deuce");
                else if (puntosP1 > puntosP2){
                    if(puntosP1-puntosP2 == 10) System.out.println("Ventaja P1");
                    else if (puntosP1-puntosP2 == 20){
                        System.out.println("Gana P1");
                        break;
                    }
                }
            }
            if(puntosP2>=40 && puntosP1>=40){
                if (puntosP2 > puntosP1){
                    if(puntosP2-puntosP1 == 10) System.out.println("Ventaja P2");
                    else if (puntosP2-puntosP1 == 20){
                        System.out.println("Gana P2");
                        break;
                    }
                }
            }
            if(puntosP1<=40 && puntosP2 <40 || puntosP2<=40 && puntosP1 <40){
                if (puntosP1==0 && puntosP2>0) System.out.println("Love"+" - "+puntosP2);
                else if (puntosP1>0 && puntosP2==0) System.out.println(puntosP1+" - "+"Love");
                else System.out.println(puntosP1+" - "+puntosP2);
            }
        }
        entrada.close();
    }
}
