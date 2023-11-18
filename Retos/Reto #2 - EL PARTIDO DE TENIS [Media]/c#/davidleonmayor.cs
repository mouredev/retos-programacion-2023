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

public class TennisGame
{
    private int player1Score = 0;
    private int player2Score = 0;

    private string ScoreToTennisTerms(int score)
    {
        switch (score)
        {
            case 0: return "Love";
            case 1: return "15";
            case 2: return "30";
            case 3: return "40";
            default: return "Error";
        }
    }

    public void PlayGame(List<string> points)
    {
        foreach (string point in points)
        {
            if (point == "P1") player1Score++;
            else if (point == "P2") player2Score++;

            if (player1Score >= 3 && player2Score >= 3)
            {
                if (Math.Abs(player1Score - player2Score) >= 2)
                {
                    Console.WriteLine($"Player {(player1Score > player2Score ? "1" : "2")} wins");
                    return;
                }
                else if (player1Score == player2Score)
                {
                    Console.WriteLine("Deuce");
                    continue;
                }
                else
                {
                    Console.WriteLine($"Advantage Player {(player1Score > player2Score ? "1" : "2")}");
                    continue;
                }
            }

            Console.WriteLine($"{ScoreToTennisTerms(player1Score)} - {ScoreToTennisTerms(player2Score)}");
        }
    }

    static void Main(string[] args)
    {
        var game = new TennisGame();
        game.PlayGame(new List<string> { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" });
    }
}
