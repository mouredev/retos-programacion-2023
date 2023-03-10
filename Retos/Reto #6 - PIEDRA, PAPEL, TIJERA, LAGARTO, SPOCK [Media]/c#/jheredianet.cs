// Programado por Juan Carlos Heredia
// 2023-02-06
// Esta soluciΓ³n itera a travΓ©s de cada par de jugadas y 
// luego utiliza una serie de condicionales para determinar 
// quΓ© jugador gana o si hay un empate. Finalmente, se devuelve el resultado.


using System;

class Program
{
    static void Main(string[] args)
    {
        string[][] plays = new string[][]
        {
            new string[] {"πΏ", "βοΈ"},
            new string[] {"βοΈ", "πΏ"},
            new string[] {"π", "βοΈ"}
        };

        Console.WriteLine(GetWinner(plays));
    }

    public static string GetWinner(string[][] plays)
    {
        int player1Wins = 0;
        int player2Wins = 0;

        foreach (string[] play in plays)
        {
            if ((play[0] == "πΏ" && (play[1] == "βοΈ" || play[1] == "π¦")) ||
                (play[0] == "π" && (play[1] == "πΏ" || play[1] == "π")) ||
                (play[0] == "βοΈ" && (play[1] == "π" || play[1] == "π¦")) ||
                (play[0] == "π¦" && (play[1] == "π" || play[1] == "π")) ||
                (play[0] == "π" && (play[1] == "πΏ" || play[1] == "βοΈ")))
            {
                player1Wins++;
            }
            else if ((play[1] == "πΏ" && (play[0] == "βοΈ" || play[0] == "π¦")) ||
                     (play[1] == "π" && (play[0] == "πΏ" || play[0] == "π")) ||
                     (play[1] == "βοΈ" && (play[0] == "π" || play[0] == "π¦")) ||
                     (play[1] == "π¦" && (play[0] == "π" || play[0] == "π")) ||
                     (play[1] == "π" && (play[0] == "πΏ" || play[0] == "βοΈ")))
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
