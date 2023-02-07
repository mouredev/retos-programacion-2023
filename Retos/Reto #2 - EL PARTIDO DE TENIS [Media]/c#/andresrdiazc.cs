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
* - Consulta las reglas del juego si tienes dudas sobre el sistema de unidades.   
*/

using System.Numerics;

namespace Retos;

public enum Player
{
    P1, P2
}

public class RetoDos
{
    public static void Main(string[] args)
    {
        var playerPoints = new List<Player> { Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1 };
        TennisGame(playerPoints);
    }

    private static void TennisGame(List<Player> players)
    {
        string[] valoresPuntajes = { "Love", "15", "30", "40" };

        var pointsP1 = 0;
        var pointsP2 = 0;

        foreach (var player in players)
        {
            if (player == Player.P1)
            {
                pointsP1++;
            }
            else if (player == Player.P2)
            {
                pointsP2++;
            }

            if (pointsP1 >= 3 && pointsP2 >= 3)
            {
                if (pointsP1 == pointsP2)
                {
                    Console.WriteLine("Deuce");
                }
                else if (pointsP1 > pointsP2)
                {
                    Console.WriteLine($"Ventaja del P1: {pointsP1}");
                }
                else
                {
                    Console.WriteLine($"Ventaja del P2: {pointsP2}");
                }
            }
            else
            {
                if (pointsP1 < 4 && pointsP2 < 4)
                {
                    Console.WriteLine(valoresPuntajes[pointsP1] + " - " + valoresPuntajes[pointsP2]);
                }
            }
        }
        Console.WriteLine(pointsP1 > pointsP2 ? "Gana P1" : "Gana P2");
    }
}