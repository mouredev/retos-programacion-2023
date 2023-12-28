import java.util.Scanner;

/**
 * Reto #2: EL PARTIDO DE TENIS
 * MEDIA | Publicación: 09/01/23 | Resolución: 16/01/23
 * 
 * Enunciado:
 * 
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
public class aronracso
{
    private static final String JUGADOR1 = "P1";
    private static final String JUGADOR2 = "P2";

    private static int puntosP1 = 0;
    private static int puntosP2 = 0;

    public static void main(String[] args)
    {
        System.out.println("Reto #2 - EL PARTIDO DE TENIS");
        System.out.println("-----------------------------");
        System.out.println();
        System.out.println("Comienza el partido, introduce \"" + JUGADOR1 + "\" o \"" + JUGADOR2 + 
            "\" y pulsa [enter] para indicar el ganador de cada set y mostrar el estado del partido");
        System.out.print("Introduce el ganador del set: ");
     
        try (Scanner scanner = new Scanner(System.in))
        {
            while(!procesarGanadorSet(scanner.nextLine()))
            {
                System.out.print("Introduce el ganador del set: ");
            }
        }
    }

    public static boolean procesarGanadorSet(String jugador)
    {
        switch(jugador)
        {
            case JUGADOR1:
            {
                if(puntosP2 > 3) {
                    //Rompe la ventaja del rival
                    puntosP2 -= 1;
                } else if(puntosP1 >= 3 && puntosP2 < 3) {
                    //Gana por ventaja suficiente, fuerzo la puntuación máxima
                    puntosP1 = 5;
                } else {
                    //Suma puntos
                    puntosP1 += 1;
                }

                break;
            }
            case JUGADOR2:
            {
                if(puntosP1 > 3) {
                    //Rompe la ventaja del rival
                    puntosP1 -= 1;
                } else if(puntosP2 >= 3 && puntosP1 < 3) {
                    //Gana por ventaja suficiente, fuerzo la puntuación máxima
                    puntosP2 = 5;
                } else {
                    //Suma puntos
                    puntosP2 += 1;
                }

                break;
            }
            default:
            {
                System.out.println(" - El jugador " + jugador + " no es correcto, se esperaba \"" + JUGADOR1 + "\" o \"" + JUGADOR2 + "\"");
                return false;
            }
        }

        mostrarPuntos();
        return (puntosP1 >= 5 || puntosP2 >= 5);
    }

    private static String traducirPuntos(int puntos)
    {
        switch(puntos)
        {
            case 0: return "Love";
            case 1: return "15";
            case 2: return "30";
            case 3: return "40";
            //case 4: return "Ventaja " + jugador;
            //case 5: return "Ha ganado " + jugador;
            default: return "";
        }
    }

    private static void mostrarPuntos()
    {
        if(puntosP1 >= 5) {
            System.out.println("Ha ganado " + JUGADOR1);
        } else if(puntosP2 >= 5) {
            System.out.println("Ha ganado " + JUGADOR2);
        } else if(puntosP1 == 3 && puntosP2 == 3) {
            System.out.println("Deuce");
        } else if(puntosP1 > 3) {
            System.out.println("Ventaja " + JUGADOR1);
        } else if(puntosP2 > 3) {
            System.out.println("Ventaja " + JUGADOR2);
        } else {
            System.out.println(
                traducirPuntos(puntosP1) + " - " +
                traducirPuntos(puntosP2));
        }
    }
}
