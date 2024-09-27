import java.util.Scanner;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;

// Reto #2: EL PARTIDO DE TENIS
// Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

// Enunciado

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
 *   Ventaja P1 //si el jugador P1 marca tras estar empatados, si vuelve a marcar, gana
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

public class TaidaCR {
    
    //FALTA MANEJAR ERRORES
    public static void main(String[] args) {
        //input de quien marca
        //ir sumando a variables P1 y P2
        //validador P1/P2 (si introduce otra cosa error)
        //mensajes
        Scanner scanner = new Scanner(System.in);

        Map<Integer,String> correspPuntos= new HashMap<>();

        correspPuntos.put(0,"Love");
        correspPuntos.put(1,"15");
        correspPuntos.put(2,"30");
        correspPuntos.put(3,"40");

        //variable del bucle
        boolean r=true;
        String output="";
        int m1=0; 
        int m2=0;

        while (r){
            System.out.println("AUMENTAR MARCADOR: Introduce 1/2 para jugador 1/2: ");
            try{
                int punto= scanner.nextInt();
                //variable del segundo bucle
                boolean r2=true;
                while (r2) {
                    if (punto!=1&&punto!=2){
                        System.out.println("Tienes que introducir un número válido: 1 o 2");
                        punto= scanner.nextInt();
                    }else{
                        r2=false;
                    }
                }
                //OPCION 1 PARA SUMAR
                int puntos=0;
                puntos=(punto==1)?m1++:m2++;

                //OPCION 2 PARA SUMAR PUNTOS
                /*
                 * switch (punto){
                    case 1:
                        m1++;
                        break;
                    case 2:
                        m2++;
                        break;
                }
                 */
                
                int diferencia=Math.abs(m1-m2);
    
                if (m1==m2){
                    System.out.println("Deuce");
                }else if ((m1>3) || (m2>3)){ //|| ((m1>4) && (m2>4))
                    if (diferencia > 1){
                        output = ((m1>4) ? "     Gana Jugador 1" : "     Gana Jugador 2");
                        System.out.println("------>RESULTADO<------");
                        System.out.println();
                        System.out.println(output);
                        System.out.println();
                        System.out.println("---->FIN DEL JUEGO<----");
                        break;
                    }else{
                        output = ((m1>4) ? "Ventaja Jugador 1" : "Ventaja Jugador 2");
                        System.out.println(output);
                    }
                }else if ((m1<4) && (m2<4)){
                        System.out.println(correspPuntos.get(m1)+" - "+correspPuntos.get(m2));
                    }
                    //entrada en escaner errónea CUANDO INTRODUCE ALGO QUE NO ES UN NUMERO, YA QUE EL ESCANER ES PARA INT
            }catch(InputMismatchException e){
                System.out.println("Tienes que introducir uno de los dos números: 1 o 2");
                scanner.nextLine();
            }
        }
    scanner.close();
    }
}
            


    
