//# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
//#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

//## Enunciado

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

var input = new List<(string,string)>{ ("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️") };

int score1 = 0;

foreach (var item in input)
    score1 += DetermineWinner(item);

Console.WriteLine(score1 == 0 ? "Tie" : score1 > 1 ? "Player 1" : "Player 2");

static int DetermineWinner((string play1, string play2) play)
{
    // Empate
    if(play.play1 == play.play2) return 0;

    // Punto player 1
    if (play.play1 == "🗿" && (play.play2 == "✂️" || play.play2 == "🦎")) return 1;
    if (play.play1 == "✂️" && (play.play2 == "📄" || play.play2 == "🦎")) return 1;
    if (play.play1 == "📄" && (play.play2 == "🗿" || play.play2 == "🖖")) return 1;
    if (play.play1 == "🦎" && (play.play2 == "🖖" || play.play2 == "📄")) return 1;
    if (play.play1 == "🖖" && (play.play2 == "✂️" || play.play2 == "🗿")) return 1;

    // Punto player 2
    return -1;
}