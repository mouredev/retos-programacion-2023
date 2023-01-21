using System;
using System.Linq;
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

    public static void PlayGame(string[] scores)
    {
        string[] points = { "LOVE", "15", "30", "40" };
        string[] players = { "P1", "P2" };
        int[] gameScores = { 0, 0 };

        if (scores.Any(score => !score.ToUpper().Equals("P1") && !score.ToUpper().Equals("P2")))
        {
            Console.WriteLine("Error en la puntuación, valores posibles: P1 o P2");
            return;
        }

        Console.WriteLine("INICIO PARTIDO");
        Console.WriteLine($"{points[gameScores[0]]} - {points[gameScores[1]]}");
        Console.WriteLine(string.Empty);

        for (int i = 0; i < scores.Length; i++)
        {
            int player = Array.IndexOf(players, scores[i].ToUpper());

            gameScores[player]++;

            if (gameScores[player] >= 4 && gameScores[player] - gameScores[1 - player] >= 2)
            {
                Console.WriteLine($"Ha ganado {players[player]}");
                break;
            }
            else if (gameScores[player] == gameScores[1 - player])
            {
                Console.WriteLine("Deuce");
            }
            else if (gameScores[player] >= 3 && gameScores[1 - player] >= 3)
            {
                Console.WriteLine($"Ventaja {players[player]}");
            }
            else
            {
                Console.WriteLine($"{points[gameScores[0]]} - {points[gameScores[1]]}");
            }

        }
    }
    public static void Main()
    {
        var scores = new string[] { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
        //var scores = new string[]{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","P2"};
        PlayGame(scores);
    }
}