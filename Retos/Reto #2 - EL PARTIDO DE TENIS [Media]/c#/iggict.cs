
using System.Collections.Generic;
using System;

const string P1 = "P1";
const string P2 = "P2";

Dictionary<int, string> tennisDict = new()
{
    { 0, "Love"},
    { 1, "15"},
    { 2, "30"},
    { 3, "40"}
};

do
{
    string result;

    int player1 = 0;
    int player2 = 0;

    Console.Write("\nIntroduce la secuencia de puntos del juego (P1,P2,P1,etc.):");
    string points = Console.ReadLine() ?? "";

    var pointsArray = points.Split(',');

    foreach (var point in pointsArray)
    {
        if (point.Trim().ToUpper().Equals(P1))
            player1++;
        else if (point.Trim().ToUpper().Equals(P2))
            player2++;

        result = player1 == player2 && player1 >= 3 ? "Deuce" :
                 player1 > 3 && player1-player2 == 1 ? "Ventaja P1" :
                 player1 > 3 && player1-player2 > 1 ? "Ha ganado el P1" :
                 player2 > 3 && player2-player1 == 1 ? "Ventaja P2" :
                 player2 > 3 && player2-player1 > 1 ? "Ha ganado el P2" :
                 $"{tennisDict[player1]} - {tennisDict[player2]}";

        Console.WriteLine(result);

        if (result.StartsWith("Ha ganado"))
            break;
    }

} while (true);
