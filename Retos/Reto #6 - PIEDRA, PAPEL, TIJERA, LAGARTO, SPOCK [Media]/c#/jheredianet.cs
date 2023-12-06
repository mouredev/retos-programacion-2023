// Programado por Juan Carlos Heredia
// 2023-02-06
// Esta solución itera a través de cada par de jugadas y 
// luego utiliza una serie de condicionales para determinar 
// qué jugador gana o si hay un empate. Finalmente, se devuelve el resultado.


using System;

class Program
{
    static void Main(string[] args)
    {
        string[][] plays = new string[][]
        {
            new string[] {"🗿", "✂️"},
            new string[] {"✂️", "🗿"},
            new string[] {"📄", "✂️"}
        };

        Console.WriteLine(GetWinner(plays));
    }

    public static string GetWinner(string[][] plays)
    {
        int player1Wins = 0;
        int player2Wins = 0;

        foreach (string[] play in plays)
        {
            if ((play[0] == "🗿" && (play[1] == "✂️" || play[1] == "🦎")) ||
                (play[0] == "📄" && (play[1] == "🗿" || play[1] == "🖖")) ||
                (play[0] == "✂️" && (play[1] == "📄" || play[1] == "🦎")) ||
                (play[0] == "🦎" && (play[1] == "📄" || play[1] == "🖖")) ||
                (play[0] == "🖖" && (play[1] == "🗿" || play[1] == "✂️")))
            {
                player1Wins++;
            }
            else if ((play[1] == "🗿" && (play[0] == "✂️" || play[0] == "🦎")) ||
                     (play[1] == "📄" && (play[0] == "🗿" || play[0] == "🖖")) ||
                     (play[1] == "✂️" && (play[0] == "📄" || play[0] == "🦎")) ||
                     (play[1] == "🦎" && (play[0] == "📄" || play[0] == "🖖")) ||
                     (play[1] == "🖖" && (play[0] == "🗿" || play[0] == "✂️")))
            {
                player2Wins++;
            }
        }

        if (player1Wins > player2Wins)
        {
            return "Player 1";
        }
        else if (player2Wins > player1Wins)
        {
            return "Player 2";
        }
        else
        {
            return "Tie";
        }
    }
}
