import java.util.ArrayList;
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

public class partido_tenis 
{
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        String [] secuencia = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        //String [] secuencia = {"P2", "P2", "P1", "P1", "P2", "P1","P2", "p2"};
        //String [] secuencia = {"P2", "P2", "P1", "P1", "P2", "P2"};
        //String [] secuencia = {"P1", "P1", "P2", "P2", "P1", "P1"};
        
        String puntaje_p1 = "love";
        String puntaje_p2 = "love";
        String Ganador = "";
        String Empate = "";

        List <String> marcador1 = new ArrayList<String>();
        List <String> marcador2 = new ArrayList<String>();

        marcador1.add(puntaje_p1);
        marcador2.add(puntaje_p2);

        for (int i=0; i<secuencia.length; i++)
        {
            if (secuencia[i].toString().equals("P1"))
            {  
                switch (puntaje_p1)
                {
                    case "love":
                        puntaje_p1 = "15";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "15":
                        puntaje_p1 = "30";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "30":
                        puntaje_p1="40";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "40":
                        if (puntaje_p2.equals("30") || puntaje_p2.equalsIgnoreCase("15") || puntaje_p2.equals("love"))
                        {
                           Ganador = "Ha ganado P1";  
                        }else{
                           Empate = "deuce";
                           puntaje_p1 = "Ad-in P1";
                           puntaje_p2 = "deuce";
                           marcador1.add(puntaje_p1);
                           marcador2.add(puntaje_p2);
                        }
                        break;
                    case "Ad-in P1":
                        
                        if (puntaje_p2.equals("deuce"))
                            {
                            Ganador = "Ha ganado P1";
                            
                        } else 
                            {
                            puntaje_p1="40";
                            puntaje_p2="40";
                            marcador1.add(puntaje_p1);
                            marcador2.add(puntaje_p2);
                            
                            }
                                   
                        break;
                }

            }else
            {
                switch (puntaje_p2)
                {
                    case "love":
                        puntaje_p2 = "15";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "15":
                        puntaje_p2 = "30";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "30":
                        puntaje_p2="40";
                        marcador1.add(puntaje_p1);
                        marcador2.add(puntaje_p2);
                        break;
                    case "40":
                        if (puntaje_p1.equals("30") || puntaje_p1.equalsIgnoreCase("15") || puntaje_p1.equals("love"))
                        {
                           Ganador = "Ha ganado P2";  
                        }else {
                            Empate = "deuce";
                            puntaje_p1 = "deuce";
                            puntaje_p2 = "Ad-in P2";
                            marcador1.add(puntaje_p1);
                            marcador2.add(puntaje_p2);

                        }
                        break;
                    case "Ad-in P2":
                        if (puntaje_p1.equals("deuce"))
                        {
                        Ganador = "Ha ganado P2";
                    
                         } else 
                        {
                            puntaje_p1="deuce";
                            puntaje_p2="deuce";
                            marcador1.add(puntaje_p1);
                            marcador2.add(puntaje_p2);
                        }
                        break;
                }
            }          
        }
        
       for (int j=0; j<marcador1.size(); j++)
        {
            if (marcador1.get(j).equals("40") && marcador2.get(j).equals("40"))
            {
                System.out.println(Empate);

            } else if (marcador1.get(j).equals("Ad-in P1") && marcador2.get(j).equals("deuce"))
            {
                System.out.println("Ventaja P1");
            } else if (marcador1.get(j).equals("deuce") && marcador2.get(j).equals("Ad-in P2"))
            {
                System.out.println("Ventaja P2");
            } else{
                System.out.print(marcador1.get(j) + " - " + marcador2.get(j) + "\n");
            }           
        }
        System.out.println(Ganador);
        //System.out.println(marcador1);
        //System.out.println(marcador2);
    }    
}