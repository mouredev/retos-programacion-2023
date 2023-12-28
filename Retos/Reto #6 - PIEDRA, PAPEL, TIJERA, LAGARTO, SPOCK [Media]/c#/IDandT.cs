/*
* Crea un programa que calcule quien gana más partidas al piedra,
* papel, tijera, lagarto, spock.
* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
* - La función recibe un listado que contiene pares, representando cada jugada.
* - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
*   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
* - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
* - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

    Tijeras✂️ cortan papel📄
    Papel📄 cubre piedra🗿
    Piedra🗿 aplasta lagarto🦎
    Lagarto🦎 envenena Spock🖖
    Spock🖖 destruye tijeras✂️
    Tijeras✂️ decapitan lagarto🦎
    Lagarto🦎 come papel📄
    Papel📄 desaprueba Spock🖖
    Spock🖖 vaporiza piedra🗿
    Piedra🗿 aplasta tijeras✂️
*/
using System;

namespace Soluciones
{
  class Reto_06
  {
    static readonly string[] winnerHandsPlayer1 = { "✂️📄", "📄🗿", "🗿🦎", "🦎🖖", "🖖✂️",
                                                    "✂️🦎", "🦎📄", "📄🖖", "🖖🗿", "🗿✂️" };
    static readonly string[] winnerHandsPlayer2 = { "📄✂️", "🗿📄", "🦎🗿", "🖖🦎", "✂️🖖",
                                                    "🦎✂️", "📄🦎", "🖖📄", "🗿🖖", "✂️🗿" };

    static bool CheckHand(string hand, string[] winnerHands) => Array.IndexOf(winnerHands, hand) >= 0;

    static void PlayGame(string[] hands)
    {
      int pointsPlayer1 = 0;
      int pointsPlayer2 = 0;
      foreach (string hand in hands)
      {
        if (CheckHand(hand, winnerHandsPlayer1)) pointsPlayer1++;
        else if (CheckHand(hand, winnerHandsPlayer2)) pointsPlayer2++;
      }

      Console.WriteLine($"{pointsPlayer1}  -  {pointsPlayer2}");
      if (pointsPlayer1 > pointsPlayer2) Console.WriteLine("Ganador: Player 1");
      else if (pointsPlayer2 > pointsPlayer1) Console.WriteLine("Ganador: Player 2");
      else Console.WriteLine("El resultado es un empate");
    }

    static public void Main()
    {
      string[] hands = { "✂️📄", "📄🦎", "🗿🗿", "🗿✂️", "🦎📄", "🦎🖖", "✂️🗿" };
      PlayGame(hands);
      Console.ReadKey();
    }
  }
}