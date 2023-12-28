package Ilmanamudi;


import java.util.Arrays;
import java.util.List;

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
public class PartidoTenis {
    
    public static void main(String[] args) {

        List<String> Partido = Arrays.asList("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1");
            
//        Puntos de un solo jugador
        
//        List<String> Partido = Arrays.asList("P1", "P1", "P1", "P1");
//        List<String> Partido = Arrays.asList("P2", "P2", "P2", "P2");

//        Juego con puntos más largos  

//        List<String> Partido = Arrays.asList("P2", "P2", "P2", "P1", "P1", "P1", "P2", "P1","P2", "P1", "P1", "P2", "P2", "P1", "P2", "P1","P1", "P2", "P1", "P2", "P2", "P2");
//        List<String> Partido = Arrays.asList("P2", "P1", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1");
        int P1 = 0;                        
        int P2 = 0;

        for (String punto : Partido) {

            if (!punto.equals("P1") && !punto.equals("P2")) {
                System.out.println("Error de ingreso");
                break;
            }

            P1 += (punto.equals("P1") && P1 == 40 && P2 == 50) ? 0 :
                    punto.equals("P1") && P1 < 30 ? 15 :
                    punto.equals("P1") && P1 >= 30 ? 10 : 0;
            P2 += (punto.equals("P2") && P2 == 40 && P1 == 50) ? 0 :
                    punto.equals("P2") && P2 < 30 ? 15 :
                    punto.equals("P2") && P2 >= 30 ? 10 : 0;
          
            P1 -= punto.equals("P2") && P1 == 50 ? 10 : 0;
            P2 -= punto.equals("P1") && P2 == 50 ? 10 : 0;
            
            System.out.println((P1 == 60) || (P1==50 && P2<=30) ? "Ha ganado P1" : (P2 == 60) || (P2==50 && P1<=30) ? "Ha ganado P2"
                    : (P1 == 40 && P2 == 40) ? "Deuce"
                            : (P1 >= 50 && P2 >= 40) ? "Ventaja P1" : (P1 >= 40 && P2 >= 50) ? "Ventaja P2"
                                            : (P1 == 0 ? "Love" : P1) + (" - ") + (P2 == 0 ? "Love" : P2));

        }
    }
}
