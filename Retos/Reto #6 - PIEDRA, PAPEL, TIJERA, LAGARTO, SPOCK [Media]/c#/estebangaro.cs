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
var winningCombs = new Tuple<options, options>[] { new(options.tijera, options.papel), new(options.papel, options.piedra), new(options.piedra, options.lagarto), new(options.lagarto, options.spock), new(options.spock, options.tijera), new(options.tijera, options.lagarto), new(options.lagarto, options.papel), new(options.papel, options.spock), new(options.spock, options.piedra), new(options.piedra, options.tijera) };
var combs = new Tuple<options, options>[] { new(options.piedra, options.tijera), new(options.tijera, options.piedra), new(options.papel, options.tijera) };
Console.WriteLine(play(combs));
string play(params Tuple<options, options>[] combs)
{
    int score1 = 0, score2 = 0;
    combs.ToList().ForEach(comb =>
    {
        bool r1 = false, r2 = false;
        if (comb.Item1 != comb.Item2 && winningCombs.Any(wc => (r1 = wc.Item1 == comb.Item1 && wc.Item2 == comb.Item2)
            || (r2 = wc.Item1 == comb.Item2 && wc.Item2 == comb.Item1)))
        {
            if (r1) score1++; else score2++;
        }
    });
    return score1 == score2 ? "Tie" : score1 > score2 ? "Player 1" : "Player 2";
}
enum options : byte { piedra = 0, papel = 1, tijera = 2, lagarto = 3, spock = 4 };