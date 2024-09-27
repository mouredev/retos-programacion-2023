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
using System.Linq;
using System.Timers;

namespace program
{
    public class Jankenpo
    {
        public static void Main()
        {
            var game = new (string, string)[] { ("Roca", "Tijeras"), ("Tijeras", "Roca"), ("Papel", "Tijeras") };
            var game2 = new (string, string)[] { ("Roca", "Tijeras"), ("Tijeras", "Roca"), ("Tijeras", "Tijeras") };
            var game3 = new (string, string)[] { ("Roca", "Tijeras"), ("Tijeras", "Roca"), ("Lagarto", "Papel") };
            Ganador(game);
            Ganador(game2);
            Ganador(game3);
        }
        public static void Ganador((string, string)[] game)
        {
            var rules = new Dictionary<string, List<string>>{
                { "Roca" , new List<string> { "Tijeras", "Lagarto" } },
                { "Papel" , new List<string> { "Roca", "Spock" } },
                { "Tijeras" , new List<string> { "Papel", "Lagarto" } },
                { "Lagarto" , new List<string> { "Papel", "Spock" } },
                { "Spock" , new List<string> { "Roca", "Tijeras" } }
            };
            var tie = 0;
            var player1 = 0;
            var player2 = 0;
            foreach (var tupla in game)
            {
                if (rules[tupla.Item1].Contains(tupla.Item2))
                {
                    player1++;
                }
                else if (tupla.Item1 == tupla.Item2)
                {
                    tie++;
                }
                else
                {
                    player2++;
                }
            }
            string result = player1 == player2 ? $"El resultado fue empate: {player1}/{player2}" :
                            player1 > player2 ? $"El ganador es el player 1, el resultado fue: {player1}/{player2}" : $"El ganador es el player 2, el resultado fue: {player1}/{player2}";
            Console.WriteLine(result);
        }
    }
}