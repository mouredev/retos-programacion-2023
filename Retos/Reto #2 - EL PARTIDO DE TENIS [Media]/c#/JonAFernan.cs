using System;
using System.Collections.Generic;

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

public class Program
{
  public static void Main()
  {
    
    string[] tenisGame = {"P1", "P1", "P2", "P2","P1", "P2","P1","P1"};
        
    PrintGame(tenisGame);
    
  }

  

  static void PrintGame (string[] game)
  {
    string [] tenisPoints = {"Love","15","30","40"};
    int player1Points = 0;
    int player2Points = 0;

    foreach (string point in game)
    {

        if(point == "P1") player1Points++;
        else if (point=="P2") player2Points ++;
        else
            {
               System.Console.WriteLine("El registro de partido no es correcto");
               break; 
            }
        if(player1Points == 3 && player2Points == 3)
            {
                
                Deuce(game);
                break;
            }
        if(player1Points == 4) System.Console.WriteLine("Ha ganado el P1");
        else if(player2Points == 4) System.Console.WriteLine("Ha ganado el P2");
        else System.Console.WriteLine(tenisPoints[player1Points] +" "+"-"+" " +tenisPoints[player2Points]);
       
    }

  }

  static void Deuce (string[] game)
  {
    int dP1Points = 0;
    int dP2Points = 0;
    System.Console.WriteLine("Deuce");
    for (int i = 6; i < game.Length; i++)
    {
        if(game [i] == "P1") dP1Points++;
        else if(game [i] == "P2") dP2Points++;
        else 
        {   
            System.Console.WriteLine("El registro de partido no es correcto");
            break;
        } 

        if (dP1Points == dP2Points) System.Console.WriteLine("Deuce");
        else if (dP1Points == dP2Points+1) System.Console.WriteLine("Ventaja P1");
        else if (dP2Points == dP1Points+1) System.Console.WriteLine("Ventaja P2");
        else if (dP1Points == dP2Points+2) System.Console.WriteLine("Ha ganado el P1");
        else if (dP2Points == dP1Points+2) System.Console.WriteLine("Ha ganado el P2");
    }
                
  }

}
