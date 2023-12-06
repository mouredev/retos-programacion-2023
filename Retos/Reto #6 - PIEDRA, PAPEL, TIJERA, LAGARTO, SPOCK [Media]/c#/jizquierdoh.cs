using System;
using System.Collections.Generic;

namespace RockPaperScissorsLizardSpock
{
  class Program
  {
    static void Main(string[] args)
    {
      string[][] moves = new string[][] {
                new string[] { "🗿", "✂️" },
                new string[] { "✂️", "🗿" },
                new string[] { "📄", "✂️" }
            };

      Console.WriteLine("Resultado: " + DetermineWinner(moves));
    }

    public static string DetermineWinner(string[][] moves)
    {
      Dictionary<string, Dictionary<string, string>> outcomes = new Dictionary<string, Dictionary<string, string>>
            {
                { "🗿", new Dictionary<string, string> { { "✂️", 1 }, { "📄", 0 }, { "🦎", 1 }, { "🖖", 0 } } },
                { "✂️", new Dictionary<string, string> { { "📄", 1 }, { "🦎", 0 }, { "🗿", 0 }, { "🖖", 1 } } },
                { "📄", new Dictionary<string, string> { { "🦎", 1 }, { "🖖", 0 }, { "🗿", 1 }, { "✂️", 0 } } },
                { "🦎", new Dictionary<string, string> { { "🖖", 1 }, { "🗿", 0 }, { "✂️", 1 }, { "📄", 0 } } },
                { "🖖", new Dictionary<string, string> { { "🗿", 1 }, { "✂️", 0 }, { "📄", 1 }, { "🦎", 0 } } }
            };

      int player1Wins = 0;
      int player2Wins = 0;

      foreach (string[] move in moves)
      {
        string player1 = move[0];
        string player2 = move[1];

        if (outcomes[player1][player2] == 1)
        {
          player1Wins++;
        }
        else if (outcomes[player2][player1] == 1)
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
}
