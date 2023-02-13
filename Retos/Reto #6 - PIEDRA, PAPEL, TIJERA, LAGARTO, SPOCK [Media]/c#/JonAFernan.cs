namespace PiedraLAgartoSpook;

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

class Program{

    static void Main(string [] args)
    {
        string [,] gameArray = {{"Piedra" , "Tijera"} , {"Tijera","Piedra"} , {"Papel","Tijera"}};      
        System.Console.WriteLine(Game(gameArray));
    }

    static string Game(string [,] movesArray)
    {
        int player1Points = 0;
        int player2Points = 0;
        
        for (int i = 0; i < movesArray.GetLength(0); i++)
        {
            if(movesArray[i,0]== movesArray[i,1]) continue;
            if (WinningMovesDic[movesArray[i,0]].Contains(movesArray[i,1])) player1Points ++;
            else player2Points ++;

        }
        

        if(player1Points == player2Points) return "Tie";
        return player1Points > player2Points ? "Player1" : "Player2";
    }   
    
    static Dictionary<string ,string> WinningMovesDic = new Dictionary<string, string>(){
	{"Piedra", "Tijera, Lagarto"},
	{"Tijera", "Papel, Lagarto"},
	{"Papel", "Piedra, Spock"},
    {"Lagarto", "Piedra, Papel"},
    {"Spock", "Piedra, Tijera"}
};
}