/* Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
 *
 * Enunciado: 
 *
 *  Crea un programa que calcule quien gana más partidas al piedra,
 *  papel, tijera, lagarto, spock.
 * 
 *      - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 *      - La función recibe un listado que contiene pares, representando cada jugada.
 *      - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *          "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 *      - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 *      
 * Reglas:
 * 
 *     ✂️    cortan      📄
 *     📄    cubre       🗿
 *     🗿    aplasta     🦎
 *     🦎    envenena    🖖
 *     🖖    destruye    ✂️
 *     ✂️    decapita    🦎
 *     🦎    come        📄
 *     📄    desaprueba  🖖
 *     🖖    vaporiza    🗿
 *     🗿    aplasta     ✂️
 */

using System.Collections.Generic;
using System;
using System.Globalization;
using System.Linq;

Console.WriteLine("Reto #5: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK");
Console.WriteLine("----------------------------------------------\n");

var EmojiDict = new Dictionary<char, string>() {
    { '0', "🗿" },
    { '1', "📄" },
    { '2', "✂️" },
    { '3', "🦎" },
    { '4', "🖖" }
};

Console.WriteLine("Cómo se juega:\n");

Console.Write("El usuario debe introducir una cadena de texto con parejas de valores separados por comas. ");
Console.Write("El primer valor de cada pareja corresponde a una jugada del jugador 1. ");
Console.WriteLine("El segundo valor de cada pareja corresponde a una jugada del jugador 2.");

Console.WriteLine("\nValores:\n");
Console.WriteLine(" 0 -> Piedra:");
Console.WriteLine(" 1 -> Papel:");
Console.WriteLine(" 2 -> Tijera:");
Console.WriteLine(" 3 -> Lagarto:");
Console.WriteLine(" 4 -> Spock:");

Console.WriteLine("\nEjemplo: 00, 01, 21, 02 --> Gana jugador 1");

do
{
    Console.Write("\nIntroduce las jugadas separadas por comas: ");

    string userText = Console.ReadLine() ?? "";

    var Score = new ScoreBoard();

    try
    {
        string[] inputPlays = string.Concat(userText.Select(x => EmojiDict.ContainsKey(x) ? EmojiDict[x] : x.ToString())).Split(',');
        Console.WriteLine(Score.EvaluatePlays(inputPlays));

    }
    catch
    {
        Console.WriteLine("Se ha producido un error");
    }

} while (true);


// string[] inputPlays = new string[] { "📄📄", "🗿🦎", "🦎🗿" }; // Simula Console.Read();

class ScoreBoard
{
    private int _player1Score = 0;
    private int _player2Score = 0;

    public string Result
    {
        get => _player1Score > _player2Score ? "Player 1" :
               _player1Score < _player2Score ? "Player 2" :
               "Tie";
    }

    public string EvaluatePlays(string[] plays)
    {
        plays.ToList().ForEach(x => EvaluatePlay(x.Trim()));
        return Result;
    }

    public void EvaluatePlay(string play)
    {
        string[] winnerPlays = { "✂️📄", "📄🗿", "🗿🦎", "🦎🖖", "🖖✂️", "✂️🦎", "🦎📄", "📄🖖", "🖖🗿", "🗿✂️" };

        if (Array.IndexOf(winnerPlays, play) >= 0)
            _player1Score++;
        else if (Array.IndexOf(winnerPlays, string.Concat(SplitEmojis(play).Reverse())) >= 0)
            _player2Score++;
    }

    static string[] SplitEmojis(string input)
    {
        var emojiList = new List<string>();
        var enumerator = StringInfo.GetTextElementEnumerator(input);
        while (enumerator.MoveNext())
        {
            string element = enumerator.GetTextElement();
            emojiList.Add(element);
        }

        return emojiList.ToArray();
    }

}