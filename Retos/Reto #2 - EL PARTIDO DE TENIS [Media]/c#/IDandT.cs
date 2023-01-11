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
using System;

namespace Soluciones
{
  class Reto_02
  {
    static readonly string[] possiblePoints = { "Love", "15", "30", "40", "Advantage", "Win" };
    static readonly int[] playerPoints = { 0, 0 };
    static bool isDeuce = false;
    static string GetPoints(int playerIndex) => possiblePoints[playerPoints[playerIndex]];

    static void PlayGame(String[] winPoints)
    {
      foreach (String pointWinner in winPoints)
      {
        // Indices del jugador que marca, y del rival
        int playerIndex = pointWinner.ToUpper() == "P1" ? 0 : 1;
        int rivalIndex = pointWinner.ToUpper() == "P1" ? 1 : 0;

        // Si habia ventaja del rival, se la quitamos estabeciendo Deuce
        if (GetPoints(rivalIndex) == "Advantage")
        {
          playerPoints[rivalIndex] -= 1;
          isDeuce = true;
        }
        else
        {
          // Si era Deuce, damos ventaja al jugador que marca
          if (isDeuce)
          {
            playerPoints[playerIndex] += 1;
            isDeuce = false;
          }
          else
          {
            playerPoints[playerIndex] += 1;
            // Si despues de sumar el punto estan igualados a 40 es Deuce
            if (GetPoints(playerIndex) == "40" && GetPoints(rivalIndex) == "40")
              isDeuce = true;
            else
              // Si el rival tiene 30 puntos o menos, obtener ventaja equivale a victoria
              if (GetPoints(playerIndex) == "Advantage") playerPoints[playerIndex] += 1;
          }
        }

        // En funcion del resultado de la jugada mostramos el mensaje correspondiente
        Console.Write($"({pointWinner}) ");
        if (GetPoints(playerIndex) == "Win")
        {
          Console.WriteLine($"Ha ganado el {pointWinner}");
          return;
        }
        else if (isDeuce)
          Console.WriteLine("Deuce");
        else if (GetPoints(playerIndex) == "Advantage")
          Console.WriteLine($"Ventaja {pointWinner}");
        else
          Console.WriteLine($"{GetPoints(0)} - {GetPoints(1)}");
      }
    }

    static public void Main()
    {
      String[] winPoints = { "P1", "P2", "P1", "P2", "P2", "P1", "P1", "P2", "P2", "P1", "P2", "P2" };
      //String[] winPoints = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };

      PlayGame(winPoints);

      Console.ReadKey();
    }
  }
}