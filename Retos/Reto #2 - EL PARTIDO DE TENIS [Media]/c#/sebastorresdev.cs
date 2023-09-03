//// Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

// Enunciado

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


string[] games = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
string[] score = { "Love", "15", "30", "40"};

int score1 = 0, score2 = 0;

foreach (var game in games)
{
    if (game == "P1") score1++;
    if (game == "P2") score2++;

    // imprimir resultados
    if (score1 < 4 && score2 < 4)
    {
        Console.WriteLine($"{score[score1]} - {score[score2]}");
    }
    else
    {
        if (score1 == score2) Console.WriteLine("Deuce");
        else if (score1 - score2 > 1) Console.WriteLine("Ha ganado P1");
        else if (score2 - score1 > 1) Console.WriteLine("Ha ganado P2");
        else if (score1 > score2) Console.WriteLine("Ventaja P1");
        else Console.WriteLine("Ventaja P2");
    }
}